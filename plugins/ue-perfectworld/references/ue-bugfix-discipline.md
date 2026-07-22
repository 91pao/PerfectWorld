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

## Mutable State And Event Identity

- Do not use a mutable current selection as the identity of an asynchronous event, projectile, request, or delayed callback
- Preserve fixed type, value, radius, cooldown, ownership, and authority context for the lifetime of an event
- Use a per-action snapshot when concurrent or delayed actions are possible; use shared pending state only when the project proves a second action cannot overlap

## Recovery Gate

- Treat repeated compile, link, reflection, asset, or configuration failures as a possible architecture or integration error
- After multiple related failures or patches to the same feature, stop adding local fixes and retrace ownership, data flow, lifecycle, registration, and project precedent end to end
- Remove temporary investigation code and obsolete workaround state before finalizing
- Do not claim completion until the runtime path and required editor/data setup are verified or explicitly identified as unverified

## Rejected Patterns

- Redundant booleans that duplicate an existing enum or numeric state
- Public wrappers or Blueprint APIs without verified callers
- One-use generic helpers, managers, caches, retry queues, result types, or state machines
- Silent catch-all returns where the developer or user needs a clear reason
