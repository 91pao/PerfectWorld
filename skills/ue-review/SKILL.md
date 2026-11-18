---
name: ue-review
description: Review an existing Unreal Engine diff, patch, or applied change for correctness, lifecycle, authority, project consistency, overdesign, and missing validation. Use only for a review request; do not edit files or replace root-cause diagnosis.
---

# UE Review

Always read the common reference set in `../../references/ue-core-rules.md`.

Read only when applicable:

- Network authority, replication, or RPC changes: `../../references/ue-client-server-boundary-rules.md`
- A bug-fix patch or accumulated workaround chain: `../../references/ue-bugfix-discipline.md`
- Comment or diagnostic changes: `../../references/ue-comment-log-rules.md`
- Encoding or patch-integrity risk: `../../references/ue-edit-safety.md`
- UI entry parameters or event payloads: `../../references/ue-ui-param-contract-rules.md`
- Currency, inventory, rewards, purchases, or persistent resource changes: `../../references/ue-economy-rpc-rules.md`

## Review Priorities

This skill performs the S5 review of the available change and verification evidence. Missing earlier stage paperwork does not block review; inspect the actual patch and report unavailable checks. A review-only request remains read-only. When supporting an authorized implementation, return confirmed findings to its owner for bounded correction and recheck the resulting version before a clean conclusion.

For substantial work, follow the parallel agent workflow in `ue-core-rules.md`: split independent review responsibilities when useful, inspect a stable baseline and diff, and reconcile findings with the final integrated snapshot. Reviewers must verify actual contracts and scope rather than endorse the author's summary. The coordinator confirms disputed findings; review-only agents do not edit.

When the review target is a patch batch applied by the user, first verify application completeness: re-read the touched regions, confirm anchor placement, and run a residual-symbol sweep for APIs the batch removed. A partially applied patch is a finding category of its own, ordered above any code-level finding.

When `ue_rag_*` tools are available, load `../../references/ue-rag-integration.md` to discover related active paths, then verify them directly before drawing a review conclusion.

For shared infrastructure, review architecture before local behavior: verify the shared owner, all active consumers, the public lifecycle contract, cache-hit and failure paths, cancellation and pool reuse, callback cleanup, and duplicate initialization. Flag per-frame Tick polling used only to wait for an asynchronous transition as an architectural finding, not merely a performance suggestion. Keep Tick when it owns continuous progression or tracking.

For C++ style, use `ue-code-style.md` to separate blocking correctness or generated-code risks from recommendations and context-dependent tradeoffs. Require project evidence before enforcing prefixes, casing, `auto`, indexed loops, division/square-root avoidance, or access changes.

Find real issues first. Use the loaded references as the checklist, starting with whether the implementation still matches the latest requirement and hard scope and whether any mechanism survives only from superseded requirements. Check requirement-and-capability fit before accepting compensating mechanisms or scope expansion, then inspect evidence-gate gaps across data source, runtime lifecycle, trigger, read path, persistence, and cleanup. Require separate responsibility evidence for UI composition, navigation, state, object access, guards, and diagnostics when applicable; also check correctness, project consistency, lifecycle, authority and replication, state mutation, duplicated authority, avoidable structure, and whether a teammate can maintain the result without the AI conversation.

When the change adds a holder or a gate consumer of shared state (points, flags, leases, budget slots), run the Claim Audit in `../../references/ue-self-review.md` before concluding: a direction matrix over every holder-latecomer pair, the worst-case blocking lifetime for every consumed external flag (grep every set and clear site), and seam-first effort on untouched legacy paths the new logic intersects. A missing direction row or an unbounded block is a P1/P2 finding even when the new code's own logic is internally consistent — reviewing the new door you built is not reviewing the old doors that now need to respect your lock.

Before finalizing the review, run the final self-review against the findings so safety-sensitive gaps, false confidence, missed defects, and overdesigned remedies are corrected. Keep suggested fixes minimal; do not edit files during a review-only request.

## Output Format

Check **requirement fit**, **consistency and lifecycle**, and **overdesign** independently; passing one does not clear another. Follow the user's requested format. Otherwise lead with actionable findings ordered by severity, with source locations and relevant verification gaps; group by axis only when that helps the reader. Do not print empty categories or require a separate stage report for a small review.

If something is only a style concern and not a real risk, label it as low priority or omit it.

Do not suggest broad rewrites when a local simplification is enough.
