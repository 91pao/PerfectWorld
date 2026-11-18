# Skill Routing Evaluations

Use `skill-routing.json` as a manual routing and behavior regression set after changing skill descriptions, routing guidance, onboarding, authorization, or evidence-checkpoint instructions.

## Run

1. Install the candidate plugin build and start a fresh Codex conversation for each case. If a case has `setup`, prepare its minimum project fixture or prior conversation facts in an isolated workspace. These facts are inputs, not expected conclusions; do not show the agent the evaluation criteria.
2. Submit `prompt` exactly as written, without naming the expected skill. For resume cases, retain the described authorization history and inspect the current files after resuming.
3. Record the selected primary and supporting skills, the evidence gathered, scope summary, actual file/tool effects, review snapshot, verification performed, and any prohibited claim. Preserve the run transcript and resulting diff so another reviewer can assess the result.
4. Compare the run with `expected_primary`, `expected_supporting`, `required`, and `must_not` in the case.
5. Re-run the direct and boundary cases after changing a skill description. A routing change is not accepted if it fixes one case by causing an adjacent case to route incorrectly.

## Acceptance

- Every case selects the expected primary workflow, or an explicitly equivalent combination that preserves the expected boundaries.
- Blueprint is supporting-only unless the requested work is specifically about Blueprint/editor integration.
- No skill claims RAG use when the corresponding tools are unavailable.
- Applicable S0-S6 evidence checkpoints remain grounded in project facts. Compact checkpoints may be combined and completed in one authorized turn; separate manual approval at each checkpoint is not required.
- A clear implementation or fix request authorizes bounded edits after evidence gathering and a short visible scope summary. Read-only planning, diagnosis, review, and explicit no-edit requests retain their boundaries.
- Unresolved product decisions and necessary scope expansion require a user decision before dependent changes. An internal checkpoint is not itself a reason to ask again for existing edit authorization.
- Reuse or configuration is preferred when evidence shows it satisfies the request. New code must address a demonstrated gap; cleanup must be attributable to the authorized change.
- Parallel work uses bounded roles and disjoint file writers, adapts to actual capacity, and reviews the integrated result. After a fix, affected verification and review cover the latest snapshot.
- Resumed work recovers the latest requirement, scope, authorization, and current diff from evidence. A continuation prompt does not create authorization absent from the prior task.
- Read-only and review-only cases do not modify project files.
- Setup initialization writes only the requested concurrency setting (default 12) in an isolated configuration directory, preserves unrelated TOML, and verifies the saved result. Inspection-only setup stays read-only; a saved ceiling is not proof of expanded runtime slots.

Run `python tests/validate_plugin.py` from the plugin root for static manifest, skill metadata, reference, and evaluation-schema checks. It does not execute these scenarios or judge the behavior described by `required` and `must_not`.

These are manual prompt-level evaluations, not automated correctness proofs. Report which cases were actually run and retain failures separately from static validation results. A schema pass or a matching skill name does not establish correct scope, code, review, or runtime behavior.
