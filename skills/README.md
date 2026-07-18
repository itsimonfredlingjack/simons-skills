# Skill Catalog

This directory houses Simon's personal collection of curated agent workflows.

## Catalog

| Skill Family | Description | Target | Status |
|---|---|---|---|
| [**Grok Build Cross-Model Workflow**](grill-me-grok/) | A Claude Code skill family that uses Grok Build as an independent reviewer and optional implementation agent. | `claude-code`, `grok` | `experimental` |

## Structure

A typical skill directory looks like this:

```text
skills/<skill-slug>/
├── SKILL.md       # The agent-facing workflow instructions
├── README.md      # The human-facing usage guide
└── ...            # Optional examples, scripts, or references
```

To contribute or scaffold a new skill, see the root `CONTRIBUTING.md` and use the `scripts/new_skill.py` tool.
