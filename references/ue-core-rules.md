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

## Integration Timing Maps

- Before integrating with a shared framework or subsystem, draw a complete timing map (not a call graph): time on the horizontal axis, participants on the vertical axis, with the actual execution moment of every key function annotated. Use different line styles for synchronous calls and asynchronous callbacks.
- When the integrating party and the framework's original caller have different execution models (synchronous contract vs. deferred start, immediate return vs. completion callback), the timing map is the only tool that exposes the conflict before code is written. Reading what a function does is not the same as reading when it runs.
- Run the existing consumer's full flow once (via log timestamps or debugger) to establish the ground-truth timing before designing the integration. Do not assume the existing consumer's timing applies to the new consumer.

## Fail-Loud Error Handling

- When a lookup or derivation returns "unavailable" inside a flow that has already validated its preconditions, treat it as an invariant break: return failure with an Error log naming the missing object and the violated expectation. Never silently fall back to a default value — the fallback hides the broken invariant and lets a doomed flow continue with arbitrary parameters.
- Classify every default before using it: legitimate optional input (default allowed, no log), degradable failure (proceed degraded + Error/Warning trail so the degradation stays visible), or invariant break (fail loud). A named constant with a comment can still be a magic number — if it papers over class 3, it is a calibrated guess that drifts out of sync with config (incident: a 60s grace constant tuned by hand, silently wrong after any config or asset change).
- A lifetime that must cover an unpredictable process (presentation length, network wait) is owned by a renewal/keep-alive callback, never by a predicted constant or one-shot config-derived value. Predicted lifetimes expire silently at exactly the wrong moment; renewals fail loudly and immediately when the system is broken.
- Every swallowed failure needs a written justification at the swallow site: why the silent branch is the correct semantic (e.g., "session gone = delivery already cancelled, nothing to commit"), plus a Verbose log if the state could ever indicate a bug.

## Stage Gate Workflow

- The default path for any task whose endpoint is a project change (feature, bug fix, integration, asset or configuration change, or a paste-ready change specification) is S0 → S1 → S2 → S3 → S4 → S5 → S6. Small tasks may keep a stage brief, but no stage may be skipped, merged, or declared complete without its artifact.
- Announce the current stage and gate status at the top of every response. A stage counts as complete only when its named artifact exists in the conversation; announcing completion without the artifact is fabrication, not progress.
- S0 Requirement Intake: restate the goal, the hard scope, explicit non-goals, success criteria, and every question the project cannot answer. Artifact: the understanding card with open questions.
- S1 Evidence And Precedent Base: read-only. For every requirement point cite an existing capability (path:line) or name it as a gap; run the route-precedent check for integration points the framework already reserved; read precedents by timing, not by interface. Artifact: the evidence base. S0 and S1 may share one gate stop because both are read-only.
- S2 Change Specification: read-only. Artifact: the change manifest — every touched file with the intended change and anchors, configuration design, each item classified reuse/configure/extend/create where create must prove no existing capability fits, and zero-change proofs for neighboring paths. Unresolved S0 questions or unnamed S1 gaps block this gate. Gate: the user approves the manifest; this is the heaviest human gate.
- S3 Implementation: edit only manifest-approved files in small compilable steps; when the code shows the manifest is wrong, stop and amend the manifest for approval instead of silently expanding the edit. Artifact: the change set with a per-step self-review record and a residual-symbol sweep. User edit permission does not substitute for this gate — no approved manifest, no file edits.
- S4 Verification: write the probe checklist and expected values before any run; verify what can be verified (incremental build, PIE log acceptance by single request GUID per `ue-self-review.md`); list explicitly what was not run. Artifact: the verification record. Gate: the user sees the evidence or accepts the not-run list.
- S5 Adversarial Review: review the delivered change against the audits in `ue-self-review.md` (interruption and latecomer, survivor residue, runtime log acceptance) plus project consistency and overdesign. Artifact: findings ordered by severity, each with a fix and re-verification. Gate: no open P1/P2.
- S6 Delivery: write the development document (`ue-dev-doc`), prepare the single-ticket commit, and reconcile the delivery — every stage's audit fingerprint appears in the final response. Gate: the user confirms delivery; commits and pushes still need per-action consent.
- Between stages, stop and wait for explicit user approval (an answer to the gate question, "过", or "继续"). Never announce two stages' completions in one response; the shared S0+S1 stop is the only exception. If the user orders a stage skipped, name the skipped artifacts and risks in the response and proceed only on that explicit instruction — never advance silently.
