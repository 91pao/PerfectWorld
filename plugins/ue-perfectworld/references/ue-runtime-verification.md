# Runtime Verification By Log

Method for the runtime level of the verification ladder: how to accept or reject a runtime claim from PIE logs, so that "verified" means evidence, not confidence. Extends ue-self-review's "match the conclusion to the highest verification level actually reached".

## Probe List (define before the run)

Before the user runs PIE, list the failure-probe log tags this change must keep at zero, with expected values. Example shape: admission-grant-missing = 0, lease-rejected = 0 unless the scenario intentionally blocks an anchor, window-derive-failed = 0. A probe list written after the run is not acceptance, it is narration.

## Timeline Tracing (the primary technique)

Pick one request GUID from the log and trace it across subsystems by that single id: lease acquisition → budget (reserve → commit → finalize) → presentation → settlement. Check three properties:

1. Closure: every open state has its close event in the same run
2. Interval sanity: commit should sit milliseconds after reserve when the design commits early; a commit seconds later means the sequencing drifted
3. Terminal state matches the design: PartiallyCompleted versus Completed versus Failed, with the reason name matching the intended semantics

## Tag Census

Count occurrences per log tag in the run and compare against expectation (census, not spot reading — one grep per tag). Distinguish three classes before judging a warning noisy:

- New behavior of this change: judge against design
- Pre-existing pattern: verify against older logs (backup logs) before claiming regression — a pattern present in history is not this change's defect
- Known non-issue with documented reason (map density, legacy batch accounting): record, do not relitigate

## Honest Scoping

- Log closure proves the observed scenario, not all scenarios; interruption paths without a trigger stay unverified (ue-interruption-matrix.md step 6)
- Tearing down must be checked too: world-teardown lines showing active=0 and no tombstones is part of acceptance
- State the verification level reached in the conclusion: source review, runtime-observed, or runtime-with-triggered-interruption
