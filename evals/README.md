# Skill Routing Evaluations

Use `skill-routing.json` as a manual regression set after changing skill descriptions, routing guidance, onboarding, or stage-gate instructions.

## Run

1. Install the candidate plugin build and start a fresh Codex conversation for each case.
2. Submit the prompt exactly as written, without naming the expected skill.
3. Record the selected primary skill(s), whether required stage artifacts appeared in order, whether the agent modified files, and whether it made any prohibited claim.
4. Compare the run with `expected_primary`, `expected_supporting`, `required`, and `must_not` in the case.
5. Re-run the direct and boundary cases after changing a skill description. A routing change is not accepted if it fixes one case by causing an adjacent case to route incorrectly.

## Acceptance

- Every case selects the expected primary workflow, or an explicitly equivalent combination that preserves the expected boundaries.
- Blueprint is supporting-only unless the requested work is specifically about Blueprint/editor integration.
- No skill claims RAG use when the corresponding tools are unavailable.
- Project-change requests retain the full S0-S6 sequence and approval gates defined in `references/ue-core-rules.md`.
- Read-only and review-only cases do not modify project files.

These are prompt-level evaluations, not automated correctness proofs. Verify the actual response and file/tool effects; matching a skill name alone is insufficient.
