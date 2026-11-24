# Code investigation

1. Complete the read-only environment preflight first, consulting [detailed guidance](environment-preflight.md) under the resource loading policy; distinguish Git/Repo/plain-file workspaces and map each relevant path to its owning project when possible.
2. Capture requested target type (module / feature / symbol), relevant module root(s), behavioral boundary, repository branch/commit, languages and build target/flavor if available. Consult [module boundary](module-boundary.md) when boundary decisions need clarification, before expanding scope.
3. Start with target symbol/path and search definitions, references, registrations, tests and config.
4. Follow entry -> guards -> delegation -> side effects -> result/error. Record cross-thread/cross-process and cross-language transitions using [language analysis](language-analysis.md) when relevant.
5. Check feature flags, defaults, runtime properties, compile-time guards, resources, overlays and dependency injection.
6. For each edge note: caller, callee, file, verified lines, condition, sync/async, observed effect.
7. When tracing becomes too broad, stop at the nearest boundary that does not hide the user-requested outcome; for end-to-end features, cross relevant module boundaries and label only genuinely uninspected paths `not inspected`.
8. Compare branches/versions only when both source trees or trustworthy diffs are available.
9. Before finalizing, search for competing registrations, overrides, alternate branches and failure paths that could falsify each proposed behavior. Stop when material behaviors and alternatives are evidenced or explicitly unresolved.

## Bounded reading and focused discovery
- Start with scoped file paths, sizes or symbol locations and narrow searches for entry points, definitions, registrations and relevant configuration. Return only useful discovery results (paths, symbols, line locations or focused matches); narrow overly broad searches without silently treating partial results as exhaustive.
- Read small relevant files in full when useful. For large files, locate relevant definitions and read line-numbered ranges along semantic boundaries. Expand across ranges and dependencies until the relevant behavior, conditions, alternate branches, side effects and failure paths are understood. Search hits and summaries alone are not implementation evidence.
- Size each read or search batch against the effective tool response capacity, leaving headroom for wrappers and metadata. Control the combined output of all commands, files and ranges in one tool call, including loops and parallel batches. If capacity is unknown, start with modest batches and adapt to observed output; do not rely on a requested maximum output setting to prevent downstream truncation.
- Inspect results for truncation, omitted ranges or incomplete output. Treat unseen content as uninspected; recover necessary missing ranges with smaller targeted calls, retaining sufficient surrounding context. Do not repeat an entire batch merely because part was truncated. Keep discovered potentially material behaviors whose implementations are missing or truncated open in the existing investigation inventory. Before stopping, recover the necessary implementation and relevant caller/guard context, establish an evidence-backed reason for exclusion, or explicitly report the unresolved behavior and limit coverage. A symbol hit or partial response does not close the item.
- Reuse inspected source ranges, verified locations and source-linked behavior facts across tracing, extraction and validation. Reopen only when needed for missing context, competing paths, conflicting evidence, changed source or precise verification. Maintain unresolved questions alongside confirmed facts in the working context; no separate tracking file is required.
- These are per-response efficiency measures, not limits on total investigation depth, file count, lines, tokens or tool calls. Never omit material behavior or skip necessary counterexample searches to meet a reading budget.

## Source-discovery and trace filter
Build a scoped candidate set from tracked paths and untracked non-ignored paths using Git commands in the owning worktree. Do not assume `rg`'s default ignore behavior is identical to Git eligibility: `rg` can hide tracked files matching ignore patterns, while a direct path read or an unrestricted walker can include ignored untracked files. Filter search results and direct follow-up reads against the eligible set. Use `git grep` for tracked content and targeted reads/searches for eligible untracked content; keep paths limited to the requested scope. Do not use `rg --no-ignore`, `rg -uuu`, or equivalent ignore-bypassing scans by default. A user explicitly naming an ignored file authorizes only that file as an exception; record it and never silently follow its ignored neighbors. For plain files or unavailable Git, follow scope and note the limitation.

Suggested commands (adapt to repository):
```bash
git -C '<project-dir>' rev-parse HEAD
git -C '<project-dir>' status --short -- '<target-path>'
rg -n 'TargetSymbol|related_flag' relevant/path
rg -n 'TargetSymbol' --glob '*Test*' --glob '*test*'
git log --oneline -- relevant/path
nl -ba path/to/file | sed -n '120,190p'
```

Never infer runtime behavior solely from a symbol name or comment. Tests and documentation corroborate but may diverge from current implementation.
