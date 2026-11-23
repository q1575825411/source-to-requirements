# source-to-requirements

A read-only, scope-aware, multilingual (C, C++, Java and mixed-language) source-to-requirements Agent Skill for Codex CLI and compatible agents, including supported GitHub Copilot Agent Skills environments. No third-party dependencies or executable scripts.

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

Modes: `quick`, `standard` (default), `deep`. Start with a module, feature or symbol. A module request follows module contracts; a feature request follows the end-to-end behavior across modules as necessary; a symbol request starts locally. The user-requested behavioral scope always takes precedence over module boundaries. Language-specific investigation is routed through `references/language-analysis.md`; Android guidance is optional.

## Environment preflight

Before source discovery, the skill checks source readability, Git availability, and Repo availability when relevant. It identifies the owning Git project(s), available revisions, and relevant uncommitted changes using targeted read-only commands. Git/Repo are optional: readable plain source files can still be analyzed. It never installs tools, syncs Repo, or modifies the workspace during preflight. See `references/environment-preflight.md`.

## Output behavior

- Requirements table: required when accessible source evidence supports reconstruction; otherwise provide an investigation plan.
- Requirements describe verifiable observable behavior, not every internal function or code statement.
- Validation seeks counterexamples and records unresolved external or cross-language edges.
- Call-chain analysis: when multi-step, cross-service, async, or explicitly requested.
- Acceptance scenarios: when meaningful branches, errors, permissions, variants, or explicitly requested.
- Deep mode: add compact branch/state, traceability and scoped coverage matrices.
- Default output is one answer. Files are created only on request, and separate deliverables only when explicitly requested.

Source files must be accessible in the agent workspace. The skill does not inspect a repository until invoked with access to it, and never modifies analyzed source without separate authorization.
