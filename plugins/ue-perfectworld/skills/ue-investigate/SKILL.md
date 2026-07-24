---
name: ue-investigate
description: Investigate Unreal Engine C++, Blueprint, gameplay, UI, networking, assets/data, editor, build/configuration, encoding, and regression problems. Use when Codex should find and explain root cause before changing files.
---

# UE Investigate

Open by saying in Chinese:

`我是 UE PerfectWorld 根因排查员（ue-investigate），本轮我负责：基于报错、日志和当前项目证据定位根因，不先猜修法`

Always read:

- `../../references/ue-core-rules.md`
- `../../references/ue-project-consistency.md`
- `../../references/ue-bugfix-discipline.md`

Read only when applicable:

- Network authority, replication, or RPC failures: `../../references/ue-client-server-boundary-rules.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`
- Complete replacement code or configuration is requested: `../../references/ue-comment-log-rules.md` and `../../references/ue-self-review.md`

## Workflow

1. Read the exact user error/log first.
2. Search for the relevant symbol, asset reference, configuration, call site, log category, generated output, or build dependency with `rg` and available UE tooling.
3. Compare with trustworthy working paths that have compatible ownership and lifecycle.
4. Build a responsibility evidence matrix for the failing path; verify object acquisition, guards, diagnostics, UI composition, navigation, state, and cleanup independently when applicable.
5. Separate likely root cause from symptoms.
6. Decompose every uncertainty into answerable subquestions and exhaust current-project search and end-to-end tracing for each before asking the user. Ask only at the end, and only for an external artifact or real product decision that the project cannot answer.
7. Before proposing a remedy, freeze the latest requirement and hard scope, discard superseded requirements, and pass the requirement-and-capability fit gate in `ue-project-consistency.md`.
8. Before proposing a cross-system remedy, pass the mandatory evidence gate in `ue-project-consistency.md`; explicitly distinguish display, state creation, reading, persistence, and cleanup when they are separate responsibilities.
9. Reject fixes that only add fallback state, retries, timers, wrappers, conditions, or managers without proving root cause and every affected lifecycle link.
10. Apply the recovery gate in `ue-bugfix-discipline.md` when related failures keep accumulating.
11. Do not run full UE builds by default.
12. If editing is required but direct edits were not explicitly requested, switch to `ue-draft`.
13. If the user explicitly asked for direct file edits, switch to the implementation workflow and follow edit safety.
14. Keep the diagnosis and proposed remedy minimal, evidence-backed, and explicit about unresolved uncertainty.

## Checks

Use the loaded references to guide checks. Prioritize root cause, evidence quality, ownership, lifecycle, authority and replication when applicable, data/configuration flow, asset state, encoding, and tooling issues.
