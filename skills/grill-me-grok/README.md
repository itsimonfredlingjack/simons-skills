# Grok Build Cross-Model Workflow

A Claude Code skill family that uses Grok Build as an independent reviewer and optional implementation agent. Claude and the operator lock the plan, Grok adversarially reviews it through an explicit resumable session, and—after human approval—Grok can implement while Claude verifies the complete diff and proof command.

*Note: The implementation source was completed locally; repository publication is pending.*

## Summary

| Field             | Value                                                                |
| ----------------- | -------------------------------------------------------------------- |
| Family            | Grok Build Cross-Model Workflow                                      |
| Commands          | `grill-me-grok`, `grill-with-docs-grok`, `grok-review`, `grok-build` |
| Host              | Claude Code                                                          |
| Independent agent | Grok Build                                                           |
| Verified CLI      | Grok Build `0.2.103` (Stable channel)                                |
| Default Model     | `grok-4.5` (may report as `grok-4.5-build`)                          |
| Status            | Experimental                                                         |
| Validation        | 36 deterministic tests; 2 authenticated live smoke tests             |
| Source            | Implementation completed locally; repository publication pending     |
| Heritage          | Matt Pocock → Chase AI / Codex workflow → Simon’s Grok adaptation    |

## Integration Architecture

The implementation uses:
* Headless Grok Build
* A repository-local Python adapter (`scripts/grok_adapter.py`)
* Explicit session IDs, never reusing review sessions for build tasks
* Repository working-directory control
* Sandbox configuration with tool allowlists and denylists
* Deterministic parsing and fail-closed checks

## Verified Facts
* **Auth:** Verified through `grok.com`; `XAI_API_KEY` is also supported.
* **Format:** Headless operation supports prompt files and JSON output, exposing session information, response text, and stop reason.
* **Session Model:** State is stored under `.grill-me-grok/session-state.json`.

## Known Limitations

* Grok Build’s built-in sandbox may soft-fail under some operating-system conditions. (Repository fingerprinting provides fail-closed mutation detection but is not a universal kernel-isolation audit).
* Shell denial for operations such as commit and push is an additional policy control; Claude’s independent diff verification remains authoritative.
* The skills currently call `scripts/grok_adapter.py` from the skill-pack checkout unless the user configures another adapter path.
* Image generation is not claimed for this family.
* ACP is not integrated.
* The complete disposable-repository build flow has not yet been live-tested end-to-end, although deterministic build gates are covered.

## Usage and Installation

*Note: Installation paths below describe Simon's verified development environment and are not yet portable universal commands.*

When source is published, the adapter can be checked via:
```bash
python3 scripts/grok_adapter.py prerequisites
```

Slash commands available in Claude Code:
* `/grill-me-grok`
* `/grill-with-docs-grok`
* `/grok-review`
* `/grok-build`

## Attribution

This work is part of a derivation chain:
* **Matt Pocock:** Original `grill-me` and `grill-with-docs` Act 1 work.
* **Peter Steinberger:** Credited build-delegation pattern.
* **Chase AI:** `grill-me-codex`, its Codex review/build workflow, packaging, and license.
* **Simon Fredling Jack:** Grok Build adaptation, adapter implementation, Grok session strategy, isolation controls, tests, documentation, and integration decisions.

All applicable MIT notices must be preserved when implementation files are imported.
