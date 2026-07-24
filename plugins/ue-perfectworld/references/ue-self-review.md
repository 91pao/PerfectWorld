# UE Final Self Review

Run this as a blocking gate before delivering code, direct edits, or a code-review conclusion.

## Correctness

- Trace the primary success path and important failure paths end to end
- Confirm the result implements the user's latest requirement and hard scope, and contains no mechanism retained only for a superseded requirement
- Confirm each required behavior maps to a verified project capability; when requirement and allowed scope conflict, require the exact conflict, strict implementation cost, and closest project-native alternative before implementation
- Recheck every project-specific symbol and assumption against the current workspace
- Recheck every introduced mechanism against the responsibility evidence matrix; one similar feature is insufficient when UI composition, navigation, state, diagnostics, or lifecycle use different project owners
- For non-trivial cross-system work, verify the evidence gate is complete: authoritative data, runtime lifecycle, trigger, read path, persistence boundary, and cleanup path all have project evidence
- Reject any solution that infers one responsibility from another, such as deriving message creation from display aggregation or deriving cleanup from a trigger condition
- Confirm selected precedents have active production evidence and compatible ownership, lifecycle, authority, and responsibility
- Recheck reflection declarations, includes, module dependencies, object lifetime, null handling, delegate cleanup, threading, assets, configuration, persistence, and network rules where applicable
- Audit each new guard and diagnostic against the closest maintained same-responsibility path. Remove invented logging policies, repeated boundary logs, and inconsistent HUD, player, optional-widget, or callback handling
- Confirm bug fixes correct the root cause instead of hiding it with fallback state, retries, delays, or silent returns
- Distinguish proven guarantees from mitigations and unresolved assumptions
- For shared user-visible state, confirm the producer and persistence owner, acknowledgement owner, and display-only consumers are distinct and correct
- If two surfaces are required to stay identical, confirm they resolve the same authoritative identity instead of maintaining synchronized copies or proxy state
- Trace each participating mechanism by execution stage and reject both missing stages and parallel paths that perform the same responsibility
- Cross-check code, factory registration, DataAssets, DataTables, GameplayTags, Blueprint bindings, UI extension or platform overrides, external payloads, persistence, and cleanup as one final contract

## Maintainability

- Compare the result with the smallest complete project-consistent implementation
- Reopen the requirement-and-capability fit gate if complexity grew through another file, shared integration point, state owner, persistence path, RPC, cache, delegate, timer, manager, or configuration source
- Require every added file, class, function, field, delegate, override, configuration item, and abstraction to have a current requirement and real consumer
- Remove duplicate data authority, unused state, empty lifecycle overrides, speculative extension points, one-use wrappers, generic managers, compatibility branches, and parallel execution paths
- Keep one authoritative source for each tag, ID, state, and configuration value
- Apply the change test: a normal requirement change has an obvious bounded edit location
- Apply the deletion test: the feature can be removed without hidden registration, duplicate state, or undocumented coupling
- Apply the no-chat test: a teammate can trace, modify, and remove the implementation without the generation conversation
- Rewrite avoidable overdesign before delivery; do not merely document it as a concern
- Compare the delivered file and asset list with the change-surface manifest; reject undeclared shared changes, stale fields from earlier designs, duplicated configuration, and dependencies incorrectly described as modifications
- Treat a visual variant as presentation unless a verified business rule requires a separate persisted or acknowledged state

## Delivery

- Correct every known in-scope defect before presenting complete code or finalizing direct edits
- If the evidence gate has a gap, remove any speculative implementation from the response and state the missing proof instead
- Ensure complete-code responses contain no pseudocode, ellipses, placeholders, TODOs, omitted branches, or unverified project symbols
- Keep comments concise, production-suitable, and synchronized with the final implementation
- Confirm source text was not modified through incorrectly decoded shell output
- Confirm no unrelated files or stable release flows changed
- State which compile, editor, automation, and packaging checks were run or skipped
- If repeated local fixes accumulated, apply the recovery gate in `ue-bugfix-discipline.md` before finalizing
- Include the final create, replace, configure, and reuse-only surface summary so the user can distinguish required work from existing project infrastructure
