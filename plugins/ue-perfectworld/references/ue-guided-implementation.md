# UE Guided Implementation

Use this as the default workflow when the user wants to implement Unreal Engine changes manually and has not explicitly authorized Codex to edit project files.

## Non-Mutation Rule

- Keep the workspace read-only
- Do not create, modify, rename, move, or delete project files
- Do not call `apply_patch` or run tools that rewrite project files
- The user may manually create or edit files when the feature requires it; provide every required action and exact code in the conversation

## Evidence Before Code

- Read the actual target declarations, implementations, module dependencies, call sites, relevant assets or configuration, and UE version evidence available in the project
- Resolve exact type names, signatures, includes, macros, ownership, lifecycle, authority, and existing APIs before presenting code as transcription-ready
- Do not invent project symbols or silently assume a generic template matches the project
- If essential evidence is unavailable, continue read-only investigation; if it still cannot be found, state exactly what is missing instead of fabricating complete-looking code
- For non-trivial cross-system work, present the verified evidence, ownership map, precedent differences, and smallest design first; wait for user confirmation before the transcription-ready code unless the user explicitly skips that checkpoint after reviewing the findings
- Apply `ue-evidence-maintainability-gates.md` before claiming the implementation is complete

## Teaching Format

Present the implementation in the order the user should perform it. For each step:

1. Name the exact target file or editor asset
2. State whether to create, insert, replace, configure, or bind
3. Identify the exact insertion or replacement location using symbols that exist in the project
4. Briefly explain why this step is required
5. Provide the complete code or exact editor/configuration values for that step
6. State what should be true before moving to the next step

Order steps by real dependency, typically module/configuration requirements, declarations, definitions, call-site integration, Blueprint/editor setup, data setup, and validation. Adapt the order to the current project rather than forcing this example sequence.

## Code Completeness

- Provide complete declarations and complete function bodies for every changed or added symbol
- For a modified function, show the entire replacement function unless a smaller insertion has an unambiguous exact anchor
- For a new source file, show its complete contents
- Include required headers, forward declarations, reflection macros, module dependencies, access specifiers, overrides, and registration or binding code
- Use exact current-project names and style
- Include comprehensive, concise, production-suitable teaching comments according to `ue-comment-log-rules.md`; the user may choose whether to enter those comments
- Do not output pseudocode, ellipses, omitted branches, TODOs, placeholder identifiers, "fill this in", or non-compiling pattern sketches inside code blocks
- Do not claim code is transcription-ready while any required type, symbol, file, asset, value, or integration decision remains unresolved
- Keep broader tutorial prose outside code blocks, but include required code comments inside the blocks so they can be entered literally

## Teaching Comment Coverage

- Add a concise purpose comment for every added or meaningfully changed class, struct, function, and important property
- Default to one-line `//` comments placed immediately above the code they govern
- Explain relevant UE lifecycle timing, object ownership, authority, replication, delegate lifetime, side effects, and failure behavior wherever each matters
- Comment critical branches and non-obvious engine calls with a short explanation of why they are required
- Expand to consecutive `//` lines only when one line cannot explain the required behavior accurately
- Keep coverage comprehensive without narrating trivial syntax or repeating clear names and signatures
- After any correctness or simplicity rewrite, update the comments to match the final code

## Blueprint And Editor Steps

- Give editor actions in click order with exact asset, panel, property, event, pin, row, tag, or value names discovered from the project
- Separate visual/editor instructions from C++ code
- Explain compile, editor restart, Blueprint refresh, reparenting, rebinding, or asset resave steps when actually required

## Final Validation

- End with a checklist in the same order the user should compile and verify the feature
- Include expected behavior and important failure cases
- State that the code was not compiled by Codex unless the user explicitly requested and authorized a build
