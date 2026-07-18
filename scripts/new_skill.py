#!/usr/bin/env python3
import argparse
import os
import re
import shutil
import sys
from pathlib import Path

def is_kebab_case(s):
    return re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', s) is not None

def main():
    parser = argparse.ArgumentParser(description="Create a new skill from the template.")
    parser.add_argument("slug", help="The kebab-case name of the new skill (e.g., my-new-skill)")
    parser.add_argument("--title", help="The human-readable title of the skill", default="")
    parser.add_argument("--target", help="The primary target platform (e.g., claude-code)", default="claude-code")
    parser.add_argument("--status", help="The initial status", choices=["draft", "experimental", "stable", "deprecated"], default="draft")

    args = parser.parse_args()
    slug = args.slug
    title = args.title if args.title else slug.replace("-", " ").title()

    if not is_kebab_case(slug):
        print(f"Error: Skill slug '{slug}' must be lowercase kebab-case.", file=sys.stderr)
        sys.exit(1)

    # Prevent path traversal implicitly by strictly validating kebab-case
    # but let's be explicit
    if "/" in slug or "\\" in slug or "." in slug:
        print("Error: Invalid characters in slug.", file=sys.stderr)
        sys.exit(1)

    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"
    template_dir = repo_root / "templates" / "new-skill"
    target_dir = skills_dir / slug

    if not template_dir.exists():
        print(f"Error: Template directory not found at {template_dir}", file=sys.stderr)
        sys.exit(1)

    if target_dir.exists():
        print(f"Error: Skill directory '{target_dir}' already exists.", file=sys.stderr)
        sys.exit(1)

    print(f"Creating new skill '{slug}'...")

    try:
        shutil.copytree(template_dir, target_dir)
    except Exception as e:
        print(f"Error copying template: {e}", file=sys.stderr)
        sys.exit(1)

    replacements = {
        "{{SKILL_SLUG}}": slug,
        "{{SKILL_TITLE}}": title,
        "{{SKILL_STATUS}}": args.status,
        "{{SKILL_TARGET}}": args.target,
    }

    # Replace placeholders
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = Path(root) / file
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    for key, val in replacements.items():
                        content = content.replace(key, val)

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Warning: Failed to process {file_path}: {e}", file=sys.stderr)

    print(f"\nSuccess! Skill '{slug}' created at:\n{target_dir.relative_to(repo_root)}")
    print("\nNext steps:")
    print(f"  1. Edit skills/{slug}/SKILL.md to define agent instructions.")
    print(f"  2. Edit skills/{slug}/README.md to explain usage.")
    print("  3. Run `python scripts/validate_repository.py` to ensure it meets requirements.")

if __name__ == "__main__":
    main()
