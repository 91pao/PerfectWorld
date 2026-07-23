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

Read only when applicable:

- Network authority, replication, or RPC design: `../../references/ue-client-server-boundary-rules.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`

## Workflow

1. Use `rg` to discover candidate same-domain code, assets, configuration, and call sites.
2. Identify the actual ownership chain, runtime lifecycle, trigger, read path, authority model, data source, persistence boundary, cleanup path, and C++/Blueprint split relevant to the task.
3. Build the responsibility evidence matrix required by `ue-project-consistency.md`; do not use one similar feature to justify unrelated UI, navigation, state, guard, or diagnostic behavior.
4. Explain which current-project precedents are trustworthy for each responsibility and why their complete active paths apply, or state the standard UE basis when no reliable precedent exists.
5. Resolve each uncertainty through current-project search and end-to-end tracing before asking the user. If a required evidence link remains unavailable, state that gap and limit the output to the investigation required; do not invent a design to bridge it.
6. Propose the smallest implementation path only after the evidence gate passes.
7. State any loaded-reference constraints that materially affect the plan.
8. Call out client/server responsibility boundaries when applicable.
9. Reject avoidable layers, files, states, and integration paths before finalizing.
10. Do not edit files in this skill unless the user changes the request.

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
