#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path

REQUIRED_STATUSES = {"draft", "experimental", "stable", "deprecated"}

def parse_frontmatter(content):
    """Simple YAML frontmatter parser."""
    if not content.startswith("---\n"):
        return None, content

    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return None, content

    yaml_text = parts[1]
    body = parts[2]

    metadata = {}
    current_list_key = None

    for line in yaml_text.splitlines():
        line = line.rstrip()
        if not line:
            continue

        if line.startswith("  - "):
            if current_list_key:
                val = line[4:].strip()
                if val:
                    metadata[current_list_key].append(val)
            continue

        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()

            if val == "":
                current_list_key = key
                metadata[key] = []
            else:
                current_list_key = None
                # Strip simple quotes
                if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
                    val = val[1:-1]
                metadata[key] = val

    return metadata, body

def validate_skill(skill_dir):
    errors = []
    slug = skill_dir.name

    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug):
        errors.append(f"Directory name '{slug}' is not valid kebab-case.")

    skill_md_path = skill_dir / "SKILL.md"
    readme_md_path = skill_dir / "README.md"

    if not skill_md_path.exists():
        errors.append("Missing SKILL.md")
    else:
        try:
            with open(skill_md_path, "r", encoding="utf-8") as f:
                content = f.read()

            if "{{SKILL_" in content:
                errors.append("SKILL.md contains unresolved template placeholders.")

            meta, body = parse_frontmatter(content)
            if meta is None:
                errors.append("SKILL.md missing valid YAML frontmatter block.")
            else:
                if meta.get("name") != slug:
                    errors.append(f"Frontmatter 'name' ({meta.get('name')}) does not match directory slug ({slug}).")
                if "description" not in meta:
                    errors.append("Frontmatter missing 'description'.")
                if "author" not in meta:
                    errors.append("Frontmatter missing 'author'.")
                if "version" not in meta:
                    errors.append("Frontmatter missing 'version'.")

                status = meta.get("status")
                if status not in REQUIRED_STATUSES:
                    errors.append(f"Invalid status '{status}'. Must be one of {REQUIRED_STATUSES}.")

                targets = meta.get("targets")
                if not targets or not isinstance(targets, list) or len(targets) == 0:
                    errors.append("Frontmatter 'targets' must be a non-empty list.")

        except UnicodeDecodeError:
            errors.append("SKILL.md could not be decoded as UTF-8.")

    if not readme_md_path.exists():
        errors.append("Missing README.md")
    else:
        try:
            with open(readme_md_path, "r", encoding="utf-8") as f:
                content = f.read()
            if "{{SKILL_" in content:
                errors.append("README.md contains unresolved template placeholders.")
        except UnicodeDecodeError:
            errors.append("README.md could not be decoded as UTF-8.")

    return errors

def main():
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"

    if not skills_dir.exists():
        print("Error: skills/ directory not found.")
        sys.exit(1)

    has_errors = False
    skill_count = 0

    print("Validating skills repository...\n")

    for item in skills_dir.iterdir():
        if item.is_dir() and item.name != "templates": # just in case
            skill_count += 1
            errors = validate_skill(item)
            if errors:
                has_errors = True
                print(f"❌ Skill '{item.name}':")
                for err in errors:
                    print(f"   - {err}")
            else:
                print(f"✅ Skill '{item.name}' is valid.")

    if skill_count == 0:
        print("ℹ️  No skills found. The workbench is empty (this is valid).")

    # Check if template is leaking into published
    template_dir = repo_root / "templates" / "new-skill"
    if template_dir.exists():
        # Ensure it doesn't accidentally trigger logic outside its intended use.
        pass

    print("\nValidation completed.")
    if has_errors:
        print("Status: FAILED")
        sys.exit(1)
    else:
        print("Status: PASSED")
        sys.exit(0)

if __name__ == "__main__":
    main()
