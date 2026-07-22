# UE Final Self Review

Run this as a blocking gate before delivering code, direct edits, or a code-review conclusion.

## Correctness

- Trace the primary success path and important failure paths end to end
- Recheck every project-specific symbol and assumption against the current workspace
- Confirm selected precedents have active production evidence and compatible ownership, lifecycle, authority, and responsibility
- Recheck reflection declarations, includes, module dependencies, object lifetime, null handling, delegate cleanup, threading, assets, configuration, persistence, and network rules where applicable
- Confirm bug fixes correct the root cause instead of hiding it with fallback state, retries, delays, or silent returns
- Distinguish proven guarantees from mitigations and unresolved assumptions

## Maintainability

- Compare the result with the smallest complete project-consistent implementation
- Require every added file, class, function, field, delegate, override, configuration item, and abstraction to have a current requirement and real consumer
- Remove duplicate data authority, unused state, empty lifecycle overrides, speculative extension points, one-use wrappers, generic managers, compatibility branches, and parallel execution paths
- Keep one authoritative source for each tag, ID, state, and configuration value
- Apply the change test: a normal requirement change has an obvious bounded edit location
- Apply the deletion test: the feature can be removed without hidden registration, duplicate state, or undocumented coupling
- Apply the no-chat test: a teammate can trace, modify, and remove the implementation without the generation conversation
- Rewrite avoidable overdesign before delivery; do not merely document it as a concern

## Delivery

- Correct every known in-scope defect before presenting complete code or finalizing direct edits
- Ensure complete-code responses contain no pseudocode, ellipses, placeholders, TODOs, omitted branches, or unverified project symbols
- Keep comments concise, production-suitable, and synchronized with the final implementation
- Confirm source text was not modified through incorrectly decoded shell output
- Confirm no unrelated files or stable release flows changed
- State which compile, editor, automation, and packaging checks were run or skipped
- If repeated local fixes accumulated, apply the recovery gate in `ue-bugfix-discipline.md` before finalizing
