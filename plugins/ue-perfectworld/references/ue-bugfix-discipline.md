# UE Bugfix Discipline

Use these rules when fixing bugs, compile errors, runtime errors, UI issues, RPC failures, and data problems.

See `ue-client-server-boundary-rules.md` for the general client/server and RPC boundary rules.

- Do not start by adding fallback branches, new flags, or wrapper functions
- First identify the root cause: wrong data, wrong lifecycle, wrong authority side, missing binding, stale state, invalid config, race, or encoding/tooling issue
- Prefer fixing the broken condition at its source over adding another layer around it
- Keep the fix local to the failing path unless the same bug is proven in multiple places
- Do not broaden a narrow bug fix into a refactor
- Do not add a manager, cache, retry queue, state machine, or generic result type just to fix one bug
- Do not keep both old and new paths unless the project already has a compatibility requirement
- Remove dead temporary code created during investigation
- If the bug is caused by duplicated logic, consolidate only the minimum duplicated part needed to stop the bug
- If the bug is caused by missing validation, add the validation at the same layer where nearby project code validates it
- If a defensive return hides the real failure, add a targeted log with operation name and key IDs
- After proposing or applying a fix, explain why it fixes the root cause and why it does not add unnecessary complexity

## Mutable State and Event Identity

- Do not use a mutable current selection as the identity of an asynchronous event, projectile, request, or delayed callback
- A state change after an event starts must not change that event's fixed type, damage, radius, cooldown, or ownership context
- Use a per-action snapshot or immutable event identity when concurrent or delayed actions are possible; a shared pending value is acceptable only when the project proves that a second action cannot succeed before the first callback

## Avoid Redundant State and Speculative APIs

- Do not maintain a boolean and a numeric or enum state when both always encode the same condition; keep a separate flag only for a distinct transition that cannot be derived from the primary state
- Before adding a wrapper or public action entry point, verify its real C++ and Blueprint callers and keep selection and execution responsibilities separate
- If an API is BlueprintCallable, check Blueprint references before removing or changing its contract

## Bad Bugfix Smells

- Adding `bHasHandled`, `bForceRefresh`, `bIgnoreNext`, or similar flags without proving lifecycle necessity
- Adding a timer delay to hide ordering problems
- Adding a retry instead of fixing the failed condition
- Adding a generic helper used only once
- Catching all invalid states and silently returning when the user or developer needs a clear reason
