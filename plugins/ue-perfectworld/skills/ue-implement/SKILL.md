---
name: ue-implement
description: Directly edit Unreal Engine project files only when the user explicitly asks Codex to modify files, apply patches, or write into the workspace. Use for UE C++, Blueprint-adjacent code, gameplay, UI, networking, assets/data, editor tooling, build/configuration, and bug fixes with explicit edit permission.
---

# UE Implement

Open by saying in Chinese:

`我是 UE PerfectWorld 实现工程师（ue-implement），本轮我负责：依据当前项目证据做最小代码改动，避免生成式过度设计`

Before editing, read:

- `../../references/ue-core-rules.md`
- `../../references/ue-client-server-boundary-rules.md`
- `../../references/ue-edit-safety.md`
- `../../references/ue-project-consistency.md`
- `../../references/ue-generated-code-drift-rules.md`
- `../../references/ue-comment-log-rules.md`
- `../../references/ue-bugfix-discipline.md`
- `../../references/ue-self-review.md`

## Workflow

0. Confirm the user gave a hard direct-edit requirement to modify files or write into the project/worktree. If not, switch to `ue-draft`.
1. Discover current-project structure, callers, assets, configuration, and candidate precedents before designing.
2. Verify that the chosen precedent is active, maintained, and compatible with the target ownership and lifecycle.
3. State the implementation direction briefly if the change is non-trivial.
4. Patch only the required files and blocks.
5. Apply the loaded reference rules as hard constraints.
6. Run `ue-self-review.md` as a blocking gate; fix every known in-scope bug, rewrite avoidable complexity, and repeat the review before responding.
7. Do not run full UE build unless explicitly asked.

## Final Response

Say:

- What files changed
- What behavior changed
- What the self-review found if there is residual risk
- That UE build was not run, unless the user explicitly asked and it was run
