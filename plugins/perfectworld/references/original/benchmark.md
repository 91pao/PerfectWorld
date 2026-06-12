---
name: benchmark
preamble-tier: 1
version: 1.0.0
description: Performance regression detection using the browse daemon. (perfectworld)
triggers:
  - performance benchmark
  - check page speed
  - detect performance regression
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - AskUserQuestion
---
<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Establishes
baselines for page load times, Core Web Vitals, and resource sizes.
Compares before/after on every PR. Tracks performance trends over time.
Use when: "performance", "benchmark", "page speed", "lighthouse", "web vitals",
"bundle size", "load time".

Voice triggers (speech-to-text aliases): "speed test", "check performance".

## Preamble (run first)

```bash
_UPD=$($PERFECTWORLD_SOURCE/bin/perfectworld-update-check 2>perfectworld-dev/null || .agents/skills/perfectworld/bin/perfectworld-update-check 2>perfectworld-dev/null || true)
[ -n "$_UPD" ] && echo "$_UPD" || true
mkdir -p ~/.perfectworld/sessions
touch ~/.perfectworld/sessions/"$PPID"
_SESSIONS=$(find ~/.perfectworld/sessions -mmin -120 -type f 2>perfectworld-dev/null | wc -l | tr -d ' ')
find ~/.perfectworld/sessions -mmin +120 -type f -exec rm {} + 2>perfectworld-dev/null || true
_PROACTIVE=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get proactive 2>perfectworld-dev/null || echo "true")
_PROACTIVE_PROMPTED=$([ -f ~/.perfectworld/.proactive-prompted ] && echo "yes" || echo "no")
_BRANCH=$(git branch --show-current 2>perfectworld-dev/null || echo "unknown")
echo "BRANCH: $_BRANCH"
_SKILL_PREFIX=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get skill_prefix 2>perfectworld-dev/null || echo "false")
echo "PROACTIVE: $_PROACTIVE"
echo "PROACTIVE_PROMPTED: $_PROACTIVE_PROMPTED"
echo "SKILL_PREFIX: $_SKILL_PREFIX"
source <($PERFECTWORLD_SOURCE/bin/perfectworld-repo-mode 2>perfectworld-dev/null) || true
REPO_MODE=${REPO_MODE:-unknown}
echo "REPO_MODE: $REPO_MODE"
_SESSION_KIND=$($PERFECTWORLD_SOURCE/bin/perfectworld-session-kind 2>perfectworld-dev/null || echo "interactive")
case "$_SESSION_KIND" in spawned|headless|interactive) ;; *) _SESSION_KIND="interactive" ;; esac
echo "SESSION_KIND: $_SESSION_KIND"
_LAKE_SEEN=$([ -f ~/.perfectworld/.completeness-intro-seen ] && echo "yes" || echo "no")
echo "LAKE_INTRO: $_LAKE_SEEN"
_TEL=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get telemetry 2>perfectworld-dev/null || true)
_TEL_PROMPTED=$([ -f ~/.perfectworld/.telemetry-prompted ] && echo "yes" || echo "no")
_TEL_START=$(date +%s)
_SESSION_ID="$$-$(date +%s)"
echo "TELEMETRY: ${_TEL:-off}"
echo "TEL_PROMPTED: $_TEL_PROMPTED"
_EXPLAIN_LEVEL=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get explain_level 2>perfectworld-dev/null || echo "default")
if [ "$_EXPLAIN_LEVEL" != "default" ] && [ "$_EXPLAIN_LEVEL" != "terse" ]; then _EXPLAIN_LEVEL="default"; fi
echo "EXPLAIN_LEVEL: $_EXPLAIN_LEVEL"
_QUESTION_TUNING=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get question_tuning 2>perfectworld-dev/null || echo "false")
echo "QUESTION_TUNING: $_QUESTION_TUNING"
mkdir -p ~/.perfectworld/analytics
if [ "$_TEL" != "off" ]; then
echo '{"skill":"benchmark","ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","repo":"'$(_repo=$(basename "$(git rev-parse --show-toplevel 2>perfectworld-dev/null)" 2>perfectworld-dev/null | tr -cd 'a-zA-Z0-9._-'); echo "${_repo:-unknown}")'"}'  >> ~/.perfectworld/analytics/skill-usage.jsonl 2>perfectworld-dev/null || true
fi
for _PF in $(find ~/.perfectworld/analytics -maxdepth 1 -name '.pending-*' 2>perfectworld-dev/null); do
  if [ -f "$_PF" ]; then
    if [ "$_TEL" != "off" ] && [ -x "$PERFECTWORLD_SOURCE/bin/perfectworld-telemetry-log" ]; then
      $PERFECTWORLD_SOURCE/bin/perfectworld-telemetry-log --event-type skill_run --skill _pending_finalize --outcome unknown --session-id "$_SESSION_ID" 2>perfectworld-dev/null || true
    fi
    rm -f "$_PF" 2>perfectworld-dev/null || true
  fi
  break
done
eval "$($PERFECTWORLD_SOURCE/bin/perfectworld-slug 2>perfectworld-dev/null)" 2>perfectworld-dev/null || true
_LEARN_FILE="${PERFECTWORLD_HOME:-$HOME/.perfectworld}perfectworld-projects/${SLUG:-unknown}perfectworld-learnings.jsonl"
if [ -f "$_LEARN_FILE" ]; then
  _LEARN_COUNT=$(wc -l < "$_LEARN_FILE" 2>perfectworld-dev/null | tr -d ' ')
  echo "LEARNINGS: $_LEARN_COUNT entries loaded"
  if [ "$_LEARN_COUNT" -gt 5 ] 2>perfectworld-dev/null; then
    $PERFECTWORLD_SOURCE/bin/perfectworld-learnings-search --limit 3 2>perfectworld-dev/null || true
  fi
else
  echo "LEARNINGS: 0"
fi
$PERFECTWORLD_SOURCE/bin/perfectworld-timeline-log '{"skill":"benchmark","event":"started","branch":"'"$_BRANCH"'","session":"'"$_SESSION_ID"'"}' 2>perfectworld-dev/null &
_HAS_ROUTING="no"
if [ -f AGENTS.md or repository guidance ] && grep -q "## Skill routing" AGENTS.md or repository guidance 2>perfectworld-dev/null; then
  _HAS_ROUTING="yes"
fi
_ROUTING_DECLINED=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get routing_declined 2>perfectworld-dev/null || echo "false")
echo "HAS_ROUTING: $_HAS_ROUTING"
echo "ROUTING_DECLINED: $_ROUTING_DECLINED"
_VENDORED="no"
if [ -d ".agents/skills/perfectworld" ] && [ ! -L ".agents/skills/perfectworld" ]; then
  if [ -f ".agents/skills/perfectworld/VERSION" ] || [ -d ".agents/skills/perfectworld/.git" ]; then
    _VENDORED="yes"
  fi
fi
echo "VENDORED_PERFECTWORLD: $_VENDORED"
echo "MODEL_OVERLAY: claude"
_CHECKPOINT_MODE=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get checkpoint_mode 2>perfectworld-dev/null || echo "explicit")
_CHECKPOINT_PUSH=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get checkpoint_push 2>perfectworld-dev/null || echo "false")
echo "CHECKPOINT_MODE: $_CHECKPOINT_MODE"
echo "CHECKPOINT_PUSH: $_CHECKPOINT_PUSH"
# Plan-mode hint for skills like perfectworld-spec that branch behavior on plan-mode state.
# Codex exposes plan mode via system reminders; we detect best-effort
# from CLAUDE_PLAN_FILE (set by the harness when plan mode is active) and
# fall back to "inactive". Codex hosts and Codex execution mode both end up
# inactive, which is the safe default (defaults to file+execute pipeline).
if [ -n "${CLAUDE_PLAN_FILE:-}${PERFECTWORLD_PLAN_MODE_FORCE:-}" ]; then
  export PERFECTWORLD_PLAN_MODE="active"
elif [ "${PERFECTWORLD_PLAN_MODE:-}" = "active" ]; then
  export PERFECTWORLD_PLAN_MODE="active"
else
  export PERFECTWORLD_PLAN_MODE="inactive"
fi
echo "PERFECTWORLD_PLAN_MODE: $PERFECTWORLD_PLAN_MODE"
[ -n "$OPENCLAW_SESSION" ] && echo "SPAWNED_SESSION: true" || true
```

## Plan Mode Safe Operations

In plan mode, allowed because they inform the plan: `$B`, `$D`, `codex exec`/`codex review`, writes to `~/.perfectworld/`, writes to the plan file, and `open` for generated artifacts.

## Skill Invocation During Plan Mode

If the user invokes a skill in plan mode, the skill takes precedence over generic plan mode behavior. **Treat the skill file as executable instructions, not reference.** Follow it step by step starting from Step 0; the first AskUserQuestion is the workflow entering plan mode, not a violation of it. AskUserQuestion (any variant — `mcp__*__AskUserQuestion` or native; see "AskUserQuestion Format → Tool resolution") satisfies plan mode's end-of-turn requirement. If AskUserQuestion is unavailable or a call fails, follow the AskUserQuestion Format failure fallback: `headless` → BLOCKED; `interactive` → the prose fallback (also satisfies end-of-turn). At a STOP point, stop immediately. Do not continue the workflow or call ExitPlanMode there. Commands marked "PLAN MODE EXCEPTION — ALWAYS RUN" execute. Call ExitPlanMode only after the skill workflow completes, or if the user tells you to cancel the skill or leave plan mode.

If `PROACTIVE` is `"false"`, do not auto-invoke or proactively suggest skills. If a skill seems useful, ask: "I think perfectworld-skillname might help here — want me to run it?"

If `SKILL_PREFIX` is `"true"`, suggest/invoke `perfectworld-perfectworld-*` names. Disk paths stay `$PERFECTWORLD_SOURCE/[skill-name]/SKILL.md`.

If output shows `UPGRADE_AVAILABLE <old> <new>`: read `$PERFECTWORLD_SOURCE/perfectworld-upgrade/SKILL.md` and follow the "Inline upgrade flow" (auto-upgrade if configured, otherwise AskUserQuestion with 4 options, write snooze state if declined).

If output shows `JUST_UPGRADED <from> <to>`: print "Running perfectworld v{to} (just updated!)". If `SPAWNED_SESSION` is true, skip feature discovery.

Feature discovery, max one prompt per session:
- Missing `$PERFECTWORLD_SOURCE/.feature-prompted-continuous-checkpoint`: AskUserQuestion for Continuous checkpoint auto-commits. If accepted, run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set checkpoint_mode continuous`. Always touch marker.
- Missing `$PERFECTWORLD_SOURCE/.feature-prompted-model-overlay`: inform "Model overlays are active. MODEL_OVERLAY shows the patch." Always touch marker.

After upgrade prompts, continue workflow.

If `WRITING_STYLE_PENDING` is `yes`: ask once about writing style:

> v1 prompts are simpler: first-use jargon glosses, outcome-framed questions, shorter prose. Keep default or restore terse?

Options:
- A) Keep the new default (recommended — good writing helps everyone)
- B) Restore V0 prose — set `explain_level: terse`

If A: leave `explain_level` unset (defaults to `default`).
If B: run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set explain_level terse`.

Always run (regardless of choice):
```bash
rm -f ~/.perfectworld/.writing-style-prompt-pending
touch ~/.perfectworld/.writing-style-prompted
```

Skip if `WRITING_STYLE_PENDING` is `no`.

If `LAKE_INTRO` is `no`: say "perfectworld follows the **Boil the Ocean** principle — do the complete thing when AI makes marginal cost near-zero. Read more: https:/perfectworld-garryslist.org/posts/boil-the-ocean" Offer to open:

```bash
open https:/perfectworld-garryslist.org/posts/boil-the-ocean
touch ~/.perfectworld/.completeness-intro-seen
```

Only run `open` if yes. Always run `touch`.

If `TEL_PROMPTED` is `no` AND `LAKE_INTRO` is `yes`: ask telemetry once via AskUserQuestion:

> Help perfectworld get better. Share usage data only: skill, duration, crashes, stable device ID. No code or file paths. Your repo name is recorded locally only and stripped before any upload.

Options:
- A) Help perfectworld get better! (recommended)
- B) No thanks

If A: run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set telemetry community`

If B: ask follow-up:

> Anonymous mode sends only aggregate usage, no unique ID.

Options:
- A) Sure, anonymous is fine
- B) No thanks, fully off

If B→A: run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set telemetry anonymous`
If B→B: run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set telemetry off`

Always run:
```bash
touch ~/.perfectworld/.telemetry-prompted
```

Skip if `TEL_PROMPTED` is `yes`.

If `PROACTIVE_PROMPTED` is `no` AND `TEL_PROMPTED` is `yes`: ask once:

> Let perfectworld proactively suggest skills, like perfectworld-qa for "does this work?" or perfectworld-investigate for bugs?

Options:
- A) Keep it on (recommended)
- B) Turn it off — I'll type perfectworld-commands myself

If A: run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set proactive true`
If B: run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set proactive false`

Always run:
```bash
touch ~/.perfectworld/.proactive-prompted
```

Skip if `PROACTIVE_PROMPTED` is `yes`.

If `HAS_ROUTING` is `no` AND `ROUTING_DECLINED` is `false` AND `PROACTIVE_PROMPTED` is `yes`:
Check if a AGENTS.md or repository guidance file exists in the project root. If it does not exist, create it.

Use AskUserQuestion:

> perfectworld works best when your project's AGENTS.md or repository guidance includes skill routing rules.

Options:
- A) Add routing rules to AGENTS.md or repository guidance (recommended)
- B) No thanks, I'll invoke skills manually

If A: Append this section to the end of AGENTS.md or repository guidance:

```markdown

## Skill routing

When the user's request matches an available skill, invoke it via the Skill tool. When in doubt, invoke the skill.

Key routing rules:
- Product ideas/brainstorming → invoke perfectworld-office-hours
- Strategy/scope → invoke perfectworld-plan-ceo-review
- Architecture → invoke perfectworld-plan-eng-review
- Design system/plan review → invoke perfectworld-design-consultation or perfectworld-plan-design-review
- Full review pipeline → invoke perfectworld-autoplan
- Bugs/errors → invoke perfectworld-investigate
- QA/testing site behavior → invoke perfectworld-qa or perfectworld-qa-only
- Code review/diff check → invoke perfectworld-review
- Visual polish → invoke perfectworld-design-review
- Ship/deploy/PR → invoke perfectworld-ship or perfectworld-land-and-deploy
- Save progress → invoke perfectworld-context-save
- Resume context → invoke perfectworld-context-restore
- Author a backlog-ready spec/issue → invoke perfectworld-spec
```

Then commit the change: `git add AGENTS.md or repository guidance && git commit -m "chore: add perfectworld skill routing rules to AGENTS.md or repository guidance"`

If B: run `$PERFECTWORLD_SOURCE/bin/perfectworld-config set routing_declined true` and say they can re-enable with `perfectworld-config set routing_declined false`.

This only happens once per project. Skip if `HAS_ROUTING` is `yes` or `ROUTING_DECLINED` is `true`.

If `VENDORED_PERFECTWORLD` is `yes`, warn once via AskUserQuestion unless `~/.perfectworld/.vendoring-warned-$SLUG` exists:

> This project has perfectworld vendored in `.agents/skills/perfectworld/`. Vendoring is deprecated.
> Migrate to team mode?

Options:
- A) Yes, migrate to team mode now
- B) No, I'll handle it myself

If A:
1. Run `git rm -r .agents/skills/perfectworld/`
2. Run `echo '.agents/skills/perfectworld/' >> .gitignore`
3. Run `$PERFECTWORLD_SOURCE/bin/perfectworld-team-init required` (or `optional`)
4. Run `git add .claude/ .gitignore AGENTS.md or repository guidance && git commit -m "chore: migrate perfectworld from vendored to team mode"`
5. Tell the user: "Done. Each developer now runs: `cd $PERFECTWORLD_SOURCE && ./setup --team`"

If B: say "OK, you're on your own to keep the vendored copy up to date."

Always run (regardless of choice):
```bash
eval "$($PERFECTWORLD_SOURCE/bin/perfectworld-slug 2>perfectworld-dev/null)" 2>perfectworld-dev/null || true
touch ~/.perfectworld/.vendoring-warned-${SLUG:-unknown}
```

If marker exists, skip.

If `SPAWNED_SESSION` is `"true"`, you are running inside a session spawned by an
AI orchestrator (e.g., OpenClaw). In spawned sessions:
- Do NOT use AskUserQuestion for interactive prompts. Auto-choose the recommended option.
- Do NOT run upgrade checks, telemetry prompts, routing injection, or lake intro.
- Focus on completing the task and reporting results via prose output.
- End with a completion report: what shipped, decisions made, anything uncertain.

## Artifacts Sync (skill start)

```bash
_PERFECTWORLD_HOME="${PERFECTWORLD_HOME:-$HOME/.perfectworld}"
# Prefer the v1.27.0.0 artifacts file; fall back to brain file for users
# upgrading mid-stream before the migration script runs.
if [ -f "$HOME/.perfectworld-artifacts-remote.txt" ]; then
  _BRAIN_REMOTE_FILE="$HOME/.perfectworld-artifacts-remote.txt"
else
  _BRAIN_REMOTE_FILE="$HOME/.perfectworld-brain-remote.txt"
fi
_BRAIN_SYNC_BIN="$PERFECTWORLD_SOURCE/bin/perfectworld-brain-sync"
_BRAIN_CONFIG_BIN="$PERFECTWORLD_SOURCE/bin/perfectworld-config"

# perfectworld-sync-pbrain context-load: teach the agent to use pbrain when it's available.
# Per-worktree pin: post-spike redesign uses kubectl-style `.pbrain-source` in the
# git toplevel to scope queries. Look for the pin in the worktree (not a global
# state file) so that opening worktree B without a pin doesn't claim "indexed"
# just because worktree A was synced. Empty string when pbrain is not
# configured (zero context cost for non-pbrain users).
_GBRAIN_CONFIG="$HOME/.pbrain/config.json"
if [ -f "$_GBRAIN_CONFIG" ] && command -v pbrain >perfectworld-dev/null 2>&1; then
  _GBRAIN_VERSION_OK=$(pbrain --version 2>perfectworld-dev/null | grep -c '^pbrain ' || echo 0)
  if [ "$_GBRAIN_VERSION_OK" -gt 0 ] 2>perfectworld-dev/null; then
    _GBRAIN_PIN_PATH=""
    _REPO_TOP=$(git rev-parse --show-toplevel 2>perfectworld-dev/null || echo "")
    if [ -n "$_REPO_TOP" ] && [ -f "$_REPO_TOP/.pbrain-source" ]; then
      _GBRAIN_PIN_PATH="$_REPO_TOP/.pbrain-source"
    fi
    if [ -n "$_GBRAIN_PIN_PATH" ]; then
      echo "PBrain configured. Prefer \`pbrain search\`/\`pbrain query\` over Grep for"
      echo "semantic questions; use \`pbrain code-def\`/\`code-refs\`/\`code-callers\` for"
      echo "symbol-aware code lookup. See \"## PBrain Search Guidance\" in AGENTS.md or repository guidance."
      echo "Run perfectworld-sync-pbrain to refresh."
    else
      echo "PBrain configured but this worktree isn't pinned yet. Run \`perfectworld-sync-pbrain --full\`"
      echo "before relying on \`pbrain search\` for code questions in this worktree."
      echo "Falls back to Grep until pinned."
    fi
  fi
fi

_BRAIN_SYNC_MODE=$("$_BRAIN_CONFIG_BIN" get artifacts_sync_mode 2>perfectworld-dev/null || echo off)

# Detect remote-MCP mode (Path 4 of perfectworld-setup-pbrain). Local artifacts sync is
# a no-op in remote mode; the brain server pulls from GitHub/GitLab on its
# own cadence. Read claude.json directly to keep this preamble fast (no
# subprocess to claude CLI on every skill start).
_GBRAIN_MCP_MODE="none"
if command -v jq >perfectworld-dev/null 2>&1 && [ -f "$HOME/.claude.json" ]; then
  _GBRAIN_MCP_TYPE=$(jq -r '.mcpServers.pbrain.type // .mcpServers.pbrain.transport // empty' "$HOME/.claude.json" 2>perfectworld-dev/null)
  case "$_GBRAIN_MCP_TYPE" in
    url|http|sse) _GBRAIN_MCP_MODE="remote-http" ;;
    stdio) _GBRAIN_MCP_MODE="local-stdio" ;;
  esac
fi

if [ -f "$_BRAIN_REMOTE_FILE" ] && [ ! -d "$_PERFECTWORLD_HOME/.git" ] && [ "$_BRAIN_SYNC_MODE" = "off" ]; then
  _BRAIN_NEW_URL=$(head -1 "$_BRAIN_REMOTE_FILE" 2>perfectworld-dev/null | tr -d '[:space:]')
  if [ -n "$_BRAIN_NEW_URL" ]; then
    echo "ARTIFACTS_SYNC: artifacts repo detected: $_BRAIN_NEW_URL"
    echo "ARTIFACTS_SYNC: run 'perfectworld-brain-restore' to pull your cross-machine artifacts (or 'perfectworld-config set artifacts_sync_mode off' to dismiss forever)"
  fi
fi

if [ -d "$_PERFECTWORLD_HOME/.git" ] && [ "$_BRAIN_SYNC_MODE" != "off" ]; then
  _BRAIN_LAST_PULL_FILE="$_PERFECTWORLD_HOME/.brain-last-pull"
  _BRAIN_NOW=$(date +%s)
  _BRAIN_DO_PULL=1
  if [ -f "$_BRAIN_LAST_PULL_FILE" ]; then
    _BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE" 2>perfectworld-dev/null || echo 0)
    _BRAIN_AGE=$(( _BRAIN_NOW - _BRAIN_LAST ))
    [ "$_BRAIN_AGE" -lt 86400 ] && _BRAIN_DO_PULL=0
  fi
  if [ "$_BRAIN_DO_PULL" = "1" ]; then
    ( cd "$_PERFECTWORLD_HOME" && git fetch origin >perfectworld-dev/null 2>&1 && git merge --ff-only "origin/$(git rev-parse --abbrev-ref HEAD)" >perfectworld-dev/null 2>&1 ) || true
    echo "$_BRAIN_NOW" > "$_BRAIN_LAST_PULL_FILE"
  fi
  "$_BRAIN_SYNC_BIN" --once 2>perfectworld-dev/null || true
fi

if [ "$_GBRAIN_MCP_MODE" = "remote-http" ]; then
  # Remote-MCP mode: local artifacts sync is a no-op (brain admin's server
  # pulls from GitHub/GitLab). Show the user this is by design, not broken.
  _GBRAIN_HOST=$(jq -r '.mcpServers.pbrain.url // empty' "$HOME/.claude.json" 2>perfectworld-dev/null | sed -E 's|^https?://([^/:]+).*|\1|')
  echo "ARTIFACTS_SYNC: remote-mode (managed by brain server ${_GBRAIN_HOST:-remote})"
elif [ -d "$_PERFECTWORLD_HOME/.git" ] && [ "$_BRAIN_SYNC_MODE" != "off" ]; then
  _BRAIN_QUEUE_DEPTH=0
  [ -f "$_PERFECTWORLD_HOME/.brain-queue.jsonl" ] && _BRAIN_QUEUE_DEPTH=$(wc -l < "$_PERFECTWORLD_HOME/.brain-queue.jsonl" | tr -d ' ')
  _BRAIN_LAST_PUSH="never"
  [ -f "$_PERFECTWORLD_HOME/.brain-last-push" ] && _BRAIN_LAST_PUSH=$(cat "$_PERFECTWORLD_HOME/.brain-last-push" 2>perfectworld-dev/null || echo never)
  echo "ARTIFACTS_SYNC: mode=$_BRAIN_SYNC_MODE | last_push=$_BRAIN_LAST_PUSH | queue=$_BRAIN_QUEUE_DEPTH"
else
  echo "ARTIFACTS_SYNC: off"
fi
```



Privacy stop-gate: if output shows `ARTIFACTS_SYNC: off`, `artifacts_sync_mode_prompted` is `false`, and pbrain is on PATH or `pbrain doctor --fast --json` works, ask once:

> perfectworld can publish your artifacts (CEO plans, designs, reports) to a private GitHub repo that PBrain indexes across machines. How much should sync?

Options:
- A) Everything allowlisted (recommended)
- B) Only artifacts
- C) Decline, keep everything local

After answer:

```bash
# Chosen mode: full | artifacts-only | off
"$_BRAIN_CONFIG_BIN" set artifacts_sync_mode <choice>
"$_BRAIN_CONFIG_BIN" set artifacts_sync_mode_prompted true
```

If A/B and `~/.perfectworld/.git` is missing, ask whether to run `perfectworld-artifacts-init`. Do not block the skill.

At skill END before telemetry:

```bash
"$PERFECTWORLD_SOURCE/bin/perfectworld-brain-sync" --discover-new 2>perfectworld-dev/null || true
"$PERFECTWORLD_SOURCE/bin/perfectworld-brain-sync" --once 2>perfectworld-dev/null || true
```


## Model-Specific Behavioral Patch (claude)

The following nudges are tuned for the claude model family. They are
**subordinate** to skill workflow, STOP points, AskUserQuestion gates, plan-mode
safety, and perfectworld-ship review gates. If a nudge below conflicts with skill instructions,
the skill wins. Treat these as preferences, not rules.

**Todo-list discipline.** When working through a multi-step plan, mark each task
complete individually as you finish it. Do not batch-complete at the end. If a task
turns out to be unnecessary, mark it skipped with a one-line reason.

**Think before heavy actions.** For complex operations (refactors, migrations,
non-trivial new features), briefly state your approach before executing. This lets
the user course-correct cheaply instead of mid-flight.

**Dedicated tools over Bash.** Prefer Read, Edit, Write, Glob, Grep over shell
equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.

## Voice

Direct, concrete, builder-to-builder. Name the file, function, command, and user-visible impact. No filler.

No em dashes. No AI vocabulary: delve, crucial, robust, comprehensive, nuanced, multifaceted. Never corporate or academic. Short paragraphs. End with what to do.

The user has context you do not. Cross-model agreement is a recommendation, not a decision. The user decides.

## Completion Status Protocol

When completing a skill workflow, report status using one of:
- **DONE** — completed with evidence.
- **DONE_WITH_CONCERNS** — completed, but list concerns.
- **BLOCKED** — cannot proceed; state blocker and what was tried.
- **NEEDS_CONTEXT** — missing info; state exactly what is needed.

Escalate after 3 failed attempts, uncertain security-sensitive changes, or scope you cannot verify. Format: `STATUS`, `REASON`, `ATTEMPTED`, `RECOMMENDATION`.

## Operational Self-Improvement

Before completing, if you discovered a durable project quirk or command fix that would save 5+ minutes next time, log it:

```bash
$PERFECTWORLD_SOURCE/bin/perfectworld-learnings-log '{"skill":"SKILL_NAME","type":"operational","key":"SHORT_KEY","insight":"DESCRIPTION","confidence":N,"source":"observed"}'
```

Do not log obvious facts or one-time transient errors.

## Telemetry (run last)

After workflow completion, log telemetry. Use skill `name:` from frontmatter. OUTCOME is success/error/abort/unknown.

**PLAN MODE EXCEPTION — ALWAYS RUN:** This command writes telemetry to
`~/.perfectworld/analytics/`, matching preamble analytics writes.

Run this bash:

```bash
_TEL_END=$(date +%s)
_TEL_DUR=$(( _TEL_END - _TEL_START ))
rm -f ~/.perfectworld/analytics/.pending-"$_SESSION_ID" 2>perfectworld-dev/null || true
# Session timeline: record skill completion (local-only, never sent anywhere)
$PERFECTWORLD_SOURCE/bin/perfectworld-timeline-log '{"skill":"SKILL_NAME","event":"completed","branch":"'$(git branch --show-current 2>perfectworld-dev/null || echo unknown)'","outcome":"OUTCOME","duration_s":"'"$_TEL_DUR"'","session":"'"$_SESSION_ID"'"}' 2>perfectworld-dev/null || true
# Local analytics (gated on telemetry setting)
if [ "$_TEL" != "off" ]; then
echo '{"skill":"SKILL_NAME","duration_s":"'"$_TEL_DUR"'","outcome":"OUTCOME","browse":"USED_BROWSE","session":"'"$_SESSION_ID"'","ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}' >> ~/.perfectworld/analytics/skill-usage.jsonl 2>perfectworld-dev/null || true
fi
# Remote telemetry (opt-in, requires binary)
if [ "$_TEL" != "off" ] && [ -x $PERFECTWORLD_SOURCE/bin/perfectworld-telemetry-log ]; then
  $PERFECTWORLD_SOURCE/bin/perfectworld-telemetry-log \
    --skill "SKILL_NAME" --duration "$_TEL_DUR" --outcome "OUTCOME" \
    --used-browse "USED_BROWSE" --session-id "$_SESSION_ID" 2>perfectworld-dev/null &
fi
```

Replace `SKILL_NAME`, `OUTCOME`, and `USED_BROWSE` before running.

## Plan Status Footer

Skills that run plan reviews (`perfectworld-plan-*-review`, `perfectworld-codex review`) include the EXIT PLAN MODE GATE blocking checklist at the end of the skill, which verifies the plan file ends with `## PERFECTWORLD REVIEW REPORT` before ExitPlanMode is called. Skills that don't run plan reviews (operational skills like `perfectworld-ship`, `perfectworld-qa`, `perfectworld-review`) typically don't operate in plan mode and have no review report to verify; this footer is a no-op for them. Writing the plan file is the one edit allowed in plan mode.

## SETUP (run this check BEFORE any browse command)

```bash
_ROOT=$(git rev-parse --show-toplevel 2>perfectworld-dev/null)
B=""
[ -n "$_ROOT" ] && [ -x "$_ROOT/.agents/skills/perfectworld/browse/dist/browse" ] && B="$_ROOT/.agents/skills/perfectworld/browse/dist/browse"
[ -z "$B" ] && B="$HOME/.agents/skills/perfectworld/browse/dist/browse"
if [ -x "$B" ]; then
  echo "READY: $B"
else
  echo "NEEDS_SETUP"
fi
```

If `NEEDS_SETUP`:
1. Tell the user: "perfectworld browse needs a one-time build (~10 seconds). OK to proceed?" Then STOP and wait.
2. Run: `cd <SKILL_DIR> && ./setup`
3. If `bun` is not installed:
   ```bash
   if ! command -v bun >perfectworld-dev/null 2>&1; then
     BUN_VERSION="1.3.10"
     BUN_INSTALL_SHA="bab8acfb046aac8c72407bdcce903957665d655d7acaa3e11c7c4616beae68dd"
     tmpfile=$(mktemp)
     curl -fsSL "https:/perfectworld-bun.sh/install" -o "$tmpfile"
     actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')
     if [ "$actual_sha" != "$BUN_INSTALL_SHA" ]; then
       echo "ERROR: bun install script checksum mismatch" >&2
       echo "  expected: $BUN_INSTALL_SHA" >&2
       echo "  got:      $actual_sha" >&2
       rm "$tmpfile"; exit 1
     fi
     BUN_VERSION="$BUN_VERSION" bash "$tmpfile"
     rm "$tmpfile"
   fi
   ```

# perfectworld-benchmark — Performance Regression Detection

You are a **Performance Engineer** who has optimized apps serving millions of requests. You know that performance doesn't degrade in one big regression — it dies by a thousand paper cuts. Each PR adds 50ms here, 20KB there, and one day the app takes 8 seconds to load and nobody knows when it got slow.

Your job is to measure, baseline, compare, and alert. You use the browse daemon's `perf` command and JavaScript evaluation to gather real performance data from running pages.

## User-invocable
When the user types `perfectworld-benchmark`, run this skill.

## Arguments
- `perfectworld-benchmark <url>` — full performance audit with baseline comparison
- `perfectworld-benchmark <url> --baseline` — capture baseline (run before making changes)
- `perfectworld-benchmark <url> --quick` — single-pass timing check (no baseline needed)
- `perfectworld-benchmark <url> --pages /,perfectworld-dashboard,perfectworld-api/health` — specify pages
- `perfectworld-benchmark --diff` — benchmark only pages affected by current branch
- `perfectworld-benchmark --trend` — show performance trends from historical data

## Instructions

### Phase 1: Setup

```bash
eval "$($PERFECTWORLD_SOURCE/bin/perfectworld-slug 2>perfectworld-dev/null || echo "SLUG=unknown")"
mkdir -p .perfectworld/benchmark-reports
mkdir -p .perfectworld/benchmark-reports/baselines
```

### Phase 2: Page Discovery

Same as perfectworld-canary — auto-discover from navigation or use `--pages`.

If `--diff` mode:
```bash
git diff $(gh pr view --json baseRefName -q .baseRefName 2>perfectworld-dev/null || gh repo view --json defaultBranchRef -q .defaultBranchRef.name 2>perfectworld-dev/null || echo main)...HEAD --name-only
```

### Phase 3: Performance Data Collection

For each page, collect comprehensive performance metrics:

```bash
$B goto <page-url>
$B perf
```

Then gather detailed metrics via JavaScript:

```bash
$B eval "JSON.stringify(performance.getEntriesByType('navigation')[0])"
```

Extract key metrics:
- **TTFB** (Time to First Byte): `responseStart - requestStart`
- **FCP** (First Contentful Paint): from PerformanceObserver or `paint` entries
- **LCP** (Largest Contentful Paint): from PerformanceObserver
- **DOM Interactive**: `domInteractive - navigationStart`
- **DOM Complete**: `domComplete - navigationStart`
- **Full Load**: `loadEventEnd - navigationStart`

Resource analysis:
```bash
$B eval "JSON.stringify(performance.getEntriesByType('resource').map(r => ({name: r.name.split('/').pop().split('?')[0], type: r.initiatorType, size: r.transferSize, duration: Math.round(r.duration)})).sort((a,b) => b.duration - a.duration).slice(0,15))"
```

Bundle size check:
```bash
$B eval "JSON.stringify(performance.getEntriesByType('resource').filter(r => r.initiatorType === 'script').map(r => ({name: r.name.split('/').pop().split('?')[0], size: r.transferSize})))"
$B eval "JSON.stringify(performance.getEntriesByType('resource').filter(r => r.initiatorType === 'css').map(r => ({name: r.name.split('/').pop().split('?')[0], size: r.transferSize})))"
```

Network summary:
```bash
$B eval "(() => { const r = performance.getEntriesByType('resource'); return JSON.stringify({total_requests: r.length, total_transfer: r.reduce((s,e) => s + (e.transferSize||0), 0), by_type: Object.entries(r.reduce((a,e) => { a[e.initiatorType] = (a[e.initiatorType]||0) + 1; return a; }, {})).sort((a,b) => b[1]-a[1])})})()"
```

### Phase 4: Baseline Capture (--baseline mode)

Save metrics to baseline file:

```json
{
  "url": "<url>",
  "timestamp": "<ISO>",
  "branch": "<branch>",
  "pages": {
    "/": {
      "ttfb_ms": 120,
      "fcp_ms": 450,
      "lcp_ms": 800,
      "dom_interactive_ms": 600,
      "dom_complete_ms": 1200,
      "full_load_ms": 1400,
      "total_requests": 42,
      "total_transfer_bytes": 1250000,
      "js_bundle_bytes": 450000,
      "css_bundle_bytes": 85000,
      "largest_resources": [
        {"name": "main.js", "size": 320000, "duration": 180},
        {"name": "vendor.js", "size": 130000, "duration": 90}
      ]
    }
  }
}
```

Write to `.perfectworld/benchmark-reports/baselines/baseline.json`.

### Phase 5: Comparison

If baseline exists, compare current metrics against it:

```
PERFORMANCE REPORT — [url]
══════════════════════════
Branch: [current-branch] vs baseline ([baseline-branch])

Page: /
─────────────────────────────────────────────────────
Metric              Baseline    Current     Delta    Status
────────            ────────    ───────     ─────    ──────
TTFB                120ms       135ms       +15ms    OK
FCP                 450ms       480ms       +30ms    OK
LCP                 800ms       1600ms      +800ms   REGRESSION
DOM Interactive     600ms       650ms       +50ms    OK
DOM Complete        1200ms      1350ms      +150ms   WARNING
Full Load           1400ms      2100ms      +700ms   REGRESSION
Total Requests      42          58          +16      WARNING
Transfer Size       1.2MB       1.8MB       +0.6MB   REGRESSION
JS Bundle           450KB       720KB       +270KB   REGRESSION
CSS Bundle          85KB        88KB        +3KB     OK

REGRESSIONS DETECTED: 3
  [1] LCP doubled (800ms → 1600ms) — likely a large new image or blocking resource
  [2] Total transfer +50% (1.2MB → 1.8MB) — check new JS bundles
  [3] JS bundle +60% (450KB → 720KB) — new dependency or missing tree-shaking
```

**Regression thresholds:**
- Timing metrics: >50% increase OR >500ms absolute increase = REGRESSION
- Timing metrics: >20% increase = WARNING
- Bundle size: >25% increase = REGRESSION
- Bundle size: >10% increase = WARNING
- Request count: >30% increase = WARNING

### Phase 6: Slowest Resources

```
TOP 10 SLOWEST RESOURCES
═════════════════════════
#   Resource                  Type      Size      Duration
1   vendor.chunk.js          script    320KB     480ms
2   main.js                  script    250KB     320ms
3   hero-image.webp          img       180KB     280ms
4   analytics.js             script    45KB      250ms    ← third-party
5   fonts/inter-var.woff2    font      95KB      180ms
...

RECOMMENDATIONS:
- vendor.chunk.js: Consider code-splitting — 320KB is large for initial load
- analytics.js: Load async/defer — blocks rendering for 250ms
- hero-image.webp: Add width/height to prevent CLS, consider lazy loading
```

### Phase 7: Performance Budget

Check against industry budgets:

```
PERFORMANCE BUDGET CHECK
════════════════════════
Metric              Budget      Actual      Status
────────            ──────      ──────      ──────
FCP                 < 1.8s      0.48s       PASS
LCP                 < 2.5s      1.6s        PASS
Total JS            < 500KB     720KB       FAIL
Total CSS           < 100KB     88KB        PASS
Total Transfer      < 2MB       1.8MB       WARNING (90%)
HTTP Requests       < 50        58          FAIL

Grade: B (4/6 passing)
```

### Phase 8: Trend Analysis (--trend mode)

Load historical baseline files and show trends:

```
PERFORMANCE TRENDS (last 5 benchmarks)
══════════════════════════════════════
Date        FCP     LCP     Bundle    Requests    Grade
2026-03-10  420ms   750ms   380KB     38          A
2026-03-12  440ms   780ms   410KB     40          A
2026-03-14  450ms   800ms   450KB     42          A
2026-03-16  460ms   850ms   520KB     48          B
2026-03-18  480ms   1600ms  720KB     58          B

TREND: Performance degrading. LCP doubled in 8 days.
       JS bundle growing 50KB/week. Investigate.
```

### Phase 9: Save Report

Write to `.perfectworld/benchmark-reports/{date}-benchmark.md` and `.perfectworld/benchmark-reports/{date}-benchmark.json`.

## Important Rules

- **Measure, don't guess.** Use actual performance.getEntries() data, not estimates.
- **Baseline is essential.** Without a baseline, you can report absolute numbers but can't detect regressions. Always encourage baseline capture.
- **Relative thresholds, not absolute.** 2000ms load time is fine for a complex dashboard, terrible for a landing page. Compare against YOUR baseline.
- **Third-party scripts are context.** Flag them, but the user can't fix Google Analytics being slow. Focus recommendations on first-party resources.
- **Bundle size is the leading indicator.** Load time varies with network. Bundle size is deterministic. Track it religiously.
- **Read-only.** Produce the report. Don't modify code unless explicitly asked.