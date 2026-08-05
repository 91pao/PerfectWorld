# UE Project RAG Integration

Use this reference only when the `ue_rag_*` MCP tools are available.

- Call `ue_rag_status` before relying on indexed evidence. Build an index with `ue_rag_index` only when it is missing or stale.
- Use `ue_rag_search` to discover candidates for a specific symbol, system, Gameplay Tag, config key, asset name, or error string. Keep results bounded.
- Use `ue_rag_open` only for the strongest candidates, then inspect the original workspace files, configuration, and assets directly.
- Treat RAG as a discovery accelerator. It does not replace `rg`, direct source reads, active caller tracing, asset inspection, runtime validation, or the evidence gates in `ue-project-consistency.md`.
- Rebuild after a branch switch, broad refactor, or regenerated asset metadata. Fall back to direct project search when the index is unavailable, incomplete, or stale.
