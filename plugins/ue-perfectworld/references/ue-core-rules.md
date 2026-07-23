# UE Core Rules

Use these rules for every Unreal Engine project task.

- Answer in Simplified Chinese unless the user explicitly asks otherwise
- Treat the current UE project workspace as read-only unless the user clearly asks Codex to modify files, apply a patch, or write into the workspace
- Route ambiguous requests such as "帮我实现", "修一下", "给我代码", or "看看怎么改" to read-only implementation or investigation instead of mutating files
- Do not assume a project module, class, function, directory, message identifier, data schema, or ownership model exists until it is found in the current workspace
- Treat existing code as evidence rather than automatic authority; use `ue-project-consistency.md` before adopting a project-specific design
- For non-trivial cross-system work, do not propose code or new architecture until the mandatory evidence gate in `ue-project-consistency.md` has verified every applicable lifecycle link
- Resolve project questions through current-project search and end-to-end tracing before asking the user; reserve a final concise question for an external artifact or genuine product decision that the project cannot answer
- Use the smallest standard Unreal Engine approach and state the assumption when no trustworthy project precedent exists
- Do not run full UE builds, editor builds, packaging, or long compile commands unless the user explicitly asks
- When files are changed without a UE build, state that clearly and request the user's local compile result when relevant
- Do not refactor unrelated code, rename stable APIs, move files, or broaden the requested scope for cosmetic cleanup
- Use `rg` first to discover project structure and relevant patterns before reading broad files
- Read source files with explicit UTF-8 when Chinese text is present or shell output looks suspicious
- Load network, transaction, UI-contract, edit-safety, comment, and bug-fix references only when the current task actually needs them
