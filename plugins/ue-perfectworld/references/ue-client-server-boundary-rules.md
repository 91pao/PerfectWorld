# UE Client Server Boundary Rules

Use these rules only after determining whether the current project and feature are networked.

- Do not introduce RPC or replication into standalone, editor-only, or local-only flows without a real networking requirement
- In networked gameplay, client checks may improve responsiveness but must not replace server validation for authoritative state
- Validate requester identity and ownership, permissions, input, current state, replay or duplicate requests, and relevant limits on the authoritative side
- Resolve the requesting player or owning object through the project's verified ownership path; do not substitute an arbitrary controller, pawn, or actor to make a request appear valid
- Prefer replicated state for durable shared state and RPCs for commands or transient targeted notifications, following the project's established model
- Use reliable RPCs only when delivery guarantees are required; avoid reliable high-frequency traffic
- One confirmed user action should usually map to one authoritative command unless the protocol genuinely requires multiple phases
- Do not duplicate authoritative calculations, inventory changes, rewards, persistence, or expensive scans on the client
- Keep visual prediction or local prechecks explicitly separate from committed state
- On validation failure, use the project's established logging and user-feedback mechanisms without leaking sensitive server details
- Recheck ownership, lifecycle, relevancy, dormancy, and replication timing when behavior differs between server, owning client, and simulated clients

## Client-Reported Action Data

- Treat client-provided actor IDs, target IDs, target lists, hit counts, tool types, and hit locations as input data, not proof that the action occurred
- Validate the claimed action's authorization, current lifecycle state, replay or duplicate status, rate limit, target scope, and per-action limits on the server
- Deduplicating IDs and rejecting invalid or dead targets are baseline checks; they do not prove that the submitted targets were inside the valid hit area

## Cooldown Clock Semantics

- Define whether a cooldown starts when the action is accepted, the spawned actor is created, the projectile impacts, or the damage is committed
- Keep client and server cooldown semantics compatible; an impact-to-impact server interval is not automatically equivalent to a cast-to-cast client cooldown
- Account for variable travel time before rejecting an otherwise valid action because of a server-side interval check

## Authoritative Moving Targets

- Do not claim exact spatial hit validation when the server only has stale or client-driven target positions
- For exact server-side hit validation, make target movement server-authoritative or deterministically reproducible from shared time, seed, and movement parameters
- Until authoritative positions exist, describe coarse bounds, rate limits, and target caps as risk mitigation rather than complete hit validation
