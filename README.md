# source-to-requirements

A read-only, module-first, multilingual (C, C++, Java and mixed-language) source-to-requirements Agent Skill for Codex CLI and compatible agents, including supported GitHub Copilot Agent Skills environments. No third-party dependencies or executable scripts.

## Install

Keep the directory structure intact so relative links from `SKILL.md` to `references/` and `templates/` resolve.

| Agent / scope | Destination |
|---|---|
| Codex CLI, user-level | `~/.agents/skills/source-to-requirements/` |
| Codex CLI, repository-level | `<repo>/.agents/skills/source-to-requirements/` |
| GitHub Copilot, repository-level | `<repo>/.github/skills/source-to-requirements/` |
| GitHub Copilot, user-level | `~/.agents/skills/source-to-requirements/` in supported environments |

Agent discovery paths vary by product and version. Verify the path supported by your installed Codex/Copilot version and restart or reload the agent session if necessary. Avoid duplicate installs with divergent versions.

You may also try the Skills CLI:

```bash
npx skills add https://github.com/q1575825411/source-to-requirements
```

Choose the target agent and scope in the installer; check its output to confirm discovery. Manual copy remains a fallback.

## Usage

Codex CLI example:

```text
$source-to-requirements Analyze HOME-key interception in this Android 14 checkout. mode: standard. Cite source evidence.
```

GitHub Copilot Agent example:

```text
Use the source-to-requirements skill to reconstruct HOME-key interception behavior. mode: standard. Cite source evidence.
```

Modes: `quick`, `standard` (default), `deep`. Start with a module directory or a narrowly scoped feature. The skill inspects module interfaces and behavior first, following dependencies only as needed to establish observable contracts. Language-specific investigation is routed through `references/language-analysis.md`; Android guidance is optional.

## Output behavior

- Requirements table: required when accessible source evidence supports reconstruction; otherwise provide an investigation plan.
- Requirements describe verifiable module behavior, not every internal function or code statement.
- Validation seeks counterexamples and records unresolved external or cross-language edges.
- Call-chain analysis: when multi-step, cross-service, async, or explicitly requested.
- Acceptance scenarios: when meaningful branches, errors, permissions, variants, or explicitly requested.
- Deep mode: add compact branch/state, traceability and scoped coverage matrices.
- Default output is one answer. Files are created only on request, and separate deliverables only when explicitly requested.

Source files must be accessible in the agent workspace. The skill does not inspect a repository until invoked with access to it, and never modifies analyzed source without separate authorization.
