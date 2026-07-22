# UE Project Evidence And Consistency

Use this reference before proposing project-specific architecture, complete code, direct edits, or review conclusions.

## Evidence Discovery

- Start with the same feature domain, module, base class, lifecycle phase, authority side, and responsibility
- Trace active callers, registration, base classes, data and configuration, relevant assets, runtime ownership, persistence, and cleanup instead of copying one nearby file
- When the user names a reference feature, verify its complete active integration path across C++, Blueprint, DataTables, DataAssets, subsystems, managers, and editor registration where applicable
- Prefer maintained production code with compatible ownership and lifecycle; reject generated, deprecated, experimental, disabled, duplicated, temporary, or dead candidates unless independent evidence proves they are authoritative
- When candidates disagree, explain the evidence and follow the closest trustworthy production path
- If essential evidence is unavailable, report the exact gap instead of inventing project symbols or claiming the implementation is complete

## Ownership Map

For non-trivial or cross-system work, identify:

- Entry point or factory
- Runtime owner and lifecycle
- Authoritative data and configuration source
- Client/server boundary when applicable
- Persistence owner
- C++ and Blueprint responsibilities
- Registration and cleanup path

## Design Constraints

- Preserve verified naming, module boundaries, reflection usage, ownership, lifecycle, diagnostics, and data-access conventions
- Keep one authoritative source for every important tag, ID, state, and configuration value
- Do not add a second DataAsset, member, Blueprint default, table field, manager, or cache for data already owned by an established project system
- Reuse an abstraction only when it is active, responsibility-compatible, and simpler than a local implementation
- Do not copy empty lifecycle overrides, known defects, legacy shortcuts, or unrelated patterns merely for visual consistency
- Do not add wrappers, managers, services, generic result types, delegates, or extension points without a current requirement and verified consumer
- Keep the execution path easy to trace, change, and remove without access to the AI conversation
- Use standard Unreal Engine conventions as the fallback when project evidence is missing or unreliable, and state that fallback explicitly
