# UE Core Rules

Use these rules for every Unreal Engine project task.

- Answer in Simplified Chinese unless the user explicitly asks otherwise
- Treat planning, diagnosis-only, review-only, paste-ready code, and explicit no-edit requests as read-only. A clear request to implement, fix, or apply a change authorizes the necessary bounded file edits; do not require a special phrase such as "write into the workspace"
- Commit, push, reset, destructive restore, publication, and other separately restricted operations require authorization for that operation. Honor authorization already given; an implementation mandate alone does not authorize them
- Resolve genuinely ambiguous goals before dependent edits; a request such as "帮我实现" or "修一下" with an established target is an implementation mandate, while "先分析怎么改" remains planning
- Do not assume a project module, class, function, directory, message identifier, data schema, or ownership model exists until it is found in the current workspace
- Treat existing code as evidence rather than automatic authority; use `ue-project-consistency.md` before adopting a project-specific design
- Freeze the latest requirement and scope baseline, then pass the requirement-and-capability fit gate in `ue-project-consistency.md` before introducing compensating mechanisms or expanding the design
- For non-trivial cross-system work, do not propose code or new architecture until the mandatory evidence gate in `ue-project-consistency.md` has verified every applicable lifecycle link
- Resolve project questions through current-project search and end-to-end tracing before asking the user; reserve a final concise question for an external artifact or genuine product decision that the project cannot answer
- Use the smallest standard Unreal Engine approach and state the assumption when no trustworthy project precedent exists
- Do not run full UE builds, editor builds, packaging, or long compile commands unless the user explicitly asks; when the user authorizes build verification, prefer an incremental single-module build over a full build
- When files are changed without a UE build, state that clearly and request the user's local compile result when relevant
- Do not refactor unrelated code, rename stable APIs, move files, or broaden the requested scope for cosmetic cleanup
- Default to conservative code growth: reuse or configure verified capabilities first, then make the smallest complete local change. Every new mechanism needs a present requirement, a real consumer, and an evidenced gap; future flexibility alone is insufficient
- Minimize responsibilities, state, dependencies, and changed contracts rather than chasing line counts. Do not compress code into an unrelated owner or remove necessary validation just to touch fewer files
- Cleanup authority is bounded by the task. Remove this change's abandoned mechanisms, but do not delete or reformat unrelated upstream code or comments merely because a search finds no caller
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

## Integration Timing

- Trace the actual runtime type, overrides, local/server boundary, callbacks, and failure result before reusing a framework API. A familiar UE name does not prove standard engine behavior
- For an ordering-sensitive integration, keep a compact timing trace of the original and new consumers; draw a diagram when it clarifies a synchronous/asynchronous or request/acknowledgement difference
- Use existing logs or a permitted debugger run to verify timing when available. Without runtime access, continue independent source checks and mark timing unverified rather than inventing a protective mechanism

## Fail-Loud Error Handling

- When a lookup or derivation returns "unavailable" inside a flow that has already validated its preconditions, treat it as an invariant break: return failure with an Error log naming the missing object and the violated expectation. Never silently fall back to a default value — the fallback hides the broken invariant and lets a doomed flow continue with arbitrary parameters.
- Classify every default before using it: legitimate optional input (default allowed, no log), degradable failure (proceed degraded + Error/Warning trail so the degradation stays visible), or invariant break (fail loud). A named constant with a comment can still be a magic number — if it papers over class 3, it is a calibrated guess that drifts out of sync with config (incident: a 60s grace constant tuned by hand, silently wrong after any config or asset change).
- A lifetime that must cover an unpredictable process (presentation length, network wait) is owned by a renewal/keep-alive callback, never by a predicted constant or one-shot config-derived value. Predicted lifetimes expire silently at exactly the wrong moment; renewals fail loudly and immediately when the system is broken.
- Every swallowed failure needs a written justification at the swallow site: why the silent branch is the correct semantic (e.g., "session gone = delivery already cancelled, nothing to commit"), plus a Verbose log if the state could ever indicate a bug.

## User Preference Override

- When the user explicitly states a verification method (e.g., "PIE testing with log probes" over automated tests, or "return-path probes only" over tick-based monitoring), that preference overrides the plugin's default recommendations for the remainder of the session. Do not re-propose a mechanism the user has rejected unless new evidence changes the trade-off.
- Track rejected mechanisms per-session. After the user rejects an approach once, subsequent responses must not re-introduce it without citing the new evidence that justifies revisiting the decision.
- The same principle applies to scope minimization preferences: if the user prefers fewer touched files over stricter type guarantees (e.g., keeping `void` over changing to `bool` to avoid touching base-class files), respect that trade-off once stated.
- After resuming or compaction, recover the latest user mandate, hard boundaries, rejected approaches, confirmed author, and current change baseline from the actual conversation and files. A summary saying "approved" is not independent authorization.

## Parallel Agent Workflow

- For substantial work with separable responsibilities, use available subagents early for independent evidence gathering, bounded implementation, or review. The coordinator advances the critical path while they work; do not delegate everything and wait
- Adapt to the actual tools, available slots, and user preferences. A configured ceiling such as 12 is a limit, not a target or permission to exceed the runtime cap. Reuse agents; avoid duplicate investigations, empty roles, and recursive fan-out
- Give each agent a bounded goal, current requirements and exclusions, relevant evidence paths, allowed side effects, and expected result. Share current-task decisions and author confirmation so agents do not ask the user again
- Assign one writer per file, asset, registry, or other shared mutable resource. Serialize overlapping edits and ownership handoffs; use separate worktrees only when integration benefits justify them. Only one owner drives a build or shared editor session at a time
- Agree cross-file interfaces before parallel implementation. Report discoveries that invalidate another worker's assumption promptly; the coordinator integrates and checks the combined contract
- Review a stable diff with its baseline and relevant requirements. Reviewers receive source, configuration, and verification evidence, not an instruction to confirm the implementer's conclusion. An author does not supply their own independent review
- Start review of stable, independent portions while other work continues. Findings on a moving file are provisional until the reviewer checks the final integrated version
- Confirm findings before fixing them. Within the authorized scope, repair confirmed defects, remove unnecessary additions, run affected checks, and have the reviewer recheck the changed result. Do not stop merely to ask permission for each correction
- If a fix needs a new requirement or crosses a hard boundary, present that decision while continuing unblocked work. If iterations repeat without new evidence or progress, retrace the contract and report the concrete blocker instead of adding more patches
- When delegation is unavailable or the task is too small to benefit, perform the same checks locally and state the review's limits; never claim an independent agent review that did not occur

## S0-S6 Evidence Checkpoints

- Keep S0-S6 as a dependency-aware quality workflow, not seven mandatory user approval rounds. Checkpoints may share one compact record and run in one authorized turn; independent work may overlap, but implementation cannot outrun its required evidence or scope
- S0 Scope: identify the latest goal, hard boundaries, non-goals, and observable success criteria. Ask only for a missing decision that blocks dependent work
- S1 Evidence: verify the relevant owners, active capabilities, contracts, and lifecycle against current project files. Record source locations and specific gaps; parallelize independent questions
- S2 Change Specification: before edits, keep a compact manifest of intended files, behavior, reuse/configure/extend/create choices, and necessary new mechanisms. Give the user a short scope summary. A clear implementation mandate covers a plan inside that scope; separate S2 approval is needed only if requested by the user or a real decision or boundary change requires it
- S3 Implementation: assign bounded file ownership, make small coherent edits, and update the manifest as evidence resolves details within scope. Preserve unrelated changes and trace removed or renamed symbols
- S4 Verification: choose risk-relevant checks and expected outcomes before running them; use authorized checks and distinguish source, syntax, compile/UHT, editor, network, and packaged results. Missing runtime access does not block independent static checks
- S5 Review And Correction: independently review substantial integrated changes for requirement fit, project contracts, lifecycle, and unnecessary growth. Confirm and fix in-scope P1/P2 findings, then reverify and re-review affected paths on the latest version. Unresolved findings or required unavailable checks remain explicit limits, never a clean result
- S6 Delivery: report final behavior, scope, verification, review outcome, and remaining gaps. Reconcile C++, Lua, CSV, saved assets, and Git/P4 delivery where relevant. Produce a separate development document only when requested or required by the project
- Continue automatically across checkpoints covered by the existing mandate. Planning-only work ends with its plan; review-only work ends with findings. Pause dependent work only for a genuine unresolved decision, scope expansion, or separately unauthorized operation, and never reset completed checks merely to print stage labels
