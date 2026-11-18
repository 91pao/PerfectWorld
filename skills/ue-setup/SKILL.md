---
name: ue-setup
description: Initialize UE PerfectWorld with a default Codex ceiling of 12 spawned agents, locate the Unreal project, and check optional ue_rag tools. Configuration checks remain read-only. Do not use for feature work, diagnosis, implementation, or review.
---

# UE PerfectWorld Setup

Use this workflow after installation or when the user asks to initialize or inspect plugin configuration. An initialization or concurrency-configuration request authorizes the bounded configuration edit below; a question, inspection-only request, or explicit no-edit instruction remains read-only. Honor an explicit user-selected ceiling instead of the default 12.

1. Briefly summarize conservative code growth, parallel agents, and S0-S6 evidence checkpoints. Explain that an authorized task can advance through them in one turn; real decisions and scope changes still require the user.
2. Inspect or configure the Codex subagent ceiling as described below. Do not request another approval when the user's existing setup or configuration mandate covers this edit.
3. Identify the current Unreal project by checking the current workspace and its parent directories for a `.uproject` file. Do not scan unrelated drives or directories.
4. Check whether `ue_rag_status`, `ue_rag_search`, `ue_rag_open`, and `ue_rag_index` are present in the available tools.
5. If the RAG tools are present, call `ue_rag_status` and report whether an index exists and whether it is current. Do not build or modify an index during onboarding.
6. If the RAG tools are absent, explain that RAG is an optional external integration, then show the direct-search fallback (`rg` and source-file reads). Do not claim RAG is installed or configured.
7. Report only what was verified. Do not change project files, create an index, or modify preferences beyond the authorized concurrency key.

## Codex Subagent Ceiling

- Resolve configuration on the execution host: `$CODEX_HOME/config.toml` when set, otherwise `~/.codex/config.toml`. Honor an explicitly supplied isolated configuration directory; never substitute the real user configuration during an evaluation.
- Parse existing TOML before editing. For initialization, set the following user-level value to 12 unless the user specified another ceiling; create the file or table only if absent. For inspection-only requests, report the current value without writing.

```toml
[agents]
max_concurrent_threads_per_session = 12
```

- Patch only this key and, if present in the same table, replace its legacy alias `max_threads`; do not leave conflicting aliases or duplicate `[agents]` tables. Preserve unrelated settings, comments, encoding, and newline style. If the requested value already exists without an alias, do not rewrite the file.
- Parse the result again, verify the requested integer, and confirm all unrelated configuration values survived. Do not print the full configuration or credentials. Invalid TOML or a failed edit is a reported setup failure, not permission to regenerate the whole file.
- Check known active profile, project, command-line, or managed overrides and whether agents are disabled. Report any conflicting source; do not silently rewrite other scopes, enable tools, or weaken policy. A saved user-level value does not prove the effective ceiling.
- This setting counts spawned agents, excluding the primary agent. Keep the saved ceiling separate from the current session's observed slots. Do not claim live expansion, automatically restart Codex, spawn 12 test agents, or retry against a runtime cap; report when reloading or starting a new session remains unverified.

Keep the setup result short: configuration path and saved ceiling (or unchanged/read-only/failure), observed runtime capacity or unverified, project path, and RAG status. Merely installing or mentioning the plugin does not execute this setup.

Official configuration reference: `https://learn.chatgpt.com/docs/config-file/config-reference`
