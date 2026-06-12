---
name: make-pdf
preamble-tier: 1
version: 1.0.0
description: Turn any markdown file into a publication-quality PDF. (perfectworld)
triggers:
  - markdown to pdf
  - generate pdf
  - make pdf
  - export pdf
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---
<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Proper 1in margins,
intelligent page breaks, page numbers, cover pages, running headers, curly
quotes and em dashes, clickable TOC, diagonal DRAFT watermark. Not a draft
artifact — a finished artifact. Use when asked to "make a PDF", "export to
PDF", "turn this markdown into a PDF", or "generate a document".

Voice triggers (speech-to-text aliases): "make this a pdf", "make it a pdf", "export to pdf", "turn this into a pdf", "turn this markdown into a pdf", "generate a pdf", "make a pdf from", "pdf this markdown".

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
echo '{"skill":"make-pdf","ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","repo":"'$(_repo=$(basename "$(git rev-parse --show-toplevel 2>perfectworld-dev/null)" 2>perfectworld-dev/null | tr -cd 'a-zA-Z0-9._-'); echo "${_repo:-unknown}")'"}'  >> ~/.perfectworld/analytics/skill-usage.jsonl 2>perfectworld-dev/null || true
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
$PERFECTWORLD_SOURCE/bin/perfectworld-timeline-log '{"skill":"make-pdf","event":"started","branch":"'"$_BRANCH"'","session":"'"$_SESSION_ID"'"}' 2>perfectworld-dev/null &
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

## MAKE-PDF SETUP (run this check BEFORE any make-pdf command)

```bash
_ROOT=$(git rev-parse --show-toplevel 2>perfectworld-dev/null)
P=""
[ -n "$MAKE_PDF_BIN" ] && [ -x "$MAKE_PDF_BIN" ] && P="$MAKE_PDF_BIN"
[ -z "$P" ] && [ -n "$_ROOT" ] && [ -x "$_ROOT/.agents/skills/perfectworld/make-pdf/dist/pdf" ] && P="$_ROOT/.agents/skills/perfectworld/make-pdf/dist/pdf"
[ -z "$P" ] && P="$HOME/.agents/skills/perfectworld/make-pdf/dist/pdf"
if [ -x "$P" ]; then
  echo "MAKE_PDF_READY: $P"
  alias _p_="$P"   # shellcheck alias helper (not exported)
  export P   # available as $P in subsequent blocks within the same skill invocation
else
  echo "MAKE_PDF_NOT_AVAILABLE (run './setup' in the perfectworld repo to build it)"
fi
```

If `MAKE_PDF_NOT_AVAILABLE` is printed: tell the user the binary is not
built. Have them run `./setup` from the perfectworld repo, then retry.

If `MAKE_PDF_READY` is printed: `$P` is the binary path for the rest of
the skill. Use `$P` (not an explicit path) so the skill body stays portable.

Core commands:
- `$P generate <input.md> [output.pdf]` — render markdown to PDF (80% use case)
- `$P generate --cover --toc essay.md out.pdf` — full publication layout
- `$P generate --watermark DRAFT memo.md draft.pdf` — diagonal DRAFT watermark
- `$P preview <input.md>` — render HTML and open in browser (fast iteration)
- `$P setup` — verify browse + Chromium + pdftotext and run a smoke test
- `$P --help` — full flag reference

Output contract:
- `stdout`: ONLY the output path on success. One line.
- `stderr`: progress (`Rendering HTML... Generating PDF...`) unless `--quiet`.
- Exit 0 success / 1 bad args / 2 render error / 3 Paged.js timeout / 4 browse unavailable.

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

# make-pdf: publication-quality PDFs from markdown

Turn `.md` files into PDFs that look like Faber & Faber essays: 1in margins,
left-aligned body, Helvetica throughout, curly quotes and em dashes, optional
cover page and clickable TOC, diagonal DRAFT watermark when you need it.
Copy-paste from the PDF produces clean words, never "S a i l i n g".

On Linux, install `fonts-liberation` for correct rendering — Helvetica and Arial
aren't present by default, and Liberation Sans is the standard metric-compatible
fallback. CI and Docker builds install it automatically via Dockerfile.ci.

Emoji need a color-emoji font. macOS (Apple Color Emoji) and Windows (Segoe UI
Emoji) ship one; most Linux distros and containers ship none, so emoji render as
empty boxes (▯). `./setup` auto-installs `fonts-noto-color-emoji` on Linux
(apt/dnf/pacman/apk, best-effort) and the print CSS falls back through Apple /
Segoe / Noto emoji families. Set `PERFECTWORLD_SKIP_FONTS=1` to skip the install (CI
without sudo, managed or offline machines).

## Core patterns

### 80% case — memo/letter

One command, no flags. Gets a clean PDF with running header + page numbers
+ CONFIDENTIAL footer by default.

```bash
$P generate letter.md                 # writes perfectworld-tmp/letter.pdf
$P generate letter.md letter.pdf      # explicit output path
```

### Publication mode — cover + TOC + chapter breaks

```bash
$P generate --cover --toc --author "Garry Tan" --title "On Horizons" \
  essay.md essay.pdf
```

Each top-level H1 in the markdown starts a new page. Disable with
`--no-chapter-breaks` for memos that happen to have multiple H1s.

### Draft-stage watermark

```bash
$P generate --watermark DRAFT memo.md draft.pdf
```

Diagonal 10% opacity DRAFT across every page. When the draft is final, drop
the flag and regenerate.

### Fast iteration via preview

```bash
$P preview essay.md
```

Renders HTML with the same print CSS and opens it in your browser. Refresh
as you edit the markdown. Skip the PDF round trip until you're ready.

### Brand-free (no CONFIDENTIAL footer)

```bash
$P generate --no-confidential memo.md memo.pdf
```

## Common flags

```
Page layout:
  --margins <dim>            1in (default) | 72pt | 2.54cm | 25mm
  --page-size letter|a4|legal

Structure:
  --cover                    Cover page (title, author, date, hairline rule)
  --toc                      Clickable TOC with page numbers
  --no-chapter-breaks        Don't start a new page at every H1

Branding:
  --watermark <text>         Diagonal watermark ("DRAFT", "CONFIDENTIAL")
  --header-template <html>   Custom running header
  --footer-template <html>   Custom footer (mutex with --page-numbers)
  --no-confidential          Suppress the CONFIDENTIAL right-footer

Output:
  --page-numbers             "N of M" footer (default on)
  --tagged                   Accessible PDF (default on)
  --outline                  PDF bookmarks from headings (default on)
  --quiet                    Suppress progress on stderr
  --verbose                  Per-stage timings

Network:
  --allow-network            Fetch external images. Off by default
                             (blocks tracking pixels).

Metadata:
  --title "..."              Document title (defaults to first H1)
  --author "..."             Author for cover + PDF metadata
  --date "..."               Date for cover (defaults to today)
```

## When Codex should run it

Watch for markdown-to-PDF intent. Any of these patterns → run `$P generate`:

- "Can you make this markdown a PDF"
- "Export it as a PDF"
- "Turn this letter into a PDF"
- "I need a PDF of the essay"
- "Print this as a PDF for me"

If the user has a `.md` file open and says "make it look nice", propose
`$P generate --cover --toc` and ask before running.

## Debugging

- Output looks empty / blank → check browse daemon is running: `$B status`.
- Fragmented text on copy-paste → highlight.js output (Phase 4). Retry with
  `--no-syntax` once that flag exists. For now, remove fenced code blocks
  and regenerate.
- Paged.js timeout → probably no headings in the markdown. Drop `--toc`.
- External image missing → add `--allow-network` (understand you're giving
  the markdown file permission to fetch from its image URLs).
- Generated PDF too tall/wide → `--page-size a4` or `--margins 0.75in`.

## Output contract

```
stdout: perfectworld-tmp/letter.pdf          ← just the path, one line
stderr: Rendering HTML...        ← progress spinner (unless --quiet)
        Generating PDF...
        Done in 1.5s. 43 words · 22KB · perfectworld-tmp/letter.pdf

exit code: 0 success / 1 bad args / 2 render error / 3 Paged.js timeout
           / 4 browse unavailable
```

Capture the path: `PDF=$($P generate letter.md)` — then use `$PDF`.