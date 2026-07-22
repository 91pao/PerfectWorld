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
2. Identify the actual ownership chain, lifecycle, authority model, data source, persistence boundary, and C++/Blueprint split relevant to the task.
3. Explain which current-project precedent is trustworthy and why it applies, or state the standard UE basis when no reliable precedent exists.
4. Propose the smallest implementation path.
5. State any loaded-reference constraints that materially affect the plan.
6. Call out client/server responsibility boundaries when applicable.
7. Reject avoidable layers, files, states, and integration paths before finalizing.
8. Do not edit files in this skill unless the user changes the request.

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
