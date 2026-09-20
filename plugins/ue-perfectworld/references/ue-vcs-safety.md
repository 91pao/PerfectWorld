# Version Control Round-trip Safety

Rules for git operations around a change session. Not a git tutorial — the failure class these rules close is silent work loss and history damage from tool round-trips.

Incident shapes: a GUI client stashing uncommitted work on branch switch and restoring it with lines eaten (a comment, half a marker pair); a squash commit carrying blank-line-only files that should have fallen out of the diff; a post-rewrite push rejected as non-fast-forward and the "update first" suggestion pulling the replaced commit back in as a merge.

## Hard Rules

- Commit before any rebase, branch switch, or history rewrite. Uncommitted work on the tree is the precondition of every loss incident
- After any GUI round-trip (switch, stash apply, reset), diff the working tree against a known-good snapshot (stash commit id, pre-operation commit) before believing the tree. Expect eaten lines: comments, marker halves, blank lines. Marker-pair balance is a cheap tripwire
- After history rewrite, pushing requires force; use force-with-lease. When the client suggests "update/pull before push" after a rewrite, that suggestion re-imports the replaced history — decline it
- Read server hook errors verbatim before rewording a commit message: push-rejected messages state the enforced format (example shape: the URL must sit alone on the second line). Match it instead of guessing
- Prefer restoring one file from a snapshot over re-typing it: `git restore --source=<snapshot> --staged --worktree -- <file>` reproduces the known-good bytes exactly

## Diff Honesty

- A "no changes" claim requires an empty `git diff <base>` against the ticket base, not against the last working state
- Diff shapes worth checking before delivery: files whose entire change is whitespace (restore to base); a renamed local next to a same-named file-scope constant in another file of the same unity blob (shadowing warning)

## Boundary

This reference governs safety, not workflow choice (rebase versus merge policy, branch naming) — those belong to the team's own conventions.
