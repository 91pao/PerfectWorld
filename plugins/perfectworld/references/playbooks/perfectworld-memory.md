# 完美世界 项目大脑管理员 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## learn

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Review, search, prune, and export what perfectworld
has learned across sessions. Use when asked to "what have we learned",
"show learnings", "prune stale learnings", or "export learnings".
Proactively suggest when the user asks about past patterns or wonders
"didn't we fix this before?"

## setup-pbrain

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

One command from zero to "pbrain is running, and this agent
can call it." Use when: "setup pbrain", "connect pbrain", "start
pbrain", "install pbrain", "configure pbrain for this machine".

## sync-pbrain

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

probing, native code-surface registration, capability checks,
and a verdict block. Re-runnable, idempotent. Use when: "sync pbrain",
"refresh pbrain", "re-index this repo", "pbrain search isn't finding
things".

## context-save

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Captures git state, decisions made, and remaining work
so any future session can pick up without losing a beat.
Use when asked to "save progress", "save state", "context save", or
"save my work". Pair with perfectworld-context-restore to resume later.
Formerly perfectworld-checkpoint  renamed because Codex treats perfectworld-checkpoint as a
native rewind alias in current environments, which was shadowing this skill.

## context-restore

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Loads the most recent
saved state (across all branches by default) so you can pick up where you
left off  even across Conductor workspace handoffs.
Use when asked to "resume", "restore context", "where was I", or
"pick up where I left off". Pair with perfectworld-context-save.
Formerly perfectworld-checkpoint resume  renamed because Codex treats perfectworld-checkpoint
as a native rewind alias in current environments.
