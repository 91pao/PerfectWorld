# UE Final Self Review

Run this as a blocking closure gate after implementation or implementation guidance and before the final response.

## Correctness Gate

- Recheck every changed or proposed file against the loaded rules and the user's requested behavior
- Trace the primary success path and important failure paths end to end
- Confirm every project-specific assumption was discovered in the current workspace
- Confirm chosen precedents have active production evidence and compatible ownership, lifecycle, authority, and responsibility
- Confirm no generated, deprecated, experimental, dead, sample, or temporary implementation was copied without independent justification
- Recheck Unreal reflection declarations, includes, module dependencies, object lifetime, ownership, null handling, delegates, threading, networking, asset/configuration references, and persistence where applicable
- For bug fixes, confirm the root cause is corrected locally instead of hidden by fallback state, retries, delays, or silent returns
- For networked work, confirm authority, ownership, validation, replication, reliability, and failure feedback
- For resource or transaction work, confirm validation, mutation, persistence, duplicate handling, and success timing
- For security, safety, or bug-sensitive work, confirm unsafe behavior is blocked rather than merely logged

## Simplicity Gate

- Compare the result with the smallest project-consistent implementation that fully satisfies the current requirement
- Treat a solution that is several times larger than necessary, such as roughly 300 lines for work that can be expressed clearly in about 50, as a failed review and rewrite it before delivery
- Use line count as a warning signal, not a code-golf target; retain required correctness, authority, lifecycle, validation, diagnostics, and readability
- Judge implementation complexity separately from useful teaching-comment volume; do not remove accurate instructional comments merely to reduce line count
- Remove speculative extension points, unused state, duplicate logic, unnecessary files, classes, managers, services, wrappers, helpers, result types, delegates, RPCs, compatibility branches, timers, retries, caches, and configuration
- Do not preserve overdesign merely because it has already been written
- Keep an abstraction only when it matches a verified project convention, removes meaningful present duplication, or materially improves correctness or testability
- Confirm the implementation did not broaden a focused task into an architecture rewrite

## Delivery Gate

- For direct implementation, fix every known in-scope correctness defect and rewrite avoidable complexity before the final response
- For guided implementation, correct the conversation code and teaching sequence before presenting it; do not hand the user a known bug or an overdesigned version to type
- For review-only or investigation-only work without edit authorization, report discovered defects instead of modifying files, but keep the proposed remedy minimal and internally coherent
- After any correction or simplification, run the correctness and simplicity gates again
- Do not finalize while a known, in-scope, fixable defect remains in produced code or while a clearly simpler complete design is available
- Do not hide unresolved uncertainty; identify missing evidence and avoid claiming unverified code is compile-ready

## Final Checks

- For guided implementation, confirm every required change is ordered and complete, code blocks contain no pseudocode, ellipses, placeholders, TODOs, or omitted branches, and project symbols were verified before claiming the code is transcription-ready
- For guided implementation, confirm every added or meaningfully changed class, struct, function, and important property has detailed production-suitable comments covering purpose and relevant lifecycle, ownership, authority, side effects, and failure behavior
- Confirm comments still match the final code after every bug fix or simplicity rewrite and do not merely narrate syntax
- Confirm source text was not modified through wrongly decoded shell output
- Confirm comments and diagnostics match current-project conventions and do not expose sensitive data
- Confirm no unrelated files or stable release flows were changed
- For any worktree, plugin metadata, or config write, state exactly what changed and what was intentionally not done
- State whether UE build, editor validation, automation tests, or packaging were run or skipped
