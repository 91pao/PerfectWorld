# UE Core Rules

Use these rules for every Unreal Engine project task.

- Answer in Simplified Chinese unless the user explicitly asks otherwise
- Apply this plugin broadly to Unreal Engine C++, Blueprint, gameplay, UI, networking, assets/data, editor tooling, build, and configuration tasks
- Treat the user's current working directory and UE project workspace as read-only by default
- Do not edit source files, create draft or scratch files, run rewriting formatters, clean build artifacts, or otherwise mutate the worktree unless the user gives a hard direct-edit requirement
- A hard direct-edit requirement must clearly ask Codex to modify files or write into the project, such as "直接改文件", "修改项目代码", "apply patch", "写入工作目录", "你来实现并改代码", or equivalent wording
- Ambiguous requests such as "帮我实现", "修一下", "给我代码", "看看怎么改", or "处理这个问题" are not enough permission to mutate the worktree; use guided implementation or investigation mode instead
- Do not assume any concrete project module, class, function, directory, message identifier, data schema, or ownership model exists until it is found in the current workspace
- Treat existing project code as evidence, not automatic authority; prefer a candidate pattern only after confirming active callers, compatible lifecycle and ownership, and consistency with nearby maintained code
- Do not present non-trivial cross-system code as complete until the evidence, ownership, lifecycle, data/configuration, asset, authority, persistence, and cleanup paths required by `ue-evidence-maintainability-gates.md` are resolved
- Do not use generated, experimental, deprecated, copied sample, dead, or temporary code as a project precedent without independent evidence that it is the intended production pattern
- If no trustworthy project precedent exists, use the smallest standard Unreal Engine approach and state the assumption
- Do not run full UE builds, editor builds, packaging, or long compile commands unless the user explicitly asks
- If code is changed, state that UE was not built and ask the user to send local compile errors if any
- If code, config, plugin metadata, workflow rules, or transcription-ready code are produced, run the final self-review as a blocking closure gate before the final response
- Treat self-review findings as required actions: fix known in-scope bugs, remove avoidable complexity, rewrite when necessary, and rerun the review before delivery
- Treat maintainability without the AI conversation as a correctness requirement, not an optional style preference
- Do not refactor unrelated code, rename stable APIs, or move files merely to make code look cleaner
- During packaging or release-sensitive work, keep changes minimal and avoid touching stable flows unless explicitly requested
- Default UE code-writing and bug-fixing work to read-only guided implementation unless the user gives a hard direct-edit requirement
- Use `rg` first to discover project structure and relevant patterns before reading broad files
- Read source files with explicit UTF-8 when Chinese text is present or shell output looks suspicious
- For networked authority, replication, and RPC direction, also read `ue-client-server-boundary-rules.md`
