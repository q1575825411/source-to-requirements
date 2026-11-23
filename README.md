# source-to-requirements

A read-only, scope-aware, multilingual (C, C++, Java and mixed-language) source-to-requirements Agent Skill for Codex CLI and compatible agents, including supported GitHub Copilot Agent Skills environments. No third-party dependencies or executable scripts.

## Install

The skill consists of `SKILL.md`, `references/`, and `templates/`. **Copy all three** into a folder named `source-to-requirements`; do not copy just `SKILL.md` or nest the folder twice. No Python, Node.js, or build dependencies are needed to run the skill. Git is only needed for the download commands below.

### Choose an installation location

| Agent / scope | Destination |
|---|---|
| Codex CLI, user-level (all projects) | `~/.agents/skills/source-to-requirements/` |
| Codex CLI, repository-level (one project) | `<your-project>/.agents/skills/source-to-requirements/` |
| GitHub Copilot in VS Code, user-level (all projects) | `~/.copilot/skills/source-to-requirements/` |
| GitHub Copilot in VS Code, repository-level (one project) | `<your-project>/.github/skills/source-to-requirements/` |

On Windows, `~` means your user home (for example, `C:\\Users\\<username>`). For a repository-level installation, run the commands from the **target source project's root**, not the skill repository. Choose one location for each agent to avoid conflicting versions.

### Windows PowerShell: install for VS Code Copilot (user-level)

```powershell
git clone https://github.com/q1575825411/source-to-requirements.git
$src = (Resolve-Path .\source-to-requirements).Path
$dest = Join-Path $HOME ".copilot\skills\source-to-requirements"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item "$src\SKILL.md" -Destination $dest -Force
Copy-Item "$src\references" -Destination $dest -Recurse -Force
Copy-Item "$src\templates" -Destination $dest -Recurse -Force
Test-Path (Join-Path $dest "SKILL.md")
```

The final command should return `True`. To install for **Codex CLI** instead, change `$dest` to `Join-Path $HOME ".agents\skills\source-to-requirements"`.

For **project-level Copilot** installation, open a PowerShell terminal in your target project's root and set:

```powershell
$dest = Join-Path (Get-Location) ".github\skills\source-to-requirements"
```

Then run the `New-Item` and three `Copy-Item` commands above. For project-level Codex CLI, use `.agents\skills\source-to-requirements` instead.

### Linux / macOS: install for VS Code Copilot (user-level)

```bash
git clone https://github.com/q1575825411/source-to-requirements.git
mkdir -p "$HOME/.copilot/skills/source-to-requirements"
cp -R source-to-requirements/SKILL.md source-to-requirements/references source-to-requirements/templates "$HOME/.copilot/skills/source-to-requirements/"
test -f "$HOME/.copilot/skills/source-to-requirements/SKILL.md" && echo "Skill files installed"
```

For **Codex CLI**, replace `$HOME/.copilot/skills` with `$HOME/.agents/skills`. For **project-level** installation, replace the destination with `./.github/skills/source-to-requirements` (Copilot) or `./.agents/skills/source-to-requirements` (Codex), while working in the target project's root.

### Alternative: Skills CLI

If you already use the third-party Skills CLI, you can try:

```bash
npx skills add https://github.com/q1575825411/source-to-requirements
```

Select the intended agent and scope, and check the installer's reported destination. This is an optional convenience, **not** a dependency of this skill.

### Verify in VS Code GitHub Copilot

1. Open the target source project in VS Code and start a **new Copilot Chat Agent session**.
2. Run **Chat: Open Customizations** from the Command Palette (`Ctrl+Shift+P` on Windows/Linux), then open **Skills**. Look for `source-to-requirements`.
3. Type `/` in the chat input and select `/source-to-requirements` if listed. Give it a small source-analysis task.
4. Check the agent activity to confirm it loaded `SKILL.md` and accessed relevant reference files. You can also ask in natural language; automatic selection depends on the task matching the skill description.

If the skill is missing, check that the parent folder is named exactly `source-to-requirements`, `SKILL.md` is immediately inside it, and `chat.useAgentSkills` is enabled (normally on by default). Reload VS Code or start a new agent session after installation. Make sure the selected agent harness supports the chosen location.

Official guide: [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

### Verify in Codex CLI

Start a new Codex CLI session in a source checkout and invoke `$source-to-requirements` with a narrow task, or ask Codex to use the skill. If it is not discovered, verify the selected user/project path and restart the session.

### Update or uninstall

To update a manual installation, pull the latest changes in the downloaded `source-to-requirements` repository and copy `SKILL.md`, `references/`, and `templates/` into the **same destination** again. Remove obsolete files from a prior installation if the repository structure changes. To uninstall, delete only the installed `source-to-requirements` directory, not its parent `skills` directory.

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
