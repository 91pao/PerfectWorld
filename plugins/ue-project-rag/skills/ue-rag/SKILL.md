---
name: ue-rag
description: Retrieve bounded, cited Unreal Engine project evidence through the optional UE Project RAG MCP server. Use for large UE projects when the server is installed and an index is available.
---

# UE Project RAG

Use this skill only when the `ue_rag_*` MCP tools are available. The first release uses local structured and full-text retrieval only; it is an evidence-discovery layer, not a source of truth and not a replacement for reading the original project files.

## Workflow

1. Call `ue_rag_status` for the project root.
2. If no index exists, call `ue_rag_index` once before the first search.
3. Call `ue_rag_search` with a precise symbol, feature name, Gameplay Tag, config key, asset name, or error text. Keep `limit` at 8 or lower unless evidence is sparse.
4. Open only the most relevant candidates with `ue_rag_open`.
5. Verify every candidate against the actual workspace source, configuration, or asset before using it as project evidence.

## Boundaries

- Never treat similarity score or a retrieved excerpt as proof of ownership, lifecycle, authority, persistence, cleanup, or active production use.
- Do not infer a Blueprint's runtime behavior from Asset Registry metadata alone.
- Use `rg` and direct project reads when RAG is unavailable, stale, incomplete, or returns no verified precedent.
- Rebuild the index after broad refactors, branch switches, generated asset metadata changes, or when results become stale.
- Keep MCP results compact. Search first, then open only the evidence needed for the current decision.
