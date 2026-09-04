#!/usr/bin/env python3
"""Cross-agent entry point for the UE Project RAG stdio MCP server."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


def load_server():
    repository_root = Path(__file__).resolve().parents[2]
    server_path = repository_root / "plugins" / "ue-project-rag" / "server" / "ue_rag_mcp.py"
    specification = importlib.util.spec_from_file_location("perfectworld_ue_rag_server", server_path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"Unable to load UE Project RAG server: {server_path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


if __name__ == "__main__":
    load_server().main()
