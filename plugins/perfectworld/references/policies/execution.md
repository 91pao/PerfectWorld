# PerfectWorld Execution and Verification Policy

The short `Iteration and Delivery Contract` in every active skill is authoritative. This reference provides detail for ambiguous cases and should not be loaded during routine work.

## Verification scope

- `ITERATION` is the default for feature additions, local edits, bug fixes, completed subtasks, and ordinary goal-mode rounds.
- `LOW` risk verifies the changed unit or exact browser path. `MEDIUM` adds the affected package and direct integrations. `HIGH` adds affected dependency boundaries for shared contracts, schemas, auth, security, migrations, and common infrastructure.
- Risk broadens focused verification but never authorizes a full repository suite during iteration.
- Reuse previous checks until relevant code, configuration, dependencies, generated artifacts, or environment changes make them stale.
- Use fail-fast order and focused reruns while fixing failures.
- `FINAL_DELIVERY` requires explicit final-version, release, full-test, or final-acceptance intent. Run full checks after implementation stabilizes. New feature work returns the project to `ITERATION` before another final pass.

## Context and tools

- Search for symbols, files, and headings before reading; open the smallest useful ranges and do not reread unchanged files.
- Start with the active skill's mission and capabilities. Search one on-demand playbook section only when deeper methodology is needed; never bulk-load inherited references.
- Cache project facts such as test commands, package boundaries, run commands, URLs, and architecture until related configuration changes.
- Summarize successful commands with scope and result. Expand logs, traces, screenshots, and diagnostics only for failures or decisions.
- Update plans by delta instead of repeating completed history.
- Use one primary role per round. Secondary perspectives are short checklists unless the bottleneck genuinely transfers ownership.
- Use multiple agents only for independent tasks where parallel execution clearly exceeds coordination cost.

## Verification ledger

Keep a compact record of changed scope, risk level, checks passed, checks intentionally deferred, and the changes that would invalidate earlier evidence. Focused verification supports only focused confidence; full-project confidence requires final-delivery validation.
