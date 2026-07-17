# UE Edit Safety

Protect source encoding and keep patches small.

- Use explicit UTF-8 reads for UE source files when possible, for example PowerShell `Get-Content -Encoding UTF8`
- If default shell output shows mojibake such as `灏`, `锛`, `涓`, `鎴`, first reread as UTF-8 before drawing conclusions
- Treat mojibake in shell output as a possible decoding problem, not proof that the source file is broken
- Do not "fix" Chinese comments or UI text based on wrongly decoded output
- Do not use Chinese comments or Chinese UI text as patch anchors
- Prefer patch anchors based on function names, class names, variable names, includes, braces, or nearby ASCII code
- Avoid whole-file rewrites; patch the smallest stable block
- Preserve existing file encoding and line endings as much as the tools allow
- After editing a file with Chinese comments or UI text, reread the touched area with UTF-8
- If the task must edit Chinese text, keep the exact project encoding and modify only the intended strings
