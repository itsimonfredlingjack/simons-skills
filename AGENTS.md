# Agent Instructions

This file contains rules and operational guidelines for AI agents (such as Jules, Claude Code, or other coding assistants) working within this repository.

This repository, `simons-skills`, contains Simon's original AI-agent skills and the reusable authoring infrastructure required to build them.

## Core Rules

* **Inspect before editing:** You must inspect the entire target skill (all relevant files in its directory) before modifying it.
* **No external imports without authorization:** Do not import, recreate, fork, translate, rename, or adapt skills from external repositories without an explicit, direct task instructing you to do so.
* **Preserve attribution:** Never remove attribution from derived or inspired work.
* **No false claims:** Never claim cross-platform compatibility without evidence. Do not invent benchmark results, user adoption claims, or fake metrics.
* **Verify before documenting:** Always verify current CLI syntax and external tool behaviors against current documentation before writing instructions for them.
* **Maintain separation of concerns:**
    * Keep agent-facing, executable instructions in `SKILL.md`.
    * Keep human-facing explanations, examples, and usage guides in `README.md`.
* **Respect boundaries:** Preserve safety boundaries and explicit requirements for human approval at consequential steps.
* **Scoped changes:** Avoid unrelated repository-wide rewrites. Keep your changes focused on the requested task.
* **Update the catalog:** When publishing a new skill to a `stable` or `experimental` state, ensure it is added to the root `README.md` catalog if applicable.
* **Update changelogs:** When modifying a skill's behavior, update its specific `CHANGELOG.md`.
* **Validate:** Always run the repository validation script (`python scripts/validate_repository.py`) before completing a task or submitting a pull request.
* **Templates are not skills:** Do not list the content in `templates/new-skill/` as a released skill in the root catalog.

## Working Process

1. Explore the codebase using read-only tools to understand the structure.
2. If creating a new skill, use the provided `scripts/new_skill.py` tool to initialize it.
3. Make changes and verify them locally.
4. Run validation checks.
5. Provide a summary of actions taken upon completion.
