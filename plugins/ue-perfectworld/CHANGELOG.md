# Changelog

## 0.1.8

- Added an explicit state-ownership split between producer and persistence owner, acknowledgement owner, and display-only consumers.
- Required multiple surfaces that represent the same state to reuse the same authoritative identity instead of introducing proxy state, forwarding events, mirrored saves, or synchronization code.
- Classified visual variants such as `NEW`, badges, counts, and alternate brushes as presentation unless a verified business rule proves they are distinct state.
- Added execution-stage mapping for entry, configuration, routing, target resolution, creation, presentation, acknowledgement, persistence, and cleanup so different pipeline stages are not mistaken for duplicate systems.
- Added a blocking change-surface manifest that separates create, replace, configure, and reuse-only targets and reopens the fit gate for undeclared shared-framework changes.
- Extended final review across C++, factories, DataAssets, DataTables, GameplayTags, Blueprint bindings, UI extension and platform overrides, external payloads, persistence, and cleanup.
- Required copied editor rows and assets to preserve verified hidden fields while replacing all platform-specific references that still point to the source feature.

## 0.1.7

- Added a blocking requirement-and-capability fit gate before implementation, compensation, or scope expansion.
- Required workflows to freeze the user's latest requirements and hard boundaries and to discard mechanisms that belong only to superseded requirements.
- Required each behavior to map to the highest-level verified project mechanism that already owns the responsibility.
- When requirements conflict with the allowed scope, required the exact conflict, unavoidable strict implementation cost, and closest project-native alternative to be presented for the user's decision instead of inventing local compensation.
- Required the fit gate to reopen when complexity grows through another file, shared integration point, state owner, persistence path, RPC, cache, delegate, timer, manager, or configuration source.
- Extended final review to reject obsolete behavior, hidden scope expansion, and unnecessary mechanisms accumulated across requirement changes.

## 0.1.6

- Added a responsibility evidence matrix so one similar feature can no longer justify unrelated UI composition, navigation, state, lifecycle, guard, or diagnostic choices.
- Required project-specific object acquisition, null guards, optional-widget handling, callback validation, and logging behavior to be verified against maintained code with the same responsibility and lifecycle.
- Prohibited universal "every return must log" and "all failures stay silent" policies; failures must be classified and handled through the project's established path.
- Required new traversals, direct manager calls, wrapper bypasses, lookup paths, and logging strategies to reopen project investigation before implementation.
- Added blocking self-review checks for repeated boundary logs, invented HUD or player access patterns, inconsistent optional-widget handling, and design changes motivated only by reducing logs or line count.
- Applied the new gate to planning, investigation, Blueprint collaboration, read-only complete implementation, direct implementation, and review workflows without adding duplicate rule files.

## 0.1.5

- Added a mandatory evidence gate for non-trivial cross-system UE designs before complete code, editor configuration, direct edits, or framework extensions.
- Required separate proof for the authoritative data/configuration source, runtime owner and lifecycle, trigger, read or acknowledgement path, persistence, and cleanup or expiry path.
- Prohibited treating adjacent responsibilities as proof of one another: parent-child aggregation does not prove message creation, a UI display path does not prove server persistence, and a trigger does not prove cleanup.
- Required agents to decompose every unresolved implementation question into answerable subquestions, exhaust current-project search and end-to-end tracing for each one, then ask the user only for an external artifact or a genuine business decision that the project cannot answer.
- Required an explicit evidence gap report when any required link is unavailable; agents must not fill the gap by inventing conditions, managers, DataAssets, fields, delegates, or lifecycle hooks.
- Applied the gate to planning, investigation, Blueprint collaboration, read-only complete implementation, direct implementation, review, final self-review, and recovery after repeated failed fixes.

## 0.1.4

- Added an evidence gate for non-trivial Unreal Engine work.
- Required an ownership map covering entry, runtime owner, authoritative data, lifecycle, authority, persistence, C++/Blueprint handoff, and cleanup before complete implementation.
- Added a collaboration checkpoint for cross-system complete implementation: evidence and the smallest design come before transcription-ready code.
- Added maintainability checks for one source of truth, current callers, empty lifecycle overrides, speculative abstractions, the change test, the deletion test, and the no-chat test.
- Added recovery rules to retrace architecture after repeated compile, link, reflection, asset, or configuration failures instead of stacking local patches.
- Applied the new gates to planning, drafting, implementation, investigation, review, and Blueprint workflows.
- Consolidated evidence, ownership, maintainability, and recovery rules into single authoritative references and removed duplicate rule files.
- Changed workflow references to a core-plus-conditional model so network, transaction, UI-contract, logging, and bug-fix rules load only when relevant.
- Made the router selection-only so it no longer preloads references that the selected workflow reads again.
- Replaced informal training-oriented wording with professional complete-implementation terminology while preserving ordered code, editor actions, and verification steps.
