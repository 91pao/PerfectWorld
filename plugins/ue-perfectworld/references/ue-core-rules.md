# UE Core Rules

Use these rules for every Unreal Engine project task.

- Answer in Simplified Chinese unless the user explicitly asks otherwise
- Treat the current UE project workspace as read-only unless the user clearly asks Codex to modify files, apply a patch, or write into the workspace
- Version-control mutations (commit, reset, push, or file-level checkout) require per-action user consent, even when file edits are already authorized; a chat-delivery preference for patches extends to git operations
- Route ambiguous requests such as "帮我实现", "修一下", "给我代码", "看看怎么改" to read-only implementation or investigation instead of mutating files
- Do not assume a project module, class, function, directory, message identifier, data schema, or ownership model exists until it is found in the current workspace
- Treat existing code as evidence rather than automatic authority; use `ue-project-consistency.md` before adopting a project-specific design
- Freeze the latest requirement and scope baseline, then pass the requirement-and-capability fit gate in `ue-project-consistency.md` before introducing compensating mechanisms or expanding the design
- For non-trivial cross-system work, do not propose code or new architecture until the mandatory evidence gate in `ue-project-consistency.md` has verified every applicable lifecycle link
- Resolve project questions through current-project search and end-to-end tracing before asking the user; reserve a final concise question for an external artifact or genuine product decision that the project cannot answer
- Use the smallest standard Unreal Engine approach and state the assumption when no trustworthy project precedent exists
- Do not run full UE builds, editor builds, packaging, or long compile commands unless the user explicitly asks; when the user authorizes build verification, prefer an incremental single-module build over a full build
- When files are changed without a UE build, state that clearly and request the user's local compile result when relevant
- Do not refactor unrelated code, rename stable APIs, move files, or broaden the requested scope for cosmetic cleanup
- Use `rg` first to discover project structure and relevant patterns before reading broad files
- Before claiming a symbol, API, or string is absent from the project, validate the search with a known positive control: run the same command on a symbol known to exist, and treat a zero-result search as unverified until the control also matches
- On Windows shells, avoid search patterns that begin with `/` (MSYS path conversion) and embedded double quotes (argument mangling); prefer hex escapes such as `\x22` or character classes, and remember `rg -v` filters whole lines by substring and can hide valid qualified call sites
- When the optional `ue_rag_*` MCP tools are available, use them only to discover bounded candidates in large projects, then verify candidates with direct project reads before treating them as evidence
- Do not use a RAG score, excerpt, or asset metadata as proof of active ownership, lifecycle, authority, persistence, cleanup, or Blueprint runtime behavior
- Read source files with explicit UTF-8 when Chinese text is present or shell output looks suspicious
- Load network, transaction, UI-contract, comment, and bug-fix references only when the current task actually needs them

## Common Reference Set

Every UE workflow skill loads the following; skill files list only their additional references:

- Always: `ue-project-consistency.md`
- Shared component, manager, subsystem, pool, resource loader, factory, base class, public API, or multiple active consumers: `ue-architecture.md`
- C++ readability or the C++/Blueprint handoff: `ue-code-style.md`
- Before delivering code, direct edits, or review conclusions: `ue-self-review.md`
- Before editing project files: `ue-edit-safety.md`

## Routing Architecture Rules

- Do not treat the first named caller as the owner when the request mentions a common, public, generic, pooled, or reusable capability; classify local business logic versus shared infrastructure before choosing files or mechanisms
- For asynchronous resource or initialization work, pass the architecture check before accepting Tick polling; Tick is reserved for continuous progression, tracking, simulation, or parameter updates
