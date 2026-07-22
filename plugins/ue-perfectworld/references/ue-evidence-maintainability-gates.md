# UE Evidence And Maintainability Gates

Use these gates for non-trivial UE features, cross-system integration, architecture work, and any implementation presented as complete or transcription-ready.

## Evidence Gate

- Do not design from a class name or one nearby file. Trace the production path across callers, registration, data/configuration, assets, runtime ownership, lifecycle, authority, persistence, and UI or Blueprint consumption where applicable.
- When the user names a reference class or feature, inspect its relevant C++ call sites, base classes, DataTables, DataAssets, Blueprint assets, subsystem or manager integration, and active registration before treating it as precedent.
- Identify the authoritative source for every important identifier and state. Do not duplicate a tag, ID, state, or configuration in a feature DataAsset or member when the project already owns it elsewhere.
- Record an ownership map before implementation: entry or factory, runtime owner, authoritative data source, lifecycle, server/client boundary, persistence owner, C++ responsibility, Blueprint responsibility, and cleanup path.
- Confirm that each precedent is active production code with compatible responsibility. Do not copy empty overrides, known defects, legacy shortcuts, or unrelated patterns merely for consistency.
- If essential evidence is missing, continue investigation or report the missing evidence. Do not fill gaps with plausible-looking code or call the result complete.

## Collaboration Gate

- For a non-trivial cross-system feature in guided implementation, first present the verified evidence, ownership map, differences from the precedent, and smallest proposed design.
- Wait for the user's confirmation before providing the full transcription-ready implementation unless the user explicitly asks to skip the design checkpoint after seeing those findings.
- When new evidence contradicts the current design, discard or revise the design at its source. Do not preserve it by adding wrappers, compatibility branches, or more state.

## Maintainability Gate

- Optimize for a teammate maintaining the code without access to the AI conversation. Project structure, names, comments, and normal call tracing must explain the implementation.
- Every new class, function, field, delegate, override, configuration entry, and abstraction must have a current requirement and a verified caller or consumer.
- Prefer one authoritative data source and one clear execution path. Reject duplicate configuration, shadow state, and parallel implementations of an existing framework service.
- Do not add empty lifecycle overrides, speculative extension points, one-use wrappers, or generic managers that do not remove present complexity.
- Use comments to explain ownership, lifecycle, authority, side effects, and non-obvious reasons. Do not rely on comments to rescue an unnecessarily indirect design.
- Apply the change test: a normal requirement change should have an obvious, bounded edit location.
- Apply the deletion test: a teammate should be able to remove the feature without discovering hidden registrations, duplicate state, or undocumented coupling.
- Apply the no-chat test: if the code only makes sense with the generation conversation, rewrite it before delivery.

## Recovery Gate

- Treat repeated compile, link, reflection, asset, or configuration failures as a possible architecture or integration error, not only a sequence of local syntax problems.
- After multiple related failures or repeated patching of the same feature, stop adding fixes and retrace ownership, data flow, lifecycle, registration, and project precedent end to end.
- Do not call a solution complete until both the runtime path and required editor/data setup have been verified or explicitly identified as unverified.
