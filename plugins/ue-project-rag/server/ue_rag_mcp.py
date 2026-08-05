#!/usr/bin/env python3
"""A dependency-free, local MCP retrieval server for Unreal Engine projects."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


INDEX_DIRECTORY = ".ue-rag"
DATABASE_NAME = "index.sqlite3"
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_RESULTS = 20
CHUNK_LINES = 120

SOURCE_SUFFIXES = {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx", ".cs"}
DOCUMENT_SUFFIXES = {".md", ".markdown", ".rst", ".txt"}
EXCLUDED_DIRECTORIES = {
    ".git",
    ".svn",
    ".vs",
    ".idea",
    "Binaries",
    "Build",
    "DerivedDataCache",
    "Intermediate",
    "Saved",
}
SENSITIVE_FILENAMES = {".env", ".netrc", "id_rsa", "id_ed25519"}
SENSITIVE_SUFFIXES = {".pem", ".pfx", ".key", ".keystore"}
TOKEN_PATTERN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|[\u4e00-\u9fff]+")
SYMBOL_PATTERN = re.compile(
    r"^\s*(?:UCLASS|USTRUCT|UENUM|class|struct|enum|namespace)\s*(?:\([^)]*\))?\s*([A-Za-z_]\w*)?"
)


@dataclass(frozen=True)
class Chunk:
    path: str
    kind: str
    symbol: str
    start_line: int
    end_line: int
    content: str


def validate_project_root(raw_root: str) -> Path:
    root = Path(raw_root).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"project_root is not a directory: {root}")
    return root


def database_path(root: Path) -> Path:
    return root / INDEX_DIRECTORY / DATABASE_NAME


def connect(root: Path) -> sqlite3.Connection:
    path = database_path(root)
    if not path.exists():
        raise ValueError("index is missing; call ue_rag_index first")
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA journal_mode = WAL;
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL,
            kind TEXT NOT NULL,
            symbol TEXT NOT NULL,
            start_line INTEGER NOT NULL,
            end_line INTEGER NOT NULL,
            content TEXT NOT NULL,
            content_hash TEXT NOT NULL,
            UNIQUE(path, start_line, end_line, kind)
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
            content,
            symbol,
            path,
            content='documents',
            content_rowid='id',
            tokenize='unicode61 remove_diacritics 2'
        );
        CREATE TRIGGER IF NOT EXISTS documents_ai AFTER INSERT ON documents BEGIN
            INSERT INTO documents_fts(rowid, content, symbol, path)
            VALUES (new.id, new.content, new.symbol, new.path);
        END;
        CREATE TRIGGER IF NOT EXISTS documents_ad AFTER DELETE ON documents BEGIN
            INSERT INTO documents_fts(documents_fts, rowid, content, symbol, path)
            VALUES ('delete', old.id, old.content, old.symbol, old.path);
        END;
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        """
    )


def should_exclude(path: Path, root: Path) -> bool:
    relative_parts = path.relative_to(root).parts
    if any(part in EXCLUDED_DIRECTORIES for part in relative_parts[:-1]):
        return True
    if path.name in SENSITIVE_FILENAMES or path.suffix.lower() in SENSITIVE_SUFFIXES:
        return True
    return False


def classify(path: Path) -> str | None:
    lower_name = path.name.lower()
    if lower_name.endswith(".build.cs") or lower_name.endswith(".target.cs"):
        return "source"
    if path.suffix.lower() in SOURCE_SUFFIXES:
        return "source"
    if path.suffix.lower() == ".ini":
        return "config"
    if path.suffix.lower() in DOCUMENT_SUFFIXES:
        return "document"
    return None


def file_content(path: Path) -> str | None:
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return None
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def named_line(line: str) -> str:
    match = SYMBOL_PATTERN.match(line)
    if match and match.group(1):
        return match.group(1)
    function_match = re.search(r"\b([A-Za-z_]\w*(?:::[A-Za-z_]\w*)?)\s*\([^;{}]*\)\s*(?:const\s*)?(?:\{|$)", line)
    return function_match.group(1) if function_match else ""


def fixed_line_chunks(relative_path: str, kind: str, content: str) -> Iterable[Chunk]:
    lines = content.splitlines()
    current_symbol = ""
    for offset in range(0, len(lines), CHUNK_LINES):
        block = lines[offset : offset + CHUNK_LINES]
        for line in block:
            symbol = named_line(line)
            if symbol:
                current_symbol = symbol
                break
        yield Chunk(
            path=relative_path,
            kind=kind,
            symbol=current_symbol,
            start_line=offset + 1,
            end_line=offset + len(block),
            content="\n".join(block),
        )


def section_chunks(relative_path: str, kind: str, content: str, marker: re.Pattern[str]) -> Iterable[Chunk]:
    lines = content.splitlines()
    starts = [index for index, line in enumerate(lines) if marker.match(line)] or [0]
    for position, start in enumerate(starts):
        end = starts[position + 1] if position + 1 < len(starts) else len(lines)
        block = lines[start:end]
        if not block:
            continue
        symbol_match = marker.match(lines[start])
        symbol = symbol_match.group(1).strip() if symbol_match and symbol_match.groups() else ""
        if len(block) <= CHUNK_LINES:
            yield Chunk(relative_path, kind, symbol, start + 1, end, "\n".join(block))
            continue
        for offset in range(0, len(block), CHUNK_LINES):
            part = block[offset : offset + CHUNK_LINES]
            yield Chunk(relative_path, kind, symbol, start + offset + 1, start + offset + len(part), "\n".join(part))


def chunks_for_file(root: Path, path: Path, kind: str, content: str) -> Iterable[Chunk]:
    relative_path = path.relative_to(root).as_posix()
    if kind == "config":
        yield from section_chunks(relative_path, kind, content, re.compile(r"^\s*\[([^]]+)\]\s*$"))
    elif kind == "document":
        yield from section_chunks(relative_path, kind, content, re.compile(r"^#{1,6}\s+(.+?)\s*$"))
    else:
        yield from fixed_line_chunks(relative_path, kind, content)


def asset_chunks(root: Path) -> Iterable[Chunk]:
    metadata_path = root / INDEX_DIRECTORY / "assets.json"
    if not metadata_path.exists():
        return
    try:
        data = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return
    records = data if isinstance(data, list) else data.get("assets", []) if isinstance(data, dict) else []
    for number, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            continue
        asset_path = str(record.get("object_path") or record.get("package_name") or record.get("path") or f"asset-{number}")
        symbol = str(record.get("asset_name") or record.get("class") or asset_path.rsplit("/", 1)[-1])
        content = json.dumps(record, ensure_ascii=False, sort_keys=True)
        yield Chunk(".ue-rag/assets.json", "asset", symbol, number, number, f"{asset_path}\n{content}")


def content_hash(chunk: Chunk) -> str:
    value = f"{chunk.path}\0{chunk.kind}\0{chunk.start_line}\0{chunk.end_line}\0{chunk.content}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def rebuild_index(raw_root: str) -> dict[str, Any]:
    root = validate_project_root(raw_root)
    index_dir = root / INDEX_DIRECTORY
    index_dir.mkdir(exist_ok=True)
    connection = sqlite3.connect(database_path(root))
    try:
        create_schema(connection)
        connection.execute("DELETE FROM documents")
        scanned_files = 0
        indexed_chunks = 0
        for path in root.rglob("*"):
            if not path.is_file() or should_exclude(path, root):
                continue
            kind = classify(path)
            if not kind:
                continue
            content = file_content(path)
            if content is None:
                continue
            scanned_files += 1
            for chunk in chunks_for_file(root, path, kind, content):
                if not chunk.content.strip():
                    continue
                connection.execute(
                    "INSERT INTO documents(path, kind, symbol, start_line, end_line, content, content_hash) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (chunk.path, chunk.kind, chunk.symbol, chunk.start_line, chunk.end_line, chunk.content, content_hash(chunk)),
                )
                indexed_chunks += 1
        for chunk in asset_chunks(root):
            connection.execute(
                "INSERT INTO documents(path, kind, symbol, start_line, end_line, content, content_hash) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (chunk.path, chunk.kind, chunk.symbol, chunk.start_line, chunk.end_line, chunk.content, content_hash(chunk)),
            )
            indexed_chunks += 1
        connection.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES ('root', ?)", (str(root),))
        connection.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES ('version', '1')")
        connection.commit()
        return {"project_root": str(root), "scanned_files": scanned_files, "indexed_chunks": indexed_chunks, "index_path": str(database_path(root))}
    finally:
        connection.close()


def search_index(raw_root: str, query: str, scopes: list[str] | None = None, limit: int = 8) -> dict[str, Any]:
    root = validate_project_root(raw_root)
    tokens = TOKEN_PATTERN.findall(query)
    if not tokens:
        raise ValueError("query must contain a searchable token")
    limit = max(1, min(int(limit), MAX_RESULTS))
    fts_query = " OR ".join(f'"{token.replace(chr(34), "")}"' for token in tokens)
    filters: list[str] = []
    parameters: list[Any] = [fts_query]
    if scopes:
        allowed = sorted({scope for scope in scopes if scope in {"source", "config", "document", "asset"}})
        if not allowed:
            raise ValueError("scopes must contain source, config, document, or asset")
        filters.append("documents.kind IN ({})".format(",".join("?" for _ in allowed)))
        parameters.extend(allowed)
    where = " AND " + " AND ".join(filters) if filters else ""
    parameters.append(limit)
    connection = connect(root)
    try:
        rows = connection.execute(
            """
            SELECT documents.id, documents.path, documents.kind, documents.symbol,
                   documents.start_line, documents.end_line, documents.content,
                   bm25(documents_fts, 1.0, 5.0, 2.0) AS rank
            FROM documents_fts
            JOIN documents ON documents.id = documents_fts.rowid
            WHERE documents_fts MATCH ?
            """ + where + " ORDER BY rank LIMIT ?",
            parameters,
        ).fetchall()
    finally:
        connection.close()
    results = []
    for row in rows:
        excerpt = row["content"].strip().replace("\x00", "")
        if len(excerpt) > 1200:
            excerpt = excerpt[:1200] + "\n..."
        results.append(
            {
                "result_id": row["id"],
                "path": row["path"],
                "kind": row["kind"],
                "symbol": row["symbol"],
                "start_line": row["start_line"],
                "end_line": row["end_line"],
                "score": round(float(-row["rank"]), 4),
                "excerpt": excerpt,
            }
        )
    return {"project_root": str(root), "query": query, "result_count": len(results), "results": results}


def open_result(raw_root: str, result_id: int) -> dict[str, Any]:
    root = validate_project_root(raw_root)
    connection = connect(root)
    try:
        row = connection.execute(
            "SELECT id, path, kind, symbol, start_line, end_line, content FROM documents WHERE id = ?",
            (int(result_id),),
        ).fetchone()
    finally:
        connection.close()
    if not row:
        raise ValueError(f"result_id does not exist: {result_id}")
    return {
        "result_id": row["id"],
        "project_root": str(root),
        "path": row["path"],
        "kind": row["kind"],
        "symbol": row["symbol"],
        "start_line": row["start_line"],
        "end_line": row["end_line"],
        "content": row["content"],
    }


def index_status(raw_root: str) -> dict[str, Any]:
    root = validate_project_root(raw_root)
    path = database_path(root)
    if not path.exists():
        return {"project_root": str(root), "ready": False, "index_path": str(path)}
    connection = connect(root)
    try:
        total = connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        kinds = dict(connection.execute("SELECT kind, COUNT(*) FROM documents GROUP BY kind").fetchall())
    finally:
        connection.close()
    return {"project_root": str(root), "ready": True, "index_path": str(path), "chunk_count": total, "chunks_by_kind": kinds}


TOOLS = [
    {
        "name": "ue_rag_index",
        "description": "Build or replace the local evidence index for a UE project. Generated directories and common secret files are excluded.",
        "inputSchema": {"type": "object", "properties": {"project_root": {"type": "string"}}, "required": ["project_root"], "additionalProperties": False},
    },
    {
        "name": "ue_rag_search",
        "description": "Search indexed UE project evidence. Results are candidates that must be verified against the original project files.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "project_root": {"type": "string"},
                "query": {"type": "string"},
                "scopes": {"type": "array", "items": {"type": "string", "enum": ["source", "config", "document", "asset"]}},
                "limit": {"type": "integer", "minimum": 1, "maximum": MAX_RESULTS},
            },
            "required": ["project_root", "query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "ue_rag_open",
        "description": "Open one indexed evidence chunk by result_id.",
        "inputSchema": {"type": "object", "properties": {"project_root": {"type": "string"}, "result_id": {"type": "integer"}}, "required": ["project_root", "result_id"], "additionalProperties": False},
    },
    {
        "name": "ue_rag_status",
        "description": "Report whether a UE project has a local retrieval index and its coverage by evidence type.",
        "inputSchema": {"type": "object", "properties": {"project_root": {"type": "string"}}, "required": ["project_root"], "additionalProperties": False},
    },
]


def call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if name == "ue_rag_index":
        return rebuild_index(arguments["project_root"])
    if name == "ue_rag_search":
        return search_index(arguments["project_root"], arguments["query"], arguments.get("scopes"), arguments.get("limit", 8))
    if name == "ue_rag_open":
        return open_result(arguments["project_root"], arguments["result_id"])
    if name == "ue_rag_status":
        return index_status(arguments["project_root"])
    raise ValueError(f"unknown tool: {name}")


def response(request_id: Any, result: Any = None, error: dict[str, Any] | None = None) -> None:
    payload: dict[str, Any] = {"jsonrpc": "2.0", "id": request_id}
    if error is not None:
        payload["error"] = error
    else:
        payload["result"] = result
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def serve() -> None:
    for raw_line in sys.stdin:
        try:
            request = json.loads(raw_line)
            method = request.get("method")
            request_id = request.get("id")
            if method == "notifications/initialized":
                continue
            if method == "initialize":
                response(request_id, {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "ue-project-rag", "version": "0.1.0"}})
            elif method == "tools/list":
                response(request_id, {"tools": TOOLS})
            elif method == "tools/call":
                params = request.get("params", {})
                try:
                    result = call_tool(params["name"], params.get("arguments", {}))
                    response(request_id, {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}]})
                except (KeyError, TypeError, ValueError, sqlite3.Error) as error:
                    response(request_id, {"content": [{"type": "text", "text": str(error)}], "isError": True})
            elif method == "ping":
                response(request_id, {})
            elif request_id is not None:
                response(request_id, error={"code": -32601, "message": f"method not found: {method}"})
        except json.JSONDecodeError:
            continue
        except Exception as error:  # Keep one bad request from terminating the MCP session.
            if "request_id" in locals() and request_id is not None:
                response(request_id, error={"code": -32603, "message": str(error)})


def main() -> None:
    parser = argparse.ArgumentParser(description="Local UE project retrieval MCP server")
    parser.add_argument("--index", metavar="PROJECT_ROOT", help="Build an index without starting the MCP server")
    parser.add_argument("--status", metavar="PROJECT_ROOT", help="Report index status without starting the MCP server")
    arguments = parser.parse_args()
    if arguments.index:
        print(json.dumps(rebuild_index(arguments.index), ensure_ascii=False, indent=2))
    elif arguments.status:
        print(json.dumps(index_status(arguments.status), ensure_ascii=False, indent=2))
    else:
        serve()


if __name__ == "__main__":
    main()
