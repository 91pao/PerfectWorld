# Route Precedent Gate

Use this gate at design time (ue-draft) and as an implementation backstop (ue-implement) whenever a plan is about to create a new mechanism, or an existing constraint blocks the obvious path.

Incident shape: a budget reservation window could not cover a long delivery presentation. The correct route was to read how the sibling source already solved the same problem (commit early, pass the full execution window as a parameter — natively supported by the framework). The actual route was a self-invented renewal + delayed-commit parallel mechanism, which cost implement-review-rework cycles and was finally resolved by the owner in one sentence. The constraint "do not modify other people's code" was never the problem — its silent escalation into "do not read other people's code" was. Talking to the path looks slow; building a parallel path looks fast; fast first, expensive after, and the further a wrong route goes the harder it turns back.

## Fork Detection

Stop and run this gate on any of these signals:

- About to create: class / manager / wrapper / helper / timer / renewal / retry queue / state machine / cache / new field-and-flow
- Language signals: "this constraint blocks us", "the framework does not support it", "touching their code is too messy", "work around it first", "we maintain our own copy"
- Structural signals: the design contains a mechanism whose only reason to exist is to route around a constraint (periodic keep-alive, "delay X then Y")

## Three Routes

- A Reuse: an existing capability solves it with different parameters or usage
- B Align: copy the sequencing of a sibling implementation that already crossed this river — same caller category, same subsystem, same problem class
- C Parallel mechanism: last resort, and it must carry proof

## Precedent Search (mechanical, never from memory)

1. Find siblings: other callers of the same problem — same source kind, same tenant, same subsystem, or whoever touched this concern in recent commits
2. Read their sequencing, not their interface: who runs first, who owns the window, who owns the lifecycle
3. Record the search terms; zero hits is itself evidence and must be logged

## Required Artifact: Precedent Table

| Need | Existing capability (path:line) | How it solves it | Route | Proof if C |
| --- | --- | --- | --- | --- |

The proof standard for a C row is "searched X (path), does not fit because Y (code fact)". "Did not search", "afraid of touching their code", and "no time to ask" are not proof.

## Owner Alignment (prerequisite for C)

When the design touches a domain another person maintains, choosing C requires producing a one-line question for the owner, handed to the user to forward, before any code is written. The assistant does not send messages; it must still put the fork on the table. The inverse of "he never told us" is "we never asked him".

## Layering

- Design time (this gate): a plan without a precedent table is not delivered, not reviewed
- Implementation time: any "create a new mechanism" action returns to this gate; discovering mid-implementation that a constraint differs from what the plan assumed means going back to fork detection, not inventing locally
- Review time: the interruption matrix's mechanism-uniqueness invariant backstops this gate — a second mechanism collecting the same resource in one domain is a red cell unless the plan carries a precedent table

## Boundary

- When the search is logged as zero-hit and the owner has no stated intent, C is the correct choice; this gate only demands complete proof, it does not forbid C
- Precedent that lives only in a person's head is invisible to mechanical search — that is exactly why the owner-alignment layer exists; the two layers together are the full coverage
