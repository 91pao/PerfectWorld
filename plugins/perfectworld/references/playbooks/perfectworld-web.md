# 完美世界 Web 操作员 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## browse

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Navigate any URL, interact with
elements, verify page state, diff before/after actions, take annotated screenshots, check
responsive layouts, test forms and uploads, handle dialogs, and assert element states.
~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a
user flow, or file a bug with evidence. Use when asked to "open in browser", "test the
site", "take a screenshot", or "dogfood this".

## open-perfectworld-browser

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Opens a visible browser window where you can watch every action in real time.
The sidebar shows a live activity feed and chat. Anti-bot stealth built in.
Use when asked to "open perfectworld browser", "launch browser", "connect chrome",
"open chrome", "real browser", "launch chrome", "side panel", or "control my browser".

Voice triggers (speech-to-text aliases): "show me the browser".

## setup-browser-cookies

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Opens an interactive picker UI where you select which cookie domains to import.
Use before QA testing authenticated pages. Use when asked to "import cookies",
"login to the site", or "authenticate the browser".

## scrape

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

First call on a new intent prototypes the flow
via $B primitives and returns JSON. Subsequent calls on a matching intent
route to a codified browser-skill and return in ~200ms. Read-only  for
mutating flows (form fills, clicks, submissions), use perfectworld-automate.
Use when asked to "scrape", "get data from", "pull", "extract from", or
"what's on" a page.
