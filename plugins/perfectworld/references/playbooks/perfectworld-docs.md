# 完美世界 文档工程师 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## document-generate

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Uses the Diataxis framework (tutorial / how-to / reference / explanation) to produce
complete, structured documentation. Can be invoked standalone or called by
perfectworld-document-release when it finds coverage gaps. Use when asked to "write docs",
"generate documentation", "document this feature", "create a tutorial", or
"explain this module".

## document-release

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Reads all project docs, cross-references the
diff, builds a Diataxis coverage map (reference/how-to/tutorial/explanation),
updates README/ARCHITECTURE/CONTRIBUTING/AGENTS.md or repository guidance to match what shipped,
detects architecture diagram drift, polishes CHANGELOG voice with a sell-test
rubric, cleans up TODOS, and optionally bumps VERSION. Surfaces documentation
debt in the PR body. Use when asked to "update the docs", "sync documentation",
or "post-ship docs". Proactively suggest after a PR is merged or code is shipped.
