# UE Edit Safety

Protect source encoding and keep patches small, verifiable, and complete.

## Encoding

- Use explicit UTF-8 reads for UE source files when possible, for example PowerShell `Get-Content -Encoding UTF8`
- If default shell output shows mojibake such as `灏`, `锛`, `涓`, `鎴`, first reread as UTF-8 before drawing conclusions
- Treat mojibake in shell output as a possible decoding problem, not proof that the source file is broken
- Do not "fix" Chinese comments or UI text based on wrongly decoded output
- Do not use Chinese comments or Chinese UI text as patch anchors
- Preserve existing file encoding and line endings as much as the tools allow
- After editing a file with Chinese comments or UI text, reread the touched area with UTF-8
- If the task must edit Chinese text, keep the exact project encoding and modify only the intended strings

## Patch Integrity

- Deliver chat patches as numbered hunks with stable ASCII anchors (function, class, member, or include names), and mark which hunks are load-bearing versus independent, so partial-application risk is visible
- Prefer whole-function replacement over many scattered hunks once more than two hunks touch the same function; scattered hunks are the main source of half-applied fatal states
- When a patch batch removes or renames an API, include the list of symbols that must have zero remaining references after application
- After the user applies a delivered patch batch, re-read the touched regions and run a residual-symbol sweep for removed APIs before any compile claim, delivery claim, or further review conclusion
- Treat "the user applied my patch" as unverified until the re-read confirms anchor placement and completeness

## Deletion Round Residue

- In deletion, revert, or slimming rounds, audit what the surviving code inherited from the deleted mechanism — registration timing, implicit sequencing, periodic coverage — and re-verify each against the new flow; attention naturally fixes on what is gone, while regressions hide in what remains
- Sweep residue mechanically per touched file: the deleted mechanism's vocabulary at zero hits including tests, modification markers balanced in pairs, includes with no remaining consumer removed, blank lines left where blocks were removed collapsed
- Compare the task's net change with its baseline, not only the previous patch. Remove whitespace churn introduced by this task; never restore a whole file to base if that would discard someone else's changes

## Shared Table And Import Edits

- Before an importer or bulk edit touches a shared registry, inspect the actual API's side effects, including global import state and each asset's source-file metadata. A successful return value alone does not prove rows or import sources survived
- Preflight the intended row type, keys, source paths, and expected edits; retain recoverable originals before destructive imports. Verify that existing rows and unrelated fields remain, each table still points to its own source, and a repeat run does not duplicate or overwrite unrelated data
- Keep one writer for each shared table and editor session. Save only after those checks pass; use the existing authoring tools rather than building a general recovery framework for a local import task
