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
