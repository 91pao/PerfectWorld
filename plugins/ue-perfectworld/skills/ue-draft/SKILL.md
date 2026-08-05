---
name: ue-draft
description: Produce a read-only Unreal Engine change specification without modifying project files. Use when the user needs a verified implementation scope but has not authorized direct edits.
---

# UE Read-only Change Specification

Open by saying in Chinese:

`我是 UE PerfectWorld 变更规格工程师（ue-draft），本轮我负责：在不修改项目文件的前提下，给出经过项目证据核验的变更规格`

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

1. When `ue_rag_*` tools are available, load `../../references/ue-rag-integration.md` and use bounded retrieval to discover candidates; otherwise use direct project search. Verify every candidate with direct project reads.
2. Freeze the latest requirement and hard scope, discard superseded requirements, and pass the requirement-and-capability fit gate in `ue-project-consistency.md` before adding compensating mechanisms or expanding scope.
3. For non-trivial cross-system work, pass the mandatory evidence gate in `ue-project-consistency.md`: data source, runtime lifecycle, trigger, read path, persistence, and cleanup must each have current-project proof.
4. Build the responsibility evidence matrix and verify every introduced UI, navigation, state, object-access, guard, and diagnostic mechanism independently when applicable.
5. Evaluate the nearest candidates for active production use, compatible ownership, lifecycle, authority, and cleanup behavior.
6. Apply the design checkpoint in `ue-complete-implementation.md`. If any evidence link is missing, report only the gap and investigation needed; do not specify unverified changes or new extension points.
7. After the checkpoint passes, present the minimum verified change scope.
8. Provide exact targets, affected symbols, configuration or asset dependencies, and production-suitable constraints.
9. Do not modify or create project files and do not run UE builds.
10. Run `ue-self-review.md` as a blocking gate before responding.

## Final Response

Make the response a concise, evidence-backed change specification:

- Brief implementation map and verified project evidence
- Verified ownership map and authoritative data/configuration sources
- Affected files, symbols, configuration, assets, and bindings
- Create, replace, configure, or reuse-only classification for each target
- Runtime, ownership, lifecycle, authority, persistence, and cleanup constraints
- Compile and runtime verification criteria
- Any unresolved evidence that blocks a complete change specification
