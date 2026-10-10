# 完美世界 设计总监 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## design-consultation

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Creates DESIGN.md as your project's design source
of truth. For existing sites, use perfectworld-plan-design-review to infer the system instead.
Use when asked to "design system", "brand guidelines", or "create DESIGN.md".
Proactively suggest when starting a new project's UI with no existing
design system or DESIGN.md.

## design-shotgun

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Standalone design exploration you can
run anytime. Use when: "explore designs", "show me options", "design variants",
"visual brainstorm", or "I don't like how this looks".
Proactively suggest when the user describes a UI feature but hasn't seen
what it could look like.

## design-review

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Iteratively fixes issues
in source code, committing each fix atomically and re-verifying with before/after
screenshots. For plan-mode design review (before implementation), use perfectworld-plan-design-review.
Use when asked to "audit the design", "visual QA", "check if it looks good", or "design polish".
Proactively suggest when the user mentions visual inconsistencies or
wants to polish the look of a live site.

## design-html

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Works with approved mockups from perfectworld-design-shotgun, CEO plans from perfectworld-plan-ceo-review,
design review context from perfectworld-plan-design-review, or from scratch with a user
description. Text actually reflows, heights are computed, layouts are dynamic.
30KB overhead, zero deps. Smart API routing: picks the right Pretext patterns
for each design type. Use when: "finalize this design", "turn this into HTML",
"build me a page", "implement this design", or after any planning skill.
Proactively suggest when user has approved a design or has a plan ready.

Voice triggers (speech-to-text aliases): "build the design", "code the mockup", "make it real".
