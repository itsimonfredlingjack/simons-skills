---
name: "grill-me-grok"
description: "A Claude Code skill family that uses Grok Build as an independent reviewer and optional implementation agent."
author: Simon Fredling Jack
version: pending
status: experimental
targets:
  - claude-code
tags:
  - planning
  - review
  - build
---

# Agent Instructions: Grok Build Cross-Model Workflow

*Note: This is the operational payload for the agent. The human-facing explanation is in README.md. Note that the implementation source is completed locally; repository publication is pending.*

## 1. Activation Conditions
Invoke this workflow when the user requests a cross-model implementation using Grok Build as an adversarial reviewer or build agent for a planned task.

## 2. Objective
To independently review plans and optionally build them using a distinct Grok Build session, ensuring that the same model does not serve as the sole planner, implementer, and evaluator.

## 3. Prerequisites
- The host environment must be Claude Code.
- `scripts/grok_adapter.py` (Local Python adapter) must be available.
- Headless Grok Build available (typically configured via `~/.grok/bin/grok`).

## 4. Workflow Stages

This family executes a three-act structure:

1. **Act 1 — Plan (`grill-me-grok`, `grill-with-docs-grok`)**
   - Claude and the operator resolve the requirements and produce the `PLAN.md`.

2. **Act 2 — Independent Review (`grok-review`)**
   - Grok reviews the plan adversarially through a dedicated resumable session.
   - Claude maintains an append-only `PLAN-REVIEW-LOG.md`.
   - Every review continuation resumes that exact UUID session ID.

3. **Act 3 — Optional Build (`grok-build`)**
   - After explicit human sign-off, Grok implements the approved plan using a *new, separate* UUID.
   - Claude then inspects the full diff and independently runs the proof command.

## 5. Safety Boundaries
- **Review Isolation:** Review sessions operate with `--sandbox read-only`, using a strict allowlist (e.g., `read_file`, `grep`, `list_dir`) and explicit denial of mutation/shell capabilities.
- **Fail-Closed Mutation:** The adapter performs before-and-after repository fingerprinting. If mutation is detected, it triggers a `REVIEW_MUTATION` failure. If isolation cannot be established, it triggers `ISOLATION_UNAVAILABLE`.
- **Human Gates:** No implementation starts before human sign-off.
- **Commit Boundary:** Grok does not commit or push. Shell operations are denied; Claude verifies the diff authoritatively.

## 6. Output Contract
- Generation of `PLAN.md`.
- Generation of append-only `PLAN-REVIEW-LOG.md`.
- Verified implementation diff (pending human approval).

## 7. Error Handling & Failure Behavior
- If Grok Build’s built-in sandbox soft-fails under host OS conditions, the deterministic fail-closed repository fingerprinting mitigates the risk.
- Ensure sessions are strictly scoped; never use `--continue` or implicit "most recent session" logic.

## 8. Completion Criteria
The workflow is complete when Claude independently runs the proof command on the Grok-implemented code and verifies the diff against the locked plan.
