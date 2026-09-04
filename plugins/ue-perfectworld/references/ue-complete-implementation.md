# UE Read-only Change Specification

Use this workflow when the user needs a verified Unreal Engine change specification and has not explicitly authorized Codex to edit project files.

## Workspace Boundary

- Keep the workspace read-only
- Do not create, modify, rename, move, or delete project files
- Report the required change surface, affected symbols, dependencies, and verification criteria without simulating a manual editing session

## Design Checkpoint

- Apply `ue-project-consistency.md` before writing project-specific code
- For non-trivial cross-system work, pass the mandatory evidence gate before writing code: show the verified data source, runtime lifecycle, trigger, read path, persistence boundary, cleanup path, and differences from the selected precedent
- Include responsibility-level evidence for every introduced mechanism, not only one high-level reference feature. UI composition, child interaction, navigation, state or red-point binding, object acquisition, guard behavior, and diagnostics require their own compatible precedents when applicable
- If a required link is not proven, report the gap and do not specify code, DataTable rows, Blueprint changes, or new extension points
- When new evidence contradicts the proposal, revise the design at its source instead of adding wrappers, compatibility branches, or duplicate state
- Before code, present a compact evidence ledger whose rows map each required behavior to its authoritative owner, active project symbol or asset, lifecycle or authority side, and verified, disproven, or unavailable status
- Before code, present a compact change-surface manifest that separates create, replace, configure, and reuse-only targets. Flag every shared integration point and prove why a modification is unavoidable
- When multiple surfaces must show the same state, show the resolved authoritative identity and verify that display-only consumers do not create, persist, forward, acknowledge, or remove it
- When several project systems participate in one action, show the execution-stage chain so routing, target resolution, widget creation, presentation, acknowledgement, and persistence are not mistaken for duplicate implementations

## Change Surface

For every proposed target, identify the verified file, symbol, asset, configuration record, or binding and classify it as create, replace, configure, or reuse-only. State the ownership, lifecycle, authority, and dependency constraints that make the target applicable.

## Validation

- State required compile, restart, refresh, reparent, rebind, or resave conditions only when they are actually necessary
- Verify copied DataTable or asset rows across all platform-specific templates, overrides, slots, extra data, registration fields, and fallback behavior; do not leave references to the source feature in another platform branch
- Cross-check every code field and lookup key against the final DataAsset, DataTable, GameplayTag, Blueprint property, factory registration, and external configuration that supplies it
- End with compile and runtime verification criteria, including expected behavior and important failure cases
- State that Codex did not compile the code unless the user explicitly requested and authorized a build
