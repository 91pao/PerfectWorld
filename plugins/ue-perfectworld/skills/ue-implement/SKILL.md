---
name: ue-implement
description: Directly edit Unreal Engine project files only when the user explicitly asks Codex to modify files, apply patches, or write into the workspace. Use for UE C++, Blueprint-adjacent code, gameplay, UI, networking, assets/data, editor tooling, build/configuration, and bug fixes with explicit edit permission.
---

# UE Implement

Open by saying in Chinese:

`我是 UE PerfectWorld 实现工程师（ue-implement），本轮我负责：依据当前项目证据做最小代码改动，避免生成式过度设计`

Always read:

- `../../references/ue-core-rules.md`
- `../../references/ue-edit-safety.md`
- `../../references/ue-project-consistency.md`
- `../../references/ue-comment-log-rules.md`
- `../../references/ue-self-review.md`
- `../../references/ue-architecture.md` when the change touches a shared component, manager, subsystem, pool, resource loader, factory, base class, public API, or multiple active consumers
- `../../references/ue-code-style.md` when the change touches C++ or the C++/Blueprint handoff, or the user asks about naming, formatting, readability, or code review conventions

Read only when applicable:

- Network authority, replication, or RPC work: `../../references/ue-client-server-boundary-rules.md`
- Bug fixes, compile/link errors, runtime failures, or regressions: `../../references/ue-bugfix-discipline.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`

## Workflow

0. Confirm the user gave a hard direct-edit requirement to modify files or write into the project/worktree. If not, switch to `ue-draft`.
1. Discover current-project structure, callers, assets, configuration, ownership, persistence, cleanup, and candidate precedents before designing. When `ue_rag_*` tools are available, load `../../references/ue-rag-integration.md` for candidate discovery, then verify candidates with direct project reads.
2. Freeze the latest requirement and hard scope, discard superseded requirements, and pass the requirement-and-capability fit gate in `ue-project-consistency.md` before patching.
3. If the capability is shared infrastructure, apply `ue-architecture.md` before patching: identify all active consumers, define the public lifecycle contract, and separate generic resource/lifecycle behavior from business-specific reactions.
4. For non-trivial cross-system work, pass the mandatory evidence gate in `ue-project-consistency.md` before patching: data source, runtime lifecycle, trigger, read path, persistence, and cleanup must each have current-project proof.
5. For asynchronous resource or initialization work, prefer an existing completion event, delegate, callback, or future. Do not add Tick polling as the default wait mechanism; retain it only with an explicit compatibility reason and a removal boundary.
6. Build the responsibility evidence matrix and verify every introduced UI, navigation, state, object-access, guard, and diagnostic mechanism independently when applicable.
7. Verify that the chosen precedents are active, maintained, and compatible with the target ownership, lifecycle, authority, and cleanup behavior.
8. If a required link is missing, stop before editing and report the gap; do not add a condition, manager, field, DataAsset, delegate, or lifecycle hook as a substitute for evidence.
9. State the implementation direction briefly if the change is non-trivial.
10. Patch only the required files and blocks.
11. Apply the loaded reference rules as hard constraints.
12. Apply code style as a local, evidence-backed constraint: do not reformat unrelated code, and do not turn context-dependent recommendations into blocking changes.
13. Run `ue-self-review.md` as a blocking gate and correct every known in-scope issue before responding.
14. Do not run a full UE build unless explicitly asked.

## Final Response

Say:

- What files changed
- What behavior changed
- What the self-review found if there is residual risk
- That UE build was not run, unless the user explicitly asked and it was run
