# UE Project Evidence And Consistency

Use this reference before proposing project-specific architecture, complete code, direct edits, or review conclusions.

## Evidence Discovery

- Start with the same feature domain, module, base class, lifecycle phase, authority side, and responsibility
- Split the requested behavior into responsibility-level questions before selecting a precedent. Check entry and ownership, data access, lifecycle, UI composition, interaction, navigation, state or red-point behavior, diagnostics, and cleanup separately when applicable
- Trace active callers, registration, base classes, data and configuration, relevant assets, runtime ownership, persistence, and cleanup instead of copying one nearby file
- When the user names a reference feature, verify its complete active integration path across C++, Blueprint, DataTables, DataAssets, subsystems, managers, and editor registration where applicable
- Prefer maintained production code with compatible ownership and lifecycle; reject generated, deprecated, experimental, disabled, duplicated, temporary, or dead candidates unless independent evidence proves they are authoritative
- When candidates disagree, explain the evidence and follow the closest trustworthy production path
- If essential evidence is unavailable, report the exact gap instead of inventing project symbols or claiming the implementation is complete

## Mandatory Evidence Gate

Before proposing a project-specific design, complete code, editor configuration, direct edit, or new framework extension for non-trivial cross-system work, prove each applicable link from current-project evidence:

- Authoritative data and configuration source
- Runtime owner and lifecycle, including activation and removal
- Trigger and condition that creates, refreshes, or removes the state
- Read, acknowledgement, consumption, or state-transition path
- Persistence owner and client/server synchronization boundary when applicable
- Cleanup, expiry, reset, and deregistration path

- Trace each link from producer to consumer. A nearby class, a matching name, or a single method is not sufficient evidence.
- Keep adjacent responsibilities separate. Display or parent-child aggregation does not prove message creation; a UI click path does not prove server persistence; a true condition does not prove removal or expiry.
- Select a project precedent only after verifying its complete active path has compatible ownership, lifecycle, authority, and cleanup behavior.
- If any required link is unverified, report the exact evidence gap and stop at a diagnosis or bounded investigation plan. Do not output complete implementation steps or add conditions, managers, DataAssets, fields, delegates, tags, or lifecycle hooks to bridge the gap.

## Evidence Resolution

- Treat every uncertainty as a list of answerable subquestions. Search the current project for each subquestion and trace its active path end to end before deciding that it is unknown.
- Keep a compact evidence matrix while investigating: for each responsibility, record the exact production symbols, why their ownership and lifecycle match, material differences from the target, and whether the question is verified, disproven, or unavailable.
- Do not let evidence for one responsibility authorize another. A red-point precedent does not prove widget discovery, a navigation precedent does not prove data ownership, and a lifecycle precedent does not prove null-handling or logging style.
- Reopen project search whenever the proposed design introduces a mechanism not covered by the matrix, including a new object lookup, tree traversal, direct manager call, wrapper bypass, guard policy, or diagnostic path.
- Query the project before asking the user when code, configuration, assets, logs, call sites, lifecycle hooks, or a compatible feature can answer the question. Do not ask the user to guess a project convention or choose between unverified designs.
- Record each subquestion as verified, disproven, or unavailable with the searched evidence. A partial match in a different feature does not resolve a different responsibility.
- When the project cannot answer, finish all unblocked investigation first. Ask one concise final question only for a required external artifact or a real product decision; otherwise state the exact missing proof and do not invent a substitute.
- Keep this procedure inside the existing evidence gate. Do not create parallel checklists, caches, or speculative scaffolding to compensate for missing evidence.

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
- Match object acquisition, null guards, optional-widget handling, callback validation, and logging behavior to the closest maintained code with the same responsibility and lifecycle; do not derive a universal policy from generic defensive-programming advice
- Do not use fewer logs, fewer lines, or local convenience as justification for a new traversal, lookup, navigation, state, or ownership path
- Keep one authoritative source for every important tag, ID, state, and configuration value
- Do not add a second DataAsset, member, Blueprint default, table field, manager, or cache for data already owned by an established project system
- Reuse an abstraction only when it is active, responsibility-compatible, and simpler than a local implementation
- Do not copy empty lifecycle overrides, known defects, legacy shortcuts, or unrelated patterns merely for visual consistency
- Do not add wrappers, managers, services, generic result types, delegates, or extension points without a current requirement and verified consumer
- Keep the execution path easy to trace, change, and remove without access to the AI conversation
- Use standard Unreal Engine conventions as the fallback when project evidence is missing or unreliable, and state that fallback explicitly
