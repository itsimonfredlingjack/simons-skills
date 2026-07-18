# Repository Conventions

This repository follows strict structural and metadata conventions to ensure skills are discoverable, usable, and validatable.

## Directory Structure

Every real skill lives in the `skills/` directory under a kebab-case slug:

```text
skills/<skill-slug>/
├── SKILL.md       # (Required) The agent-facing executable instructions
├── README.md      # (Required) The human-facing explanation and usage guide
├── CHANGELOG.md   # (Optional) Records of meaningful behavioral changes
├── examples/      # (Optional) Illustrative inputs, outputs, and scenarios
├── references/    # (Optional) Material the skill explicitly depends upon
├── scripts/       # (Optional) Supporting executable tooling
└── assets/        # (Optional) Local visual or data assets
```

## SKILL.md Metadata

Every `SKILL.md` must begin with YAML frontmatter. This metadata is used by validation scripts and helps catalog the skills.

### Required Fields

*   **`name`**: The exact slug of the skill (must match the directory name).
*   **`description`**: A concise, one-sentence description of the skill's behavior.
*   **`author`**: The creator of the skill (usually Simon Fredling Jack).
*   **`version`**: Semantic versioning (e.g., `0.1.0`).
*   **`status`**: The lifecycle status of the skill. Must be one of:
    *   `draft`: Under active development, not ready for use.
    *   `experimental`: Usable, but behavior may change significantly.
    *   `stable`: Tested and reliable for its defined scope.
    *   `deprecated`: No longer recommended for use.
*   **`targets`**: A list of supported environments (e.g., `claude-code`, `jules`, `grok`). Must contain at least one item.

### Optional Fields

*   **`tags`**: A list of categorization keywords (e.g., `planning`, `refactoring`, `review`).
*   **`requires`**: A list of required tools, MCP servers, or dependencies.

### Example Frontmatter

```yaml
---
name: example-skill
description: Generates a comprehensive execution plan before modifying code.
author: Simon Fredling Jack
version: 1.0.0
status: stable
targets:
  - claude-code
  - jules
tags:
  - planning
  - workflow
---
```

## Naming and Formatting

*   Use `kebab-case` for all directory names and file names (except standard uppercase files like `README.md`).
*   Use standard Markdown. Avoid overly complex HTML styling unless necessary for specific visual communication in the README.
