# source-to-requirements

A read-only, scope-aware, multilingual (C, C++, Java and mixed-language) source-to-requirements Agent Skill for Codex CLI and compatible agents, including supported GitHub Copilot Agent Skills environments. No third-party dependencies or executable scripts.

## Install

The skill consists of `SKILL.md`, `references/`, `templates/`, and `LICENSE`. **Copy all four** into a folder named `source-to-requirements`; do not copy just `SKILL.md` or nest the folder twice. The skill itself has no Python, Node.js, or build dependencies; the optional installer below does require Node.js.

### Recommended: one-command installation (Skills CLI)

Use the third-party [Skills CLI](https://github.com/vercel-labs/skills) to install interactively:

```bash
npx skills add q1575825411/source-to-requirements
```

For a user-level installation available across projects:

```bash
npx skills add q1575825411/source-to-requirements -g
```

Requires **Node.js 22.20+** for the installer. Select **Codex** or **GitHub Copilot** and confirm the destination reported by the CLI. The skill itself does **not** require Node.js. After installation, verify that `SKILL.md`, `references/`, `templates/`, and `LICENSE` are present in the installed directory. Installer behavior can vary by version; if `LICENSE` is missing, copy it from this repository into the installed skill directory before redistributing it. See the [Skills CLI documentation](https://github.com/vercel-labs/skills#install-a-skill).

### Alternative: GitHub CLI one-command installation

With [GitHub CLI](https://cli.github.com/) version 2.90.0 or later (the `gh skill` feature is in public preview), install directly for a specific agent. This repository keeps `SKILL.md` at its root, so pass the **exact `SKILL.md` path**, rather than the skill name, to bypass standard `skills/*/SKILL.md` discovery:

```bash
gh skill install q1575825411/source-to-requirements SKILL.md --agent github-copilot --scope user
gh skill install q1575825411/source-to-requirements SKILL.md --agent codex --scope user
```

Run **one** command for your intended agent, not both unless you use both. Replace `--scope user` with `--scope project` for a repository-specific installation. GitHub CLI and the third-party Skills CLI are alternative installers; neither is required to run the skill. Confirm the installed files include `LICENSE` before redistribution.

### Manual installation (without Node.js)

Choose a destination:

| Agent / scope | Destination |
|---|---|
| Codex CLI, user-level (all projects) | `~/.agents/skills/source-to-requirements/` |
| Codex CLI, repository-level (one project) | `<your-project>/.agents/skills/source-to-requirements/` |
| GitHub Copilot (VS Code and Copilot CLI), user-level (all projects) | `~/.copilot/skills/source-to-requirements/` |
| GitHub Copilot (VS Code and Copilot CLI), repository-level (one project) | `<your-project>/.github/skills/source-to-requirements/` |

On Windows, `~` means your user home (for example, `C:\\Users\\<username>`). For a repository-level installation, run the commands from the **target source project's root**, not the skill repository. Choose one location for each agent to avoid conflicting versions. Manual installation uses Git for downloading the source.

### Windows PowerShell: install for VS Code Copilot (user-level)

```powershell
git clone https://github.com/q1575825411/source-to-requirements.git
$src = (Resolve-Path .\source-to-requirements).Path
$dest = Join-Path $HOME ".copilot\skills\source-to-requirements"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item "$src\SKILL.md" -Destination $dest -Force
Copy-Item "$src\LICENSE" -Destination $dest -Force
Copy-Item "$src\references" -Destination $dest -Recurse -Force
Copy-Item "$src\templates" -Destination $dest -Recurse -Force
(Test-Path (Join-Path $dest "SKILL.md")) -and (Test-Path (Join-Path $dest "LICENSE"))
```

The final command should return `True`. To install for **Codex CLI** instead, change `$dest` to `Join-Path $HOME ".agents\skills\source-to-requirements"`.

For **project-level Copilot** installation, open a PowerShell terminal in your target project's root and set:

```powershell
$dest = Join-Path (Get-Location) ".github\skills\source-to-requirements"
```

Then run the `New-Item` and four `Copy-Item` commands above. For project-level Codex CLI, use `.agents\skills\source-to-requirements` instead.

### Linux / macOS: install for VS Code Copilot (user-level)

```bash
git clone https://github.com/q1575825411/source-to-requirements.git
mkdir -p "$HOME/.copilot/skills/source-to-requirements"
cp -R source-to-requirements/SKILL.md source-to-requirements/references source-to-requirements/templates source-to-requirements/LICENSE "$HOME/.copilot/skills/source-to-requirements/"
test -f "$HOME/.copilot/skills/source-to-requirements/SKILL.md" && test -f "$HOME/.copilot/skills/source-to-requirements/LICENSE" && echo "Skill files installed"
```

For **Codex CLI**, replace `$HOME/.copilot/skills` with `$HOME/.agents/skills`. For **project-level** installation, replace the destination with `./.github/skills/source-to-requirements` (Copilot) or `./.agents/skills/source-to-requirements` (Codex), while working in the target project's root.

### Verify in VS Code GitHub Copilot

1. Open the target source project in VS Code and start a **new Copilot Chat Agent session**.
2. Run **Chat: Open Customizations** from the Command Palette (`Ctrl+Shift+P` on Windows/Linux), then open **Skills**. Look for `source-to-requirements`.
3. Type `/` in the chat input and select `/source-to-requirements` if listed. Give it a small source-analysis task.
4. Check the agent activity to confirm it loaded `SKILL.md` and accessed relevant reference files. You can also ask in natural language; automatic selection depends on the task matching the skill description.

If the skill is missing, check that the parent folder is named exactly `source-to-requirements`, `SKILL.md` is immediately inside it, and `chat.useAgentSkills` is enabled (normally on by default). Reload VS Code or start a new agent session after installation. Make sure the selected agent harness supports the chosen location.

Official guide: [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

### Verify in GitHub Copilot CLI

Launch `copilot` in the source checkout. In the interactive session, run:

```text
/skills list
/skills info source-to-requirements
```

If the skill was installed while the session was running, use `/skills reload` first. To request it explicitly, enter `Use the /source-to-requirements skill to analyze HOME-key interception and cite source evidence.` Copilot CLI can also select skills automatically based on their descriptions. See the [official Copilot CLI skill guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).

### Verify in Codex CLI

Start a new Codex CLI session in a source checkout and invoke `$source-to-requirements` with a narrow task, or ask Codex to use the skill. If it is not discovered, verify the selected user/project path and restart the session.

### Update or uninstall

To update a manual installation, pull the latest changes in the downloaded `source-to-requirements` repository and copy `SKILL.md`, `references/`, `templates/`, and `LICENSE` into the **same destination** again. Remove obsolete files from a prior installation if the repository structure changes. To uninstall, delete only the installed `source-to-requirements` directory, not its parent `skills` directory.

## Usage

Codex CLI example:

```text
$source-to-requirements Analyze HOME-key interception in this Android 14 checkout. mode: standard. Cite source evidence.
```

GitHub Copilot Agent (VS Code) example:

```text
/source-to-requirements

Analyze HOME-key interception in this Android 14 checkout. mode: standard. Trace the end-to-end behavior and cite source evidence.
```

GitHub Copilot CLI example:

```text
Use the /source-to-requirements skill to analyze HOME-key interception in this Android 14 checkout. mode: standard. Cite source evidence.
```

You can also request the analysis in natural language without naming the skill; automatic selection depends on the agent recognizing the skill and matching its description.

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

## License

Unless otherwise noted, this project is licensed under the [MIT License](LICENSE).
