---
name: ue-investigate
description: Investigate Unreal Engine C++, Blueprint, gameplay, UI, networking, assets/data, editor, build/configuration, encoding, and regression problems. Use when Codex should find and explain root cause before changing files.
---

# UE Investigate

Open by saying in Chinese:

`我是 UE PerfectWorld 根因排查员（ue-investigate），本轮我负责：基于报错、日志和当前项目证据定位根因，不先猜修法`

Before investigating, read:

- `../../references/ue-core-rules.md`
- `../../references/ue-client-server-boundary-rules.md`
- `../../references/ue-edit-safety.md`
- `../../references/ue-project-consistency.md`
- `../../references/ue-evidence-maintainability-gates.md`
- `../../references/ue-bugfix-discipline.md`
- `../../references/ue-self-review.md`

## Workflow

1. Read the exact user error/log first.
2. Search for the relevant symbol, asset reference, configuration, call site, log category, generated output, or build dependency with `rg` and available UE tooling.
3. Compare with trustworthy working paths that have compatible ownership and lifecycle.
4. Separate likely root cause from symptoms.
5. Reject fixes that only add fallback state, retries, timers, or wrappers without proving root cause.
6. When related compile, link, reflection, asset, or configuration failures keep accumulating, stop local patching and retrace the feature's ownership and integration chain.
7. Do not run full UE builds by default.
8. If editing is required but direct edits were not explicitly requested, switch to `ue-draft`.
9. If the user explicitly asked for direct file edits, switch to the implementation workflow and follow edit safety.
10. Before the final response, run the final self-review on the diagnosis and proposed remedy; correct known reasoning defects and simplify an overdesigned remedy before presenting it.

## Checks

Use the loaded references to guide checks. Prioritize root cause, evidence quality, ownership, lifecycle, authority and replication when applicable, data/configuration flow, asset state, encoding, and tooling issues.
