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

## Bad Bugfix Smells

- Adding `bHasHandled`, `bForceRefresh`, `bIgnoreNext`, or similar flags without proving lifecycle necessity
- Adding a timer delay to hide ordering problems
- Adding a retry instead of fixing the failed condition
- Adding a generic helper used only once
- Catching all invalid states and silently returning when the user or developer needs a clear reason
