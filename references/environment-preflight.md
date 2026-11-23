# Environment preflight (read-only)

Run this before source discovery. Check availability, workspace type and target readability; do not assume Git or Repo is installed, or that the target is version-controlled. Use low-cost, targeted commands only. Failure of a VCS check does **not** block readable file-based analysis.

## Checks
1. Confirm the user-requested source path exists and is readable. If not, request a path or source material; do not invent requirements.
2. Detect Git availability (`git --version`) and Repo availability (`command -v repo`, when relevant). A tool's presence does not prove the workspace uses it.
3. Determine whether the target is inside a Git worktree (`git -C <target-dir> rev-parse --show-toplevel`) and whether its parent workspace is Repo-managed (e.g. a valid `.repo` directory). A Repo checkout contains multiple Git projects.
4. For each **relevant** Git project, record `git -C <project> rev-parse HEAD` and targeted `git -C <project> status --short -- <inspected-path>` when feasible. Dirty files may not match HEAD. For a feature spanning projects, track revisions per project; do not attribute one global SHA.
5. Record unavailable tools, unreadable paths, missing metadata and uncertain project mapping. Proceed with source inspection wherever possible.

## Safe command examples
```sh
git --version
command -v repo || true
git -C "<target-dir>" rev-parse --show-toplevel
git -C "<project-dir>" rev-parse HEAD
git -C "<project-dir>" status --short -- "<relative-target-path>"
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
