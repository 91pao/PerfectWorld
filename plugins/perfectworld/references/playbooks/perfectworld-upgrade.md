# 完美世界 自升级维护员 On-Demand Playbook

Read only the section relevant to the current task. The active skill's verification and efficiency policies override inherited instructions below.

## upgrade

<!-- AUTO-GENERATED from SKILL.md.tmpl  do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->


## When to use this skill

Detects global vs vendored install,
runs the upgrade, and shows what's new. Use when asked to "upgrade perfectworld",
"update perfectworld", or "get latest version".

Voice triggers (speech-to-text aliases): "upgrade the tools", "update the tools", "gee stack upgrade", "g stack upgrade".

# perfectworld-perfectworld-upgrade

Upgrade perfectworld to the latest version and show what's new.

## Inline upgrade flow

This section is referenced by all skill preambles when they detect `UPGRADE_AVAILABLE`.

### Step 1: Ask the user (or auto-upgrade)

First, check if auto-upgrade is enabled:
```bash
_AUTO=""
[ "${PERFECTWORLD_AUTO_UPGRADE:-}" = "1" ] && _AUTO="true"
[ -z "$_AUTO" ] && _AUTO=$($PERFECTWORLD_SOURCE/bin/perfectworld-config get auto_upgrade 2>perfectworld-dev/null || true)
echo "AUTO_UPGRADE=$_AUTO"
```

**If `AUTO_UPGRADE=true` or `AUTO_UPGRADE=1`:** Skip AskUserQuestion. Log "Auto-upgrading perfectworld v{old}  v{new}..." and proceed directly to Step 2. If `./setup` fails during auto-upgrade, restore from backup (`.bak` directory) and warn the user: "Auto-upgrade failed  restored previous version. Run `perfectworld-perfectworld-upgrade` manually to retry."

**Otherwise**, use AskUserQuestion:
- Question: "perfectworld **v{new}** is available (you're on v{old}). Upgrade now?"
- Options: ["Yes, upgrade now", "Always keep me up to date", "Not now", "Never ask again"]

**If "Yes, upgrade now":** Proceed to Step 2.

**If "Always keep me up to date":**
```bash
$PERFECTWORLD_SOURCE/bin/perfectworld-config set auto_upgrade true
```
Tell user: "Auto-upgrade enabled. Future updates will install automatically." Then proceed to Step 2.
