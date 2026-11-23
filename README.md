# source-to-requirements

A read-only Agent Skill that reconstructs verifiable requirements from C, C++, Java, JNI, and mixed-language source. It works with Codex CLI and supported GitHub Copilot environments. The skill has no runtime dependencies or executable scripts.

## Install

Keep `SKILL.md`, `references/`, `templates/`, and `LICENSE` together in a folder named `source-to-requirements`. Do not copy only `SKILL.md` or create a second nested `source-to-requirements` folder.

### Recommended: one-command installation (Skills CLI)

Install interactively with the third-party [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add q1575825411/source-to-requirements
```

Add `-g` for a user-level installation:

```bash
npx skills add q1575825411/source-to-requirements -g
```

Skills CLI requires Node.js 22.20+. Select Codex or GitHub Copilot and check the reported destination. The installed directory should contain `SKILL.md`, `references/`, `templates/`, and `LICENSE`. If the installer omits `LICENSE`, copy it from this repository before redistributing the skill. See the [Skills CLI documentation](https://github.com/vercel-labs/skills#install-a-skill).

### Alternative: GitHub CLI one-command installation

[GitHub CLI](https://cli.github.com/) 2.90.0 or later can also install the skill. The `gh skill` command is in public preview. Because this repository keeps `SKILL.md` at its root, pass the exact `SKILL.md` path instead of relying on `skills/*/SKILL.md` discovery:

```bash
gh skill install q1575825411/source-to-requirements SKILL.md --agent github-copilot --scope user
gh skill install q1575825411/source-to-requirements SKILL.md --agent codex --scope user
```

Run the command for the agent you use. Replace `--scope user` with `--scope project` for a repository installation. Check that the installed files include `LICENSE` before redistribution.

### Manual installation (without Node.js)

Choose a destination:

| Agent / scope | Destination |
|---|---|
| Codex CLI, user-level (all projects) | `~/.agents/skills/source-to-requirements/` |
| Codex CLI, repository-level (one project) | `<your-project>/.agents/skills/source-to-requirements/` |
| GitHub Copilot (VS Code and Copilot CLI), user-level (all projects) | `~/.copilot/skills/source-to-requirements/` |
| GitHub Copilot (VS Code and Copilot CLI), repository-level (one project) | `<your-project>/.github/skills/source-to-requirements/` |

On Windows, `~` is your user home, for example `C:\\Users\\<username>`. For a repository installation, run the commands from the target source project's root. Use one location per agent to avoid conflicting copies. Manual installation requires Git only to download the repository.

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

The final command should return `True`. For Codex CLI, set `$dest` to `Join-Path $HOME ".agents\skills\source-to-requirements"`.

For a project-level Copilot installation, open PowerShell in the target project's root and set:

```powershell
$dest = Join-Path (Get-Location) ".github\skills\source-to-requirements"
```

Then run the `New-Item` and four `Copy-Item` commands above. For Codex CLI, use `.agents\skills\source-to-requirements`.

### Linux / macOS: install for VS Code Copilot (user-level)

```bash
git clone https://github.com/q1575825411/source-to-requirements.git
mkdir -p "$HOME/.copilot/skills/source-to-requirements"
cp -R source-to-requirements/SKILL.md source-to-requirements/references source-to-requirements/templates source-to-requirements/LICENSE "$HOME/.copilot/skills/source-to-requirements/"
test -f "$HOME/.copilot/skills/source-to-requirements/SKILL.md" && test -f "$HOME/.copilot/skills/source-to-requirements/LICENSE" && echo "Skill files installed"
```

For Codex CLI, replace `$HOME/.copilot/skills` with `$HOME/.agents/skills`. For a project installation, work from the target project's root and use `./.github/skills/source-to-requirements` for Copilot or `./.agents/skills/source-to-requirements` for Codex.

### Verify in VS Code GitHub Copilot

1. Open the target source project in VS Code and start a new Copilot Chat Agent session.
2. Run **Chat: Open Customizations** from the Command Palette (`Ctrl+Shift+P` on Windows/Linux), open **Skills**, and look for `source-to-requirements`.
3. Type `/` in the chat input and select `/source-to-requirements` if listed. Give it a small source-analysis task.
4. Check the agent activity to confirm it loaded `SKILL.md` and the relevant reference files.

If the skill is missing, confirm that `SKILL.md` is directly inside a folder named `source-to-requirements` and that `chat.useAgentSkills` is enabled. Then reload VS Code or start a new agent session.

Official guide: [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).

### Verify in GitHub Copilot CLI

Launch `copilot` in the source checkout. In the interactive session, run:

```text
/skills list
/skills info source-to-requirements
```

If you installed the skill during the current session, run `/skills reload` first. Copilot CLI can select the skill from its description, or you can request it by name: `Use the /source-to-requirements skill to analyze HOME-key interception and cite source evidence.` See the [Copilot CLI skill guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).

### Verify in Codex CLI

Start a new Codex CLI session in a source checkout and invoke `$source-to-requirements` with a narrow task. If Codex does not find it, check the installation path and restart the session.

### Update or uninstall

To update a manual installation, pull this repository and copy `SKILL.md`, `references/`, `templates/`, and `LICENSE` to the same destination. Remove files that no longer exist upstream. To uninstall, delete the installed `source-to-requirements` directory, not its parent `skills` directory.

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

You can also describe the task without naming the skill. Automatic selection depends on the agent and the request.

Modes are `quick`, `standard` (default), and `deep`. The target can be a module, feature, or symbol. Module requests focus on contracts, feature requests follow behavior across modules, and symbol requests start locally. The requested behavior takes precedence over module boundaries. Language guidance is in `references/language-analysis.md`; Android guidance is optional.

## Environment preflight

Before reading source, the skill checks file access and, when relevant, Git or Repo metadata. It records the owning project, revision, and relevant uncommitted changes with targeted read-only commands. Plain files remain analyzable without Git or Repo. The preflight never installs tools, syncs Repo, or changes the workspace. See `references/environment-preflight.md`.

## Output behavior

- A requirements table when source evidence is available; otherwise, an investigation plan.
- Observable behavior rather than one requirement per function or statement.
- Counterexample checks and explicit unresolved edges.
- A call chain for multi-step, cross-service, or asynchronous flows.
- Acceptance scenarios for meaningful branches, failures, permissions, or variants.
- Branch/state, traceability, and scoped coverage matrices in deep mode.

The default output is one answer. The skill creates files or separate deliverables only when requested.

Source files must be accessible in the agent workspace. The skill does not inspect a repository until invoked with access to it, and never modifies analyzed source without separate authorization.

## License

Unless otherwise noted, this project is licensed under the [MIT License](LICENSE).
