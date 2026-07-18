# Authoring Guide

This document outlines the core principles for authoring skills in Simon's field kit. A skill is more than a prompt—it is a robust, well-bounded workflow.

## Authoring Principles

When creating a new skill, adhere to the following principles:

1. **Inspect before instructing:** Agents should always gather context about the environment and the target files before making state changes. Embed discovery steps early in your skill.
2. **Separate planning from implementation:** The workflow should require the agent to formulate a plan (and optionally seek review) before executing any modifications.
3. **Make permissions explicit:** Boundaries must be clear. If a skill is restricted to certain directories or actions, say so unequivocally.
4. **Never let an agent silently widen scope:** The skill must constrain the agent to the defined objective. Feature creep during autonomous execution is a failure mode.
5. **Preserve human approval at consequential boundaries:** High-risk actions (commits, deploys, large deletes) must require the operator's explicit confirmation.
6. **Distinguish claims from verified evidence:** Do not assume an action succeeded just because the command was sent. The workflow must include verification steps (e.g., reading a file after writing it).
7. **Define failure behavior:** What should the agent do when a step fails? Explicitly outline fallback mechanisms or stopping conditions.
8. **Prefer reusable workflows over oversized prompts:** If a skill becomes too large, consider breaking it into smaller, composable skills or moving complex deterministic logic into a script.
9. **Keep model-specific assumptions visible:** If a skill relies heavily on a specific model's reasoning style or context window, note it in the limitations.
10. **Optimize for operator control rather than maximum autonomy:** The goal is a highly capable assistant, not an unsupervised background process. Keep the human in the loop.

## The Authoring Process

1. **Define the Goal:** What specific problem does this skill solve?
2. **Identify the Target:** Which platforms (e.g., Claude Code, Jules) will execute this?
3. **Draft `SKILL.md`:** Write the operational instructions meant for the agent. Use clear, imperative language.
4. **Draft `README.md`:** Write the usage instructions meant for the human operator.
5. **Test and Iterate:** Run the skill in its intended environment. Refine the instructions based on where the agent gets confused or deviates from the plan.
