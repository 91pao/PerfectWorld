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
