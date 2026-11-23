# Environment preflight (read-only)

Run this before source discovery. Check availability, workspace type and target readability; do not assume Git or Repo is installed, or that the target is version-controlled. Use low-cost, targeted commands only. Failure of a VCS check does **not** block readable file-based analysis.

## Checks
1. Confirm the user-requested source path exists and is readable. If not, request a path or source material; do not invent requirements.
2. Detect Git availability (`git --version`) and Repo availability (`command -v repo`, when relevant). A tool's presence does not prove the workspace uses it.
3. Determine whether the target is inside a Git worktree (`git -C <target-dir> rev-parse --show-toplevel`) and whether its parent workspace is Repo-managed (e.g. a valid `.repo` directory). A Repo checkout contains multiple Git projects.
4. For each **relevant** Git project, record `git -C <project> rev-parse HEAD` and targeted `git -C <project> status --short -- <inspected-path>` when feasible. Dirty files may not match HEAD. For a feature spanning projects, track revisions per project; do not attribute one global SHA.
5. Record unavailable tools, unreadable paths, missing metadata and uncertain project mapping. Proceed with source inspection wherever possible.

## Git-aware source eligibility
Within each relevant Git worktree, eligible automatic analysis inputs are **tracked files** (`git ls-files --cached`) and **untracked non-ignored files** (`git ls-files --others --exclude-standard`). An untracked ignored file is excluded from automatic discovery, call tracing and evidence collection even if a direct filesystem scan can see it. Tracked files remain eligible even if `.gitignore` patterns match. Respect `.gitignore`, `.git/info/exclude`, and configured Git excludes via Git itself, rather than implementing a partial ignore parser. Apply independently for each owning Git project in a Repo checkout; do not treat the parent workspace as a single Git repository.

An explicitly user-selected ignored path is a scoped exception: inspect it if readable, label it `ignored/untracked explicit exception` in provenance, and do not generalize the exception to its whole directory. If an essential generated input is ignored but was not explicitly selected, report the dependency/gap and request authorization before reading it. Git absence or a plain-file workspace does not prohibit analysis: use the requested path boundary and state that Git ignore filtering was unavailable. Ignore rules are source-selection policy, **not** security controls.

## Safe command examples
```sh
git --version
command -v repo || true
git -C "<target-dir>" rev-parse --show-toplevel
git -C "<project-dir>" rev-parse HEAD
git -C "<project-dir>" ls-files --cached -- "<relative-target-path>"
git -C "<project-dir>" ls-files --others --exclude-standard -- "<relative-target-path>"
git -C "<project-dir>" check-ignore -v --no-index -- "<candidate-path>" # diagnostic only; tracked status still takes precedence
git -C "<project-dir>" status --short -- "<relative-target-path>"git -C "<project-dir>" status --short -- "<relative-target-path>"
```

Adapt to the active shell/platform (e.g. Windows PowerShell uses `Get-Command repo -ErrorAction SilentlyContinue`). Do not run `repo sync`, `repo forall`, a workspace-wide `git status`, installation commands, or any write/mutation operation as part of preflight. Do not assume the `repo` command must be available to analyze an existing Repo checkout.

## Minimal preflight record
| Field | Value |
|---|---|
| Source readable | yes / no / partial |
| Git command | available / unavailable / untested |
| Repo command | available / unavailable / not relevant |
| Workspace | Git / Repo multi-project / plain files / unknown |
| Relevant project root(s) and revision(s) | path @ SHA / unavailable |
| Dirty / untracked relevant paths | paths / none observed / untested |
| Limitations | |

Keep the preflight concise in the user-facing answer unless environment provenance is important to the requested result.
