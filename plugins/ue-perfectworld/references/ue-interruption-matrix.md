# Interruption Matrix Review

Adversarial pre-delivery audit for changes touching budgets, transactions, lifecycle, cancellation, timers, leases, or multi-stage asynchronous chains (delivery, spawning, presentation, handoff, delegation, loading, sessions). Complements ue-review's correctness/regression pass; it does not replace compilation or PIE verification.

Positive confirmation (compiles, log loop closed, probes zero, call sites alive) only proves it runs. Timing defects live in "who can interrupt this, and what state does every field hold after the interruption" — invisible to line-by-line diff reading, findable only by exhaustive matrix.

Incident shape: registration of the request binding happened at animation completion, while cancellation could arrive during the 15-45s waiting window. A cancellation refunded the budget and cleared the session but could not stop the in-flight request (no request id registered yet); the late startup callback then unconditionally cleared the cancel flag and spawned a full wave with no transaction. Each of the three conditions was individually reasonable; stacked on one timeline they formed a budget bypass.

## Protocol

1. Draw the lifecycle timeline from submission to terminal state. Stage boundaries come from real state fields and callbacks in code, not from impressions
2. Enumerate interruption entries by searching the code: every Stop / Cancel / Reset / Abort / Close / EndPlay / TearDown call site, plus user or GM cancel, framework-initiated close, failure funnels, timeouts, repeat activation, owner invalidation
3. Fill the interruption-entry × stage matrix. Every cell states the key state at that moment: transaction (reserved/committed/finalized), lease (held/released), timer (alive/dead), flags, binding and weak references (registered/null), budget occupancy. A cell with no answer is a defect
   - Hunt latecomers: if an interrupt lands at stage N, does the stage N+1 startup path still run? What stops it? No guard = red cell
   - Hunt flag lifecycles: who sets, who clears, is the clear unconditional, can clear happen before a pending interrupt
4. Invariants, each asked against the matrix:
   - Budget conservation: every Reserve has exactly one of Commit / Cancel / Finalize
   - Resource symmetry: every acquire/register/timer has a release path reachable from interruption paths too
   - Cancel semantics: after cancel, no restart, no wave or budget consumption
   - Terminal idempotency: repeated terminal callbacks do not settle twice
   - Mechanism uniqueness: one mechanism collects a given resource per domain; a diff that adds a second mechanism next to a sibling solving the same problem is a red cell unless the plan carries a precedent table (ue-route-precedent-gate.md)
5. Survivor audit (mandatory after deletion or refactor rounds): what guarantees did the surviving code inherit from the deleted mechanism? Registration timing, implicit sequencing, "the renewal will cover it" assumptions — re-examine each. Deletion rounds focus on "deleted cleanly" and are the high-incidence zone for this class of miss
6. Testability: every red cell and every interruption path needs a trigger (GM command, log probe, test). An interruption path without a trigger may not be reported as verified

## Output

Matrix table with per-cell evidence, red-cell list with fix locations, test-gap list. Verdicts on code-traced paths are source-review level, not runtime level, unless a trigger fired.
