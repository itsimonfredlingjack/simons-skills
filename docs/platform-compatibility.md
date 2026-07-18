# Platform Compatibility Guide

An AI-agent "skill" is not a universal technical standard. Different platforms interpret instructions, manage context, and expose tools in vastly different ways.

This repository acknowledges these differences and aims to provide workflows that are either adaptable across platforms or explicitly scoped to specific ones.

## The Spectrum of Skills

*   **Native Skill/Command Formats:** Some platforms have proprietary formats (e.g., specific JSON schemas or specialized prompt files) that they load directly into the system prompt.
*   **Repository Instructions (`AGENTS.md`):** Passive instructions that agents read when operating within a specific directory tree. These are good for setting ground rules.
*   **System Prompts:** Core instructions that define the agent's persona and baseline capabilities.
*   **Reusable Prompt Files:** Markdown or text files containing structured workflows that a user pastes into a chat or provides as a file reference.
*   **Scripts:** Python or Bash scripts that an agent executes. The "skill" is the agent knowing *when* and *how* to run the script.
*   **MCP Servers:** Model Context Protocol servers that provide discrete tools. A skill might orchestrate the use of multiple MCP tools.

## Targeting Environments

When authoring a skill, you must declare its target environments in the `targets` field of the `SKILL.md` frontmatter.

### Cross-Platform Adaptability

If a skill relies on standard bash tools and basic logical reasoning, it may target multiple agents (e.g., `claude-code`, `jules`). The `SKILL.md` should focus on the conceptual workflow and logical steps rather than assuming the presence of specific proprietary commands (unless those commands are verified and conditional).

### Platform-Specific Workflows

If a skill relies heavily on a specific agent's native capabilities (e.g., a specific MCP integration unique to Jules, or a specific context-loading mechanism in Claude Code), it must be explicitly scoped to that target.

*   Never claim cross-platform compatibility without evidence.
*   Provide explicit installation and usage instructions in the `README.md` for *each* claimed target.

## Verifying Commands

If your `SKILL.md` or `README.md` includes volatile CLI commands for external tools or agent platforms, you must verify them against current official documentation. Prefer conceptual guidance where exact commands are likely to change or are not strictly necessary.
