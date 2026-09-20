# Deletion Round Audit

Protocol for rounds whose deliverable is removing a mechanism, reverting a workaround, or slimming a refactor — where the failure mode inverts: success is measured by what stops existing.

Incident shapes: mechanism blocks deleted cleanly but leaving orphaned marker pairs, stale comments describing the deleted behavior, an unused include, blank-line-only files lingering in the commit; and surviving code that silently depended on a guarantee the deleted mechanism used to provide.

## Survivor Assumption Audit (the core step)

For every surviving call site that used to interact with the deleted mechanism, ask: which guarantee did it inherit — registration timing, implicit sequencing, periodic coverage, ordering side effects? Re-verify each against the new flow. Deletion-round attention naturally fixes on "is it gone"; the surviving code is where regressions hide.

## Residue Sweep (mechanical, per touched file)

- Comments: grep the deleted mechanism's vocabulary (renewal, keep-alive, delayed commit, its reason names, its delegate and field names) — zero hits required, tests included
- Modification markers: every begin/end pair balanced; a pair whose content vanished takes its markers with it
- Includes: an include whose only consumer died goes too; verify zero usages (including handle types) before removing
- Whitespace: run the diff whitespace check; collapse blank lines left where blocks were removed

## Baseline Diff Technique

Judge the round against the ticket's base commit, not against the previous working state: net-zero files must fall out of the diff entirely. A file whose net change is one or two blank lines is residue masquerading as a touched file — restore it to base so it leaves the change surface.

## Precedent Note

If the deletion reverts a route that a sibling already solved differently, run ue-route-precedent-gate.md before writing the replacement: deleting the wrong mechanism and re-inventing it differently is the same fork one round later.
