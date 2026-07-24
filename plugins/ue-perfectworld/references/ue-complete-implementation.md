# UE Complete Implementation

Use this workflow when the user wants to enter Unreal Engine changes manually and has not explicitly authorized Codex to edit project files.

## Workspace Boundary

- Keep the workspace read-only
- Do not create, modify, rename, move, or delete project files
- The user performs the shown edits; provide every required action and exact value in the conversation

## Design Checkpoint

- Apply `ue-project-consistency.md` before writing project-specific code
- For non-trivial cross-system work, pass the mandatory evidence gate before writing code: show the verified data source, runtime lifecycle, trigger, read path, persistence boundary, cleanup path, and differences from the selected precedent
- Include responsibility-level evidence for every introduced mechanism, not only one high-level reference feature. UI composition, child interaction, navigation, state or red-point binding, object acquisition, guard behavior, and diagnostics require their own compatible precedents when applicable
- If a required link is not proven, report the gap and do not provide transcription-ready code, DataTable rows, Blueprint steps, or new extension points
- Wait for the user's confirmation before providing complete code unless the user explicitly skips the checkpoint after reviewing those findings
- When new evidence contradicts the proposal, revise the design at its source instead of adding wrappers, compatibility branches, or duplicate state
- Before code, present a compact evidence ledger whose rows map each required behavior to its authoritative owner, active project symbol or asset, lifecycle or authority side, and verified, disproven, or unavailable status
- Before code, present a compact change-surface manifest that separates create, replace, configure, and reuse-only targets. Flag every shared integration point and prove why a modification is unavoidable
- When multiple surfaces must show the same state, show the resolved authoritative identity and verify that display-only consumers do not create, persist, forward, acknowledge, or remove it
- When several project systems participate in one action, show the execution-stage chain so routing, target resolution, widget creation, presentation, acknowledgement, and persistence are not mistaken for duplicate implementations

## Implementation Sequence

Present changes in real dependency order. For every step:

1. Name the exact target file or editor asset
2. State whether to create, insert, replace, configure, or bind
3. Identify the exact location using verified project symbols
4. Explain briefly why the step is required
5. Provide complete code or exact editor/configuration values
6. State the condition that should hold before continuing

Typical ordering is module/configuration requirements, declarations, definitions, call-site integration, Blueprint/editor setup, data setup, and validation. Adapt it to the verified project path.

## Completeness Contract

- Provide complete declarations and function bodies for every added or changed symbol
- Show a complete replacement function unless a smaller insertion has an unambiguous exact anchor
- Show complete contents for every new source file
- Include required headers, forward declarations, reflection macros, module dependencies, access specifiers, overrides, registration, and binding code
- Use exact current-project names and style
- Apply `ue-comment-log-rules.md` to code comments and diagnostics
- Do not use pseudocode, ellipses, omitted branches, TODOs, placeholder identifiers, or incomplete code blocks
- Do not claim the result is ready to enter while a required symbol, asset, value, or integration decision remains unresolved

## Editor And Validation

- Give Blueprint and editor actions in click order with exact asset, panel, property, event, pin, row, tag, and value names verified from the project
- State required compile, restart, refresh, reparent, rebind, or resave steps only when they are actually necessary
- Verify copied DataTable or asset rows across all platform-specific templates, overrides, slots, extra data, registration fields, and fallback behavior; do not leave references to the source feature in another platform branch
- Cross-check every code field and lookup key against the final DataAsset, DataTable, GameplayTag, Blueprint property, factory registration, and external configuration that supplies it
- End with compile and runtime checks in execution order, including expected behavior and important failure cases
- State that Codex did not compile the code unless the user explicitly requested and authorized a build
