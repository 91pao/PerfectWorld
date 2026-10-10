# 完美世界 计划总审官 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## autoplan

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Surfaces
taste decisions (close approaches, borderline scope, codex disagreements) at a final
approval gate. One command, fully reviewed plan out.
Use when asked to "auto review", "autoplan", "run all reviews", "review this plan
automatically", or "make the decisions for me".
Proactively suggest when the user has a plan file and wants to run the full review
gauntlet without answering 15-30 intermediate questions.

Voice triggers (speech-to-text aliases): "auto plan", "automatic review".

## plan-ceo-review

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Rethink the problem, find the 10-star product,
challenge premises, expand scope when it creates a better product. Four modes:
SCOPE EXPANSION (dream big), SELECTIVE EXPANSION (hold scope + cherry-pick
expansions), HOLD SCOPE (maximum rigor), SCOPE REDUCTION (strip to essentials).
Use when asked to "think bigger", "expand scope", "strategy review", "rethink this",
or "is this ambitious enough".
Proactively suggest when the user is questioning scope or ambition of a plan,
or when the plan feels like it could be thinking bigger.

## plan-eng-review

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Lock in the execution plan  architecture,
data flow, diagrams, edge cases, test coverage, performance. Walks through
issues interactively with opinionated recommendations. Use when asked to
"review the architecture", "engineering review", or "lock in the plan".
Proactively suggest when the user has a plan or design doc and is about to
start coding  to catch architecture issues before implementation.

Voice triggers (speech-to-text aliases): "tech review", "technical review", "plan engineering review".

## plan-design-review

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Rates each design dimension 0-10, explains what would make it a 10,
then fixes the plan to get there. Works in plan mode. For live site
visual audits, use perfectworld-design-review. Use when asked to "review the design plan"
or "design critique".
Proactively suggest when the user has a plan with UI/UX components that
should be reviewed before implementation.

## plan-devex-review

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Explores developer personas,
benchmarks against competitors, designs magical moments, and traces friction
points before scoring. Three modes: DX EXPANSION (competitive advantage),
DX POLISH (bulletproof every touchpoint), DX TRIAGE (critical gaps only).
Use when asked to "DX review", "developer experience audit", "devex review",
or "API design review".
Proactively suggest when the user has a plan for developer-facing products
(APIs, CLIs, SDKs, libraries, platforms, docs).

Voice triggers (speech-to-text aliases): "dx review", "developer experience review", "devex review", "devex audit", "API design review", "onboarding review".

## plan-tune

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Review which AskUserQuestion prompts fire across perfectworld skills, set per-question preferences
(never-ask / always-ask / ask-only-for-one-way), inspect the dual-track
profile (what you declared vs what your behavior suggests), and enable/disable
question tuning. Conversational interface  no CLI syntax required.

Use when asked to "tune questions", "stop asking me that", "too many questions",
"show my profile", "what questions have I been asked", "show my vibe",
"developer profile", or "turn off question tuning". 

Proactively suggest when the user says the same perfectworld question has come up before,
or when they explicitly override a recommendation for the Nth time.
