---
name: ue-router
description: Route Unreal Engine tasks across planning, read-only complete implementation, direct implementation, investigation, review, and Blueprint/editor workflows. Use for UE C++, Blueprint, gameplay, UI, networking, assets/data, editor, build, configuration, and architecture work.
---

# UE Router

Open by saying in Chinese:

`我是 UE PerfectWorld 调度员（ue-router），本轮我负责：判断这个 UE 任务该走规划、实现、排查、审查还是蓝图协作流程`

Use this router only to choose the workflow. Do not load workflow references here; follow only the selected skill's reference rules.

## Routing

- Planning or architecture before coding: use `ue-plan`
- Bug, compile error, runtime error, odd behavior, or root cause analysis: use `ue-investigate`
- Read-only complete implementation, "不要改文件", "我自己写", "把完整代码给我", or ambiguous code-writing requests: use `ue-draft`
- Direct feature/code change request with a hard direct-edit requirement to modify files or write into the project/worktree: use `ue-implement`
- "review", "看看有没有问题", AI-code smell, PR/diff/current code check: use `ue-review`
- Blueprint/editor integration, asset setup, widget binding, exposed API usage, or visual scripting: use `ue-blueprint`

If the user's wording is ambiguous about file edits, route to `ue-draft` or `ue-investigate` and keep the workspace read-only.
