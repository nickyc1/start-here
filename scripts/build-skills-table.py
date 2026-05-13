#!/usr/bin/env python3
"""Build the alphabetized skills table for the profile README.

Reads each public skill repo under nickyc1, extracts the name +
description from SKILL.md frontmatter (or README.md if SKILL.md
is absent), and rewrites the table between the
<!-- SKILLS:START --> and <!-- SKILLS:END --> markers in README.md.

Usage:
    python3 scripts/build-skills-table.py

Requires:
    - gh CLI authenticated as nickyc1
    - Python 3.9+
    - PyYAML (pip install pyyaml)
"""

import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Install PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_OWNER = "nickyc1"
README_PATH = Path(__file__).parent.parent / "README.md"
EXCLUDE_REPOS = {
    REPO_OWNER,        # the profile repo itself
    "marketing-stack",  # tools, not a skill
    "ppc-profit-intelligence",  # a guide/landing page, not a Claude skill
}


def gh_api(path):
    """Call gh api and return parsed JSON."""
    out = subprocess.check_output(
        ["gh", "api", path, "--paginate"],
        text=True,
    )
    return json.loads(out)


def get_skill_metadata(repo_name):
    """Fetch SKILL.md frontmatter from a repo. Returns dict or None."""
    paths_to_try = ["SKILL.md", "skill.md"]
    for path in paths_to_try:
        try:
            content_resp = subprocess.check_output(
                ["gh", "api", f"repos/{REPO_OWNER}/{repo_name}/contents/{path}"],
                text=True,
                stderr=subprocess.DEVNULL,
            )
            content_obj = json.loads(content_resp)
            import base64
            content = base64.b64decode(content_obj["content"]).decode()
            # Extract YAML frontmatter
            m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if m:
                return yaml.safe_load(m.group(1))
        except subprocess.CalledProcessError:
            continue
    return None


def get_repo_description(repo_name):
    """Fall back to the GitHub repo description if no SKILL.md frontmatter."""
    try:
        out = subprocess.check_output(
            ["gh", "repo", "view", f"{REPO_OWNER}/{repo_name}", "--json", "description"],
            text=True,
        )
        return json.loads(out).get("description", "")
    except subprocess.CalledProcessError:
        return ""


def build_table():
    """Build the markdown table of all skills."""
    print(f"Listing public repos for {REPO_OWNER}...", file=sys.stderr)
    repos_data = subprocess.check_output(
        [
            "gh", "repo", "list", REPO_OWNER,
            "--visibility", "public",
            "--limit", "100",
            "--json", "name,description",
        ],
        text=True,
    )
    repos = json.loads(repos_data)

    rows = []
    for repo in repos:
        name = repo["name"]
        if name in EXCLUDE_REPOS:
            continue

        meta = get_skill_metadata(name)
        if meta and "name" in meta:
            description = meta.get("description", "").strip()
        else:
            description = repo.get("description", "").strip() or get_repo_description(name)

        # Truncate description to first sentence or 200 chars
        if description:
            description = description.replace("\n", " ").strip()
            # Truncate to ~200 chars at a sentence boundary
            if len(description) > 200:
                cut = description[:200].rsplit(". ", 1)[0]
                if cut != description[:200] and len(cut) > 50:
                    description = cut + "."
                else:
                    description = description[:200].rsplit(" ", 1)[0] + "..."
        else:
            description = "(no description)"

        rows.append((name, description))
        print(f"  {name}", file=sys.stderr)

    rows.sort(key=lambda r: r[0].lower())

    lines = ["| Skill | Description |", "|-------|-------------|"]
    for name, description in rows:
        lines.append(f"| [{name}](https://github.com/{REPO_OWNER}/{name}) | {description} |")

    return "\n".join(lines)


def update_readme(table):
    """Replace the section between SKILLS:START and SKILLS:END markers."""
    if not README_PATH.exists():
        print(f"README not found at {README_PATH}", file=sys.stderr)
        sys.exit(1)

    content = README_PATH.read_text()

    start_marker = "<!-- SKILLS:START -->"
    end_marker = "<!-- SKILLS:END -->"

    if start_marker not in content or end_marker not in content:
        print(f"Markers {start_marker} and {end_marker} not found in README", file=sys.stderr)
        print("Add them to README.md first, then re-run.", file=sys.stderr)
        sys.exit(1)

    new_block = f"{start_marker}\n\n{table}\n\n{end_marker}"
    new_content = re.sub(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        new_block,
        content,
        flags=re.DOTALL,
    )

    README_PATH.write_text(new_content)
    print(f"Updated {README_PATH}", file=sys.stderr)


if __name__ == "__main__":
    table = build_table()
    update_readme(table)
