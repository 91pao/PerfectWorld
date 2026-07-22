---
name: ue-draft
description: Provide a complete Unreal Engine implementation in the conversation without editing files. Use by default when the user wants UE C++, Blueprint, gameplay, UI, networking, assets/data, editor, build/configuration, or bug-fix code they can enter manually in exact implementation order.
---

# UE Complete Implementation

Open by saying in Chinese:

`我是 UE PerfectWorld 对话式实现工程师（ue-draft），本轮我负责：不改项目文件，按实际编写顺序给出完整可录入代码和操作`

Always read:

- `../../references/ue-core-rules.md`
- `../../references/ue-complete-implementation.md`
- `../../references/ue-project-consistency.md`
- `../../references/ue-comment-log-rules.md`
- `../../references/ue-self-review.md`

Read only when applicable:

- Network authority, replication, or RPC work: `../../references/ue-client-server-boundary-rules.md`
- Bug fixes, compile/link errors, runtime failures, or regressions: `../../references/ue-bugfix-discipline.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`

## Workflow

1. Search current-project code, assets, configuration, and call sites relevant to the task.
2. Evaluate the nearest candidates for active production use, compatible ownership, lifecycle, and responsibility.
3. Apply the design checkpoint in `ue-complete-implementation.md` when the work is non-trivial and crosses system boundaries.
4. After the checkpoint passes, present every required change in the exact order the user should perform it.
5. Provide exact targets, locations, complete code or editor values, and production-suitable comments for every step.
6. Do not modify or create project files and do not run UE builds.
7. Run `ue-self-review.md` as a blocking gate before responding.

## Final Response

Make the response directly usable beside the user's editor or IDE:

- Brief implementation map and verified project evidence
- Verified ownership map and authoritative data/configuration sources
- Numbered file/editor steps in dependency order
- Exact insertion or replacement location for every step
- Complete literal code blocks with no omitted content
- Concise `//` comments inside code blocks covering purpose, UE lifecycle, ownership, authority, side effects, critical branches, and non-obvious engine behavior; use multiple lines only when one line is insufficient
- Exact Blueprint, asset, configuration, and binding actions when required
- Compile and runtime verification checklist
- Any unresolved evidence that prevents a truthful transcription-ready claim
