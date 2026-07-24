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

## Requirement And Capability Fit Gate

Pass this gate before proposing implementation or adding a compensating mechanism.

- Freeze a current requirement baseline from the user's latest decisions, including hard file, module, asset, authority, and behavior boundaries; explicitly discard superseded requirements
- Map each required behavior to the highest-level verified project mechanism that already owns the responsibility
- If the requirements and allowed scope cannot both be satisfied, stop before adding mirrored state, caches, polling, timers, retries, delegates, duplicate configuration, wrapper APIs, or shared-framework changes
- Report the exact conflict, the unavoidable scope of a strict implementation, and the closest project-native alternative; do not change the requirement or expand scope without the user's decision
- Reopen this gate whenever the design adds a file, shared integration point, state owner, persistence path, RPC, cache, delegate, timer, manager, or second source of configuration that was not justified by the baseline
- After a requirement changes, remove or reject every mechanism that exists only for the superseded behavior before continuing

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

## State Identity And Presentation

- For state shown in more than one UI or system surface, identify three responsibilities separately: the producer and persistence owner, the acknowledgement or consumption owner, and display-only consumers
- When two surfaces must show the same state, first resolve and reuse the same authoritative identity, such as the same tag, message ID, activity instance, replicated field, or model object; do not introduce proxy state, forwarding events, mirrored saves, or synchronization code unless the requirement proves that the states are intentionally different
- Treat a different visual form, such as `NEW`, a badge, a count, or another brush, as presentation unless the project proves it represents a distinct business state
- A display-only consumer must not acknowledge, remove, reset, persist, or recreate source state unless the verified project contract assigns that responsibility to it

## Execution Stages And Change Surface

- Map multi-system behavior by execution stage before judging mechanisms as duplicate: entry, configuration lookup, route selection, target resolution, object or widget creation, presentation, acknowledgement, persistence, and cleanup when applicable
- Keep verified mechanisms that own different stages; remove only parallel mechanisms that perform the same responsibility or bypass an established stage
- Before implementation, maintain a compact change-surface manifest listing every file, asset, table row, tag, registration point, and Blueprint binding as create, replace, configure, or reuse-only, with the responsibility that requires it
- Separate pre-existing dependencies from requested modifications. A shared factory, subsystem, helper, table, or base class that already satisfies the requirement is reuse-only and must not be presented as a new change
- Any shared-framework modification or new state owner not already justified by the frozen baseline must reopen the requirement-and-capability fit gate before code is produced
- When binary assets or editor-only values cannot be inspected reliably, prefer copying the closest verified production row or asset and changing only proven fields; do not invent hidden slot, platform, extra-data, or registration values

## Ownership Map

For non-trivial or cross-system work, identify:

- Entry point or factory
- Runtime owner and lifecycle
- Authoritative data and configuration source
- Client/server boundary when applicable
- Persistence owner
- C++ and Blueprint responsibilities
- Registration and cleanup path
- State producer, acknowledgement owner, and display-only consumers when user-visible state is involved
- Execution stage for each participating table, asset, subsystem, manager, factory, router, and widget

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
