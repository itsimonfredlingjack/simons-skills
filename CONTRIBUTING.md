# Contributing to Simon's Skills

This is primarily a personal repository for Simon's curated skills. However, original contributions that adhere strictly to the repository's philosophy, conventions, and structure may be considered.

## Contribution Workflow

To add a new skill or modify an existing one, please follow this standard workflow:

1. **Create a branch:** Create a new feature branch from `main` for your work.
   ```bash
   git checkout -b feature/my-new-skill
   ```
2. **Generate the skill directory:** Use the provided script to create the boilerplate for a new skill.
   ```bash
   python scripts/new_skill.py my-new-skill
   ```
3. **Write and test the skill:**
   * Edit `skills/my-new-skill/SKILL.md` to define the agent instructions.
   * Edit `skills/my-new-skill/README.md` to explain usage to a human.
   * Ensure you test the workflow in the target environment(s).
4. **Add realistic examples:** Populate the `examples/` directory if your skill benefits from demonstrative inputs and outputs.
5. **Document targets and limitations:** Be honest about which platforms the skill works on and what its failure modes are.
6. **Update the catalog:** If the skill is ready for discovery, add it to the skill catalog in the root `README.md`.
7. **Update the changelog:** Record the addition or meaningful behavioral changes in the skill's local `CHANGELOG.md` (and the root `CHANGELOG.md` if applicable).
8. **Run validation:** Ensure the repository remains in a healthy state.
   ```bash
   python scripts/validate_repository.py
   ```
9. **Open a pull request:** Submit your changes for review. Ensure your PR description summarizes the skill's purpose and the environments it was tested in.

## Guidelines

* **Do not import external skills:** We do not accept direct copies or thin adaptations of skills from other repositories.
* **No fake skills:** Do not add placeholder or fictional skills to "pad" the repository.
* **Validation is not validation:** A skill should not be marked as `stable` solely because its Markdown passes the validation script. Stability implies the workflow has been proven effective in practice.
* **Respect the license:** Ensure any original work you contribute can be licensed under the MIT License. If you must bring in derived work, ensure attribution is preserved and licenses are compatible.
