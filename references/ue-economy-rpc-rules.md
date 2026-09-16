# UE Economy And Transaction Rules

Use these rules for currencies, inventory, purchases, rewards, crafting, claims, and other stateful resource changes.

- First discover the project's authoritative resource, transaction, inventory, persistence, and notification APIs; do not assume names or storage locations
- Keep authoritative resource mutation on the trusted authority side in networked projects
- Validate identity, configuration, eligibility, current state, limits, affordability, capacity, and duplicate requests before committing
- Compute the intended cost and outcome before mutation so partial work is not mistaken for success
- Prefer the project's existing atomic transaction or commit mechanism when one exists
- Avoid deduct-first-and-refund-later designs unless the project has an explicit, tested compensation model
- Do not bypass domain APIs with low-level container mutations when those APIs enforce stacking, capacity, persistence, analytics, or notifications
- Update claim or completion state only at the success point required by the project's transaction semantics
- Make retry and duplicate-request behavior explicit for operations that can be replayed
- Persist and notify only after authoritative state reaches a valid committed result
- Log failures with the operation and non-sensitive identifiers needed to diagnose the rejected condition
- Review failure paths such as insufficient resources, capacity limits, invalid configuration, persistence failure, disconnects, and repeated requests

See `ue-client-server-boundary-rules.md` for network authority and RPC rules.
