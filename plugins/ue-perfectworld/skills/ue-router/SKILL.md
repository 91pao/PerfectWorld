---
name: ue-router
description: Route Unreal Engine tasks across planning, read-only change specification, direct implementation, investigation, review, and Blueprint workflows. Use for UE C++, Blueprint, gameplay, UI, networking, assets/data, editor, build, configuration, and architecture work.
---

# UE Router

Open by saying in Chinese:

`我是 UE PerfectWorld 调度员（ue-router），本轮我负责：判断这个 UE 任务该走规划、实现、排查、审查还是蓝图协作流程`

Use this router only to choose the workflow. Do not load workflow references here; follow only the selected skill's reference rules.

## Routing

- Planning or architecture before coding: use `ue-plan`
- Shared/public infrastructure, pooled components, resource loading, async readiness, managers, factories, or a capability used by multiple systems: use `ue-plan` first, even when the user also asks for implementation; after the architecture gate, continue to `ue-implement` only if direct edits are explicitly authorized.
- Bug, compile error, runtime error, odd behavior, or root cause analysis: use `ue-investigate`
- Read-only complete implementation, "不要改文件", "我自己写", "把完整代码给我", or ambiguous code-writing requests: use `ue-draft`
- Direct feature/code change request with a hard direct-edit requirement to modify files or write into the project/worktree: use `ue-implement`
- "review", "看看有没有问题", AI-code smell, PR/diff/current code check: use `ue-review`
- Blueprint/editor integration, asset setup, widget binding, exposed API usage, or visual scripting: use `ue-blueprint`

Architecture routing rule:

- Do not treat the first named caller as the owner when the request mentions a common, public, generic, pooled, or reusable capability.
- For asynchronous resource or initialization work, route through the architecture check before accepting Tick polling. Tick should be reserved for continuous progression, tracking, simulation, or parameter updates.

If the user's wording is ambiguous about file edits, route to `ue-draft` or `ue-investigate` and keep the workspace read-only.
