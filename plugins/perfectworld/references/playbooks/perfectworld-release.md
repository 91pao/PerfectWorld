# 完美世界 发布总管 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## ship

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Use when asked to "ship", "deploy",
"push to main", "create a PR", "merge and push", or "get it deployed".
Proactively use this skill (do NOT push/PR directly) when the user says code
is ready, asks about deploying, wants to push code up, or asks to create a PR.

## setup-deploy

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Detects your deploy
platform (Fly.io, Render, Vercel, Netlify, Heroku, GitHub Actions, custom),
production URL, health check endpoints, and deploy status commands. Writes
the configuration to AGENTS.md or repository guidance so all future deploys are automatic.
Use when: "setup deploy", "configure deployment", "set up land-and-deploy",
"how do I deploy with perfectworld", "add deploy config".

## land-and-deploy

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Merges the PR, waits for CI and deploy,
verifies production health via canary checks. Takes over after perfectworld-ship
creates the PR. Use when: "merge", "land", "deploy", "merge and verify",
"land it", "ship it to production".

## canary

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Watches the live app for console errors,
performance regressions, and page failures using the browse daemon. Takes
periodic screenshots, compares against pre-deploy baselines, and alerts
on anomalies. Use when: "monitor deploy", "canary", "post-deploy check",
"watch production", "verify deploy".

## landing-report

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Shows which VERSION slots
are currently claimed by open PRs, which sibling Conductor workspaces have
WIP work likely to ship soon, and what slot perfectworld-ship would pick next. No
mutations  just a snapshot. Use when asked to "landing report", "what's in
the queue", "show me open PRs", or "which version do I claim next".

# perfectworld-landing-report  Version Queue Dashboard
