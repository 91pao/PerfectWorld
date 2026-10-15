---
name: ue-setup
description: Run after installing UE PerfectWorld to explain its workflow, locate the current Unreal project, and check whether optional ue_rag tools are available. Do not use for feature work, diagnosis, implementation, or review.
---

# UE PerfectWorld Setup

Use this onboarding workflow once after installation or when the user explicitly asks how the plugin is configured.

1. Briefly summarize the plugin's purpose and its S0-S6 stage gates. Do not skip, merge, or weaken any stage.
2. Identify the current Unreal project by checking the current workspace and its parent directories for a `.uproject` file. Do not scan unrelated drives or directories.
3. Check whether `ue_rag_status`, `ue_rag_search`, `ue_rag_open`, and `ue_rag_index` are present in the available tools.
4. If the RAG tools are present, call `ue_rag_status` and report whether an index exists and whether it is current. Do not build or modify an index during onboarding.
5. If the RAG tools are absent, explain that RAG is an optional external integration, then show the direct-search fallback (`rg` and source-file reads). Do not claim RAG is installed or configured.
6. Report only what was verified. Do not change project files, plugin settings, or user preferences.

Keep the setup result short: project path (or not found), RAG tool availability/status, and the next usable command or skill for the user's intended task.
