# UE Bugfix Discipline

Use these rules for bugs, compile or link errors, runtime failures, UI issues, RPC failures, and data problems.

## Root Cause First

- Read the exact error, log, reproduction, and failing path before proposing changes
- Identify whether the source is data, lifecycle, authority, binding, state, configuration, ownership, race, encoding, tooling, or build integration
- Fix the broken condition at its source instead of adding fallback branches, flags, timers, retries, wrappers, or parallel state
- Keep the fix local unless the same root cause is proven in multiple paths
- Do not broaden a narrow fix into a refactor or preserve both old and new paths without a verified compatibility requirement
- Add targeted diagnostics when a defensive return would otherwise hide an actionable failure
- Explain why the remedy fixes the root cause and why it does not add unnecessary structure

## Multiple Hypotheses And Probe Discipline

- Keep plausible causes falsifiable and rank them by the reported evidence; do not invent 3-5 hypotheses for a deterministic failure. Parallelize independent traces or probes when useful, but avoid concurrent mutation of the same runtime or asset
- One probe tests exactly one prediction: change one variable at a time, and prefer a breakpoint or a log that separates two hypotheses over bulk logging; never "log everything and grep"
- Prefix every temporary diagnostic log with a unique token such as `[DEBUG-a4f2]`, and grep every token to zero before declaring the fix complete
- A runtime reproduction counts only after it produced the reported symptom. Without runtime access, investigate source and existing logs, distinguish hypotheses from confirmed causes, and state the missing validation; never present a simulation or syntax check as the actual reproduction
- For performance regressions, establish a baseline measurement first (profiler, stat counters, timing harness) and bisect against it; measure first, fix second

## Mutable State And Event Identity

- Do not use a mutable current selection as the identity of an asynchronous event, projectile, request, or delayed callback
- Preserve fixed type, value, radius, cooldown, ownership, and authority context for the lifetime of an event
- Use a per-action snapshot when concurrent or delayed actions are possible; use shared pending state only when the project proves a second action cannot overlap

## Recovery Gate

- Treat repeated compile, link, reflection, asset, or configuration failures as a possible architecture or integration error
- After multiple related failures or patches to the same feature, stop adding local fixes and retrace ownership, data flow, lifecycle, registration, and project precedent end to end
- Before adding a new condition, manager, field, DataAsset, delegate, or lifecycle override during recovery, pass the mandatory evidence gate in `ue-project-consistency.md`; do not use a new abstraction to conceal an unverified trigger, persistence, or cleanup path
- Remove temporary investigation code and obsolete workaround state before finalizing
- Track the temporary probes introduced by this task, including their tokens, counters, bindings, and helper files. Remove them after their purpose is met unless explicitly retained; preserve the production fix and pre-existing diagnostics
- Do not claim completion until the runtime path and required editor/data setup are verified or explicitly identified as unverified

## Serial Gate Debugging

- Multi-gate serial chains (validation → resource → execution → settlement) have a characteristic debugging pattern: fixing one gate exposes the next. This is progress, not regression. Track which gate number you are on, not how many fix rounds have elapsed.
- Track the contracts actually verified and the next observable failure. Do not guess a total gate count or treat repeated patches as evidence of progress.
- Do not conflate "the previous fix didn't work" with "the previous fix exposed a new failure." Verify by checking whether the previous failure mode still reproduces; if it does not, the fix worked and the new failure is a downstream gate.

## Rejected Patterns

- Redundant booleans that duplicate an existing enum or numeric state
- Public wrappers or Blueprint APIs without verified callers
- One-use generic helpers, managers, caches, retry queues, result types, or state machines
- Silent catch-all returns where the developer or user needs a clear reason
