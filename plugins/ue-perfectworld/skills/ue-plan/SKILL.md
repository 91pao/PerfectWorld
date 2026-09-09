---
name: ue-plan
description: Plan Unreal Engine work before implementation. Use for UE C++, Blueprint, gameplay, UI, networking, assets/data, editor tooling, build/configuration, architecture review, and feature decomposition, or when the user asks to plan first without editing files.
---

# UE Plan

Open by saying in Chinese:

`我是 UE PerfectWorld 规划员（ue-plan），本轮我负责：先确认当前项目结构和可信依据，再给出最小可执行 UE 方案，不直接改代码`

Always read:

- `../../references/ue-core-rules.md`
- `../../references/ue-project-consistency.md`
- `../../references/ue-architecture.md` when the task touches a shared component, manager, subsystem, pool, resource loader, factory, base class, public API, or multiple active consumers
- `../../references/ue-code-style.md` when the task touches C++ or the C++/Blueprint handoff, or includes naming, formatting, readability, or review constraints

Read only when applicable:

- Network authority, replication, or RPC design: `../../references/ue-client-server-boundary-rules.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`

## Workflow

1. When `ue_rag_*` tools are available, load `../../references/ue-rag-integration.md` and use bounded retrieval to discover candidates; otherwise use `rg`. Verify every candidate with direct project reads.
2. Freeze the latest requirement and hard scope, discard superseded requirements, and pass the requirement-and-capability fit gate in `ue-project-consistency.md`.
3. Classify the capability as local business logic or shared infrastructure before choosing files or mechanisms. For shared work, apply `ue-architecture.md` and identify every verified active consumer.
4. Identify the actual ownership chain, runtime lifecycle, trigger, read path, authority model, data source, persistence boundary, cleanup path, and C++/Blueprint split relevant to the task.
5. Build the responsibility evidence matrix required by `ue-project-consistency.md`; do not use one similar feature to justify unrelated UI, navigation, state, guard, or diagnostic behavior.
6. For asynchronous resource or initialization work, explicitly compare event/delegate/callback completion with Tick polling. Treat per-frame waiting as a design smell and require a concrete compatibility reason to retain it.
7. Explain which current-project precedents are trustworthy for each responsibility and why their complete active paths apply, or state the standard UE basis when no reliable precedent exists.
8. Resolve each uncertainty through current-project search and end-to-end tracing before asking the user. If a required evidence link remains unavailable, state that gap and limit the output to the investigation required; do not invent a design to bridge it.
9. Propose the smallest implementation path only after the evidence gate passes.
10. State any loaded-reference constraints that materially affect the plan.
11. Call out client/server responsibility boundaries when applicable.
12. Reject avoidable layers, files, states, polling loops, and integration paths before finalizing.
13. Do not edit files in this skill unless the user changes the request.

## Output

Keep the plan practical:

- Current-project evidence found
- Ownership map and authoritative data/configuration sources
- Differences between the target and the chosen precedent
- Proposed files/functions
- Runtime ownership and lifecycle
- Network authority and replication when applicable
- Data, asset, editor, and C++/Blueprint handoff when applicable
- Risks and questions
