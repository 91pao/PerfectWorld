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
4. Separate likely root cause from symptoms.
5. Reject fixes that only add fallback state, retries, timers, or wrappers without proving root cause.
6. Apply the recovery gate in `ue-bugfix-discipline.md` when related failures keep accumulating.
7. Do not run full UE builds by default.
8. If editing is required but direct edits were not explicitly requested, switch to `ue-draft`.
9. If the user explicitly asked for direct file edits, switch to the implementation workflow and follow edit safety.
10. Keep the diagnosis and proposed remedy minimal, evidence-backed, and explicit about unresolved uncertainty.

## Checks

Use the loaded references to guide checks. Prioritize root cause, evidence quality, ownership, lifecycle, authority and replication when applicable, data/configuration flow, asset state, encoding, and tooling issues.
