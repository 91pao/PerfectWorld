---
name: ue-implement
description: Implement or fix an Unreal Engine feature under a clear user mandate, with conservative changes, parallel agents, verification, and independent review. Do not edit for diagnosis-only, planning-only, or review-only requests.
---

# UE Implement

Always read the common reference set in `../../references/ue-core-rules.md`, plus:

- `../../references/ue-comment-log-rules.md`
- `../../references/ue-paste-code-gate.md`

Read only when applicable:

- Network authority, replication, or RPC work: `../../references/ue-client-server-boundary-rules.md`
- Bug fixes, compile/link errors, runtime failures, or regressions: `../../references/ue-bugfix-discipline.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`

## Workflow

0. Confirm a clear implementation or fix mandate and honor explicit no-edit or plan-first limits. Complete the relevant S0-S2 evidence and compact change manifest before dependent edits, then continue through S3-S6 within that mandate. A separate S2 approval is not required unless the user requested it or the proposed change crosses a hard boundary. Resolve implementation details autonomously; ask only for a real scope or product decision.
1. Discover current-project structure, callers, assets, configuration, ownership, persistence, cleanup, and candidate precedents before designing. When `ue_rag_*` tools are available, load `../../references/ue-rag-integration.md` for candidate discovery, then verify candidates with direct project reads.
2. Freeze the latest requirement and hard scope, discard superseded requirements, and pass the requirement-and-capability fit gate in `ue-project-consistency.md` before patching.
3. If the capability is shared infrastructure, apply `ue-architecture.md` before patching: identify all active consumers, define the public lifecycle contract, and separate generic resource/lifecycle behavior from business-specific reactions.
4. For non-trivial cross-system work, pass the mandatory evidence gate in `ue-project-consistency.md` before patching: data source, runtime lifecycle, trigger, read path, persistence, and cleanup must each have current-project proof.
5. For asynchronous resource or initialization work, prefer an existing completion event, delegate, callback, or future. Do not add Tick polling as the default wait mechanism; retain it only with an explicit compatibility reason and a removal boundary.
6. Build the responsibility evidence matrix and verify every introduced UI, navigation, state, object-access, guard, and diagnostic mechanism independently when applicable.
7. Verify that the chosen precedents are active, maintained, and compatible with the target ownership, lifecycle, authority, and cleanup behavior.
8. If a required design link is missing, pause only dependent edits and report the gap while continuing unblocked work; do not add a condition, manager, field, DataAsset, delegate, or lifecycle hook as a substitute for evidence.
9. State the implementation direction briefly. For substantial separable work, apply the parallel agent workflow in `ue-core-rules.md`: bounded roles, agreed interfaces, one writer per resource, and useful coordinator work in parallel.
10. Patch only the required files and blocks.
11. Apply the loaded reference rules as hard constraints.
12. Apply code style as a local, evidence-backed constraint: do not reformat unrelated code, and do not turn context-dependent recommendations into blocking changes.
13. Run `ue-self-review.md`, obtain independent review for substantial changes when agents are available, and correct confirmed in-scope issues without another approval round. Reverify affected checks and re-review the latest integrated result; report unresolved blockers honestly.
14. Do not run a full UE build unless explicitly asked.

## Final Response

Say:

- What files changed
- What behavior changed
- What the self-review found if there is residual risk
- That UE build was not run, unless the user explicitly asked and it was run
