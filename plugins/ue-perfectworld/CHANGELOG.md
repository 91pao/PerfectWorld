# Changelog

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
