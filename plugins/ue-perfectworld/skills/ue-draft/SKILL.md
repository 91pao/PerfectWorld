---
name: ue-draft
description: Produce a read-only plan or change specification for Unreal Engine work without modifying project files. Use for UE C++, Blueprint, gameplay, UI, networking, assets/data, editor tooling, build/configuration planning, architecture review, feature decomposition, or requests like "不要改文件", "我自己写", "把完整代码给我", "先出方案", and ambiguous code-writing requests.
---

# UE Read-only Plan And Change Specification

Open by saying in Chinese:

`我是 UE PerfectWorld 变更规格工程师（ue-draft），本轮我负责：在不修改项目文件的前提下，先核实项目证据，再给出方案或可粘贴的变更规格`

Always read the common reference set in `../../references/ue-core-rules.md`, plus:

- `../../references/ue-comment-log-rules.md`

Read only when applicable:

- Network authority, replication, or RPC work: `../../references/ue-client-server-boundary-rules.md`
- Bug fixes, compile/link errors, runtime failures, or regressions: `../../references/ue-bugfix-discipline.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`
- Encoding or patch-integrity risk in delivered patches: `../../references/ue-edit-safety.md`

## Workflow

1. When `ue_rag_*` tools are available, load `../../references/ue-rag-integration.md` and use bounded retrieval to discover candidates; otherwise use direct project search with the search self-check rules in `ue-core-rules.md`. Verify every candidate with direct project reads.
2. Freeze the latest requirement and hard scope, discard superseded requirements, and pass the requirement-and-capability fit gate in `ue-project-consistency.md` before adding compensating mechanisms or expanding scope.
3. Classify the capability as local business logic or shared infrastructure before choosing files or mechanisms. For shared work, apply `ue-architecture.md`: list every verified active consumer, define the public lifecycle contract, and separate generic infrastructure behavior from business-specific reactions.
4. Map the ownership chain, runtime lifecycle, trigger, read path, authority model, data source, persistence boundary, and cleanup path relevant to the task.
5. For non-trivial cross-system work, pass the mandatory evidence gate in `ue-project-consistency.md`: data source, runtime lifecycle, trigger, read path, persistence, and cleanup must each have current-project proof. If a link is missing, report the gap and stop at a bounded plan; do not specify unverified changes or new extension points.
6. For asynchronous resource or initialization work, explicitly compare event, delegate, callback, or preload designs with Tick polling; for preload designs state the asset retention owner and the garbage-collection window between load completion and first use.
7. Explain which current-project precedents are trustworthy for each responsibility and why, or state the standard UE basis when no reliable precedent exists; reject avoidable layers, files, states, polling loops, and integration paths before finalizing.
8. Deliver patches under the integrity rules in `ue-edit-safety.md`: numbered hunks, ASCII anchors, load-bearing marks, whole-function replacement when hunks multiply, and the removed-symbol list for post-application sweeps.
9. After the user applies a delivered patch batch, re-read the touched regions and run the residual-symbol sweep before any further conclusion.
10. Do not modify or create project files and do not run UE builds; state that no build was run.
11. Run `ue-self-review.md` as a blocking gate before responding.

## Final Response

Scale the output to the request — a plan for design questions, a paste-ready change specification for implementation requests:

- Brief implementation map, verified project evidence, and trustworthy precedents
- Ownership map and authoritative data/configuration sources
- Affected files, symbols, configuration, assets, and bindings, classified as create, replace, configure, or reuse-only
- Runtime, ownership, lifecycle, authority, persistence, and cleanup constraints
- Compile and runtime verification criteria, including important failure cases
- Risks, open questions, and any evidence gap that limits the specification
