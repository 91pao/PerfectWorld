# UE Architecture And Shared Infrastructure

Use this reference whenever a UE task touches a shared component, manager, subsystem, pool, resource loader, factory, base class, public API, or a capability that has more than one active consumer.

## Architecture First

- Classify the requested behavior before writing code: local feature logic, shared infrastructure, or a change to an existing public contract.
- If the same capability is used by multiple systems, review the shared owner first. Do not implement the first caller's workaround as if it were the architecture.
- Map the complete contract before selecting a mechanism: acquisition, initialization, readiness, success, failure, cancellation, reuse, release, and cleanup.
- Identify the authoritative owner of each state. A caller may request or consume a state, but should not duplicate the shared component's loading or lifecycle state without evidence.
- Keep the public API responsible for generic lifecycle behavior; keep each business caller responsible only for its domain-specific reaction.

## Event Versus Tick

- Use an event, delegate, callback, future, or existing async completion API for one-time transitions such as resource loading, initialization, registration, completion, and failure.
- Do not use per-frame Tick polling as the default way to wait for an asynchronous transition in a shared system.
- Tick is appropriate for continuous work whose value changes with time or frame progression: movement, interpolation, tracking, simulation, and continuous parameter updates.
- A one-frame delay caused by polling is a correctness and API-design smell, even when its CPU cost is small.
- If polling is temporarily retained for compatibility, document it as a bounded migration state and keep the polling responsibility out of the shared public API.

## FX Example

For a shared FX resource container such as `PlayEffectDeferred`:

- The public component owns pool acquisition, table lookup, cache lookup, async loading, success/failure completion, and recycle cleanup.
- The public component should expose one resource-ready contract that works for cache hits, async completion, and failure. Consumers should not each implement a loading wait loop.
- A consumer such as a laser owns domain behavior after readiness: parameter initialization, activation timing, travel progression, and target tracking.
- The laser Tick may update a moving endpoint every frame, but it must not be the public mechanism that waits for Niagara resource loading.
- Handle or generation validation is part of the pooled callback contract; a late callback must not affect a recycled component's next consumer.

## Pool And Async Contract

For a pooled component that loads resources asynchronously, verify all of the following before accepting the design:

- A new acquire starts one clearly defined usage cycle.
- The component exposes a single resource-ready notification for success and failure, or an existing project-native equivalent.
- Cache-hit completion is handled synchronously or through an explicit ready-state check before binding the notification.
- A canceled, recycled, or reused component cannot deliver an old callback to the new consumer.
- The callback validates the current handle, usage generation, request serial, or resource path before changing state.
- Recycle clears bindings, timers, pending requests, transient state, and ownership references.
- A failed load reaches the same terminal notification path as a successful load; callers must not wait forever.
- One usage cycle does not initialize the same resource twice through overlapping public entry points.

## Shared API Review

When a task proposes a new shared delegate, manager, wrapper, cache, or lifecycle hook:

1. List active consumers and prove that each one needs the same contract.
2. Separate generic resource/lifecycle work from business-specific activation or presentation.
3. Define reentrancy and ordering for synchronous cache hits, asynchronous completion, failure, cancellation, and recycle.
4. Define who binds, who unbinds, and what happens when the consumer stops before completion.
5. Check whether the existing API already owns the responsibility; remove duplicate initialization and parallel wait paths.
6. Keep the shared API small. Do not add a framework abstraction merely to hide one caller's local behavior.

## Required Output

For a shared-infrastructure task, the plan or review must explicitly state:

- Why the capability is shared rather than local.
- The current owner and all verified consumers.
- Why the selected mechanism is event-driven, Tick-driven, or a combination.
- The cache-hit, failure, cancellation, pool-reuse, and cleanup behavior.
- Which business code remains outside the shared component.
- Any temporary polling or duplicate path that remains and why it is not yet removed.
