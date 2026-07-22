# UE Complete Implementation

Use this workflow when the user wants to enter Unreal Engine changes manually and has not explicitly authorized Codex to edit project files.

## Workspace Boundary

- Keep the workspace read-only
- Do not create, modify, rename, move, or delete project files
- The user performs the shown edits; provide every required action and exact value in the conversation

## Design Checkpoint

- Apply `ue-project-consistency.md` before writing project-specific code
- For non-trivial cross-system work, first present verified evidence, the ownership map, differences from the selected precedent, and the smallest proposed design
- Wait for the user's confirmation before providing complete code unless the user explicitly skips the checkpoint after reviewing those findings
- When new evidence contradicts the proposal, revise the design at its source instead of adding wrappers, compatibility branches, or duplicate state

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
- End with compile and runtime checks in execution order, including expected behavior and important failure cases
- State that Codex did not compile the code unless the user explicitly requested and authorized a build
