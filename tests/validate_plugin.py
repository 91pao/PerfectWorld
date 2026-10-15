#!/usr/bin/env python3
"""Validate UE PerfectWorld manifests, skill metadata, references, and routing evals."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"{path.relative_to(ROOT)}: {error}")
        return None


plugin = load_json(ROOT / ".codex-plugin" / "plugin.json")
marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
evals = load_json(ROOT / "evals" / "skill-routing.json")

skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
skill_names: set[str] = set()
for skill_file in skill_files:
    text = skill_file.read_text(encoding="utf-8")
    front_matter = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if not front_matter:
        fail(f"{skill_file.relative_to(ROOT)}: missing YAML front matter")
        continue

    name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", front_matter.group(1))
    description_match = re.search(r"(?m)^description:\s*(.+?)\s*$", front_matter.group(1))
    if not name_match or not description_match:
        fail(f"{skill_file.relative_to(ROOT)}: name and description are required")
        continue

    name = name_match.group(1)
    if name != skill_file.parent.name:
        fail(f"{skill_file.relative_to(ROOT)}: skill name does not match directory")
    if name in skill_names:
        fail(f"{skill_file.relative_to(ROOT)}: duplicate skill name {name}")
    skill_names.add(name)

    for relative in re.findall(r"`(\.\./\.\./references/[^`]+)`", text):
        if not (skill_file.parent / relative).resolve().is_file():
            fail(f"{skill_file.relative_to(ROOT)}: missing reference {relative}")

if plugin:
    if plugin.get("name") != "ue-perfectworld":
        fail("plugin manifest has unexpected name")
    version = plugin.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"invalid plugin version: {version}")
    else:
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        releases = list(
            re.finditer(r"(?m)^## (\d+\.\d+\.\d+) - \d{4}-\d{2}-\d{2}$", changelog)
        )
        if not releases or releases[0].group(1) != version:
            fail(f"CHANGELOG.md has no dated entry for plugin version {version}")
        seen_versions: set[str] = set()
        for index, release in enumerate(releases):
            release_version = release.group(1)
            if release_version in seen_versions:
                fail(f"CHANGELOG.md has duplicate entry for {release_version}")
            seen_versions.add(release_version)
            end = releases[index + 1].start() if index + 1 < len(releases) else len(changelog)
            body = changelog[release.end() : end]
            if not re.search(r"(?m)^### (新增|调整|修复|移除|保持不变|升级说明)$", body):
                fail(f"CHANGELOG.md entry {release_version} has no standard category")
    onboarding = (
        plugin.get("extensions", {})
        .get("com.openai", {})
        .get("onboardingSkill")
    )
    if onboarding and not (ROOT / onboarding.removeprefix("./")).is_file():
        fail(f"onboarding skill does not exist: {onboarding}")

if marketplace:
    plugins = marketplace.get("plugins", [])
    matching = [item for item in plugins if item.get("name") == "ue-perfectworld"]
    if len(matching) != 1:
        fail("marketplace must contain exactly one ue-perfectworld entry")
    else:
        source = matching[0].get("source", {})
        source_path = source.get("path", "")
        if source.get("source") != "local" or not source_path.startswith("./"):
            fail("marketplace source must be local and use a ./-prefixed path")
        source_root = (ROOT / source_path).resolve()
        if not source_root.is_relative_to(ROOT):
            fail("marketplace source path escapes the repository")
        if not (source_root / ".codex-plugin" / "plugin.json").is_file():
            fail("marketplace source path does not contain the plugin manifest")

if evals is not None:
    seen_ids: set[str] = set()
    for case in evals:
        case_id = case.get("id")
        if not case_id or case_id in seen_ids:
            fail(f"routing eval has missing or duplicate id: {case_id}")
        seen_ids.add(case_id)
        primary = case.get("expected_primary")
        if primary is not None and primary not in skill_names:
            fail(f"{case_id}: unknown expected primary skill {primary}")
        for supporting in case.get("expected_supporting", []):
            if supporting not in skill_names:
                fail(f"{case_id}: unknown supporting skill {supporting}")

core_rules = (ROOT / "references" / "ue-core-rules.md").read_text(encoding="utf-8")
for stage in range(7):
    if f"S{stage}" not in core_rules:
        fail(f"core rules do not mention S{stage}")

if ERRORS:
    print("\n".join(f"ERROR: {error}" for error in ERRORS))
    sys.exit(1)

print(
    f"OK: plugin manifests, {len(skill_names)} skills, "
    f"{len(evals)} routing evals, and S0-S6 references"
)
