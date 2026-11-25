# Code investigation

1. Complete the [read-only environment preflight](environment-preflight.md) first; distinguish Git/Repo/plain-file workspaces and map each relevant path to its owning project when possible.
2. Capture requested target type (module / feature / symbol), relevant module root(s), behavioral boundary, repository branch/commit, languages and build target/flavor if available. Use [module boundary](module-boundary.md) before expanding scope.
3. Start with target symbol/path and search definitions, references, registrations, tests and config.
4. Follow entry -> guards -> delegation -> side effects -> result/error. Record cross-thread/cross-process and cross-language transitions using [language analysis](language-analysis.md) when relevant.
5. Check feature flags, defaults, runtime properties, compile-time guards, resources, overlays and dependency injection.
6. For each edge note: caller, callee, file, verified lines, condition, sync/async, observed effect.
7. When tracing becomes too broad, stop at the nearest boundary that does not hide the user-requested outcome; for end-to-end features, cross relevant module boundaries and label only genuinely uninspected paths `not inspected`.
8. Compare branches/versions only when both source trees or trustworthy diffs are available.
9. Before finalizing, search for competing registrations, overrides, alternate branches and failure paths that could falsify each proposed behavior. Stop when material behaviors and alternatives are evidenced or explicitly unresolved.

## Local behavior analysis

Apply these four actions within the existing investigation batch, proportionally to scope and mode. They guide the first investigation, not a separate pass or a new artifact.

1. **Define the behavior boundary.** Select a local behavior within the requested scope and current investigation units. Identify its relevant triggers and observable outcomes, state changes, persisted effects or failures. A boundary is not necessarily a function or a linear call chain: it may span events, callbacks, IPC, configuration inputs and multiple result endpoints.
2. **Trace formation paths.** Start from the relevant triggers and follow how control, data and state produce the observed effects or failures. Use an evidenced ordinary path as a reference when available; do not assume a single main path or let it exclude other material outcomes.
3. **Compare material path differences.** When a condition or source can change the behavior, follow the relevant alternative and compare its governing conditions, effects and failure scope with the reference path. Preserve both shared rules and differences, including defaults, early returns and fallback where relevant. Differences may arise from configuration precedence, input formats or versions, distinct entry points, or event ordering as well as explicit branches. Compare only differences within the requested scope that can materially change behavior; these examples are not a mandatory search checklist. Do not enumerate equivalent or irrelevant paths.
4. **Record established behavior.** Capture the confirmed shared and differing rules in the existing [behavior ledger](behavior-ledger.md) at the current batch checkpoint, before unrelated investigation or structural inspected status. Group related paths only when the resulting fact preserves their material conditions and effects. Keep requirement classification and grouping for later abstraction.

During tracing, use targeted reverse investigation when the current path cannot explain a result, when a result has multiple possible sources, or when later writes or restored state may alter it. Trace relevant producers, overrides and consumers as needed to resolve the question. This is not a mandatory reverse pass. When new evidence changes an earlier conclusion, revise or supplement the existing fact using the ledger correction rules.

A local investigation is sufficient when the relevant triggers, formation paths, observable effects and material alternatives can be explained from evidence. Explicitly retain unresolved or uninvestigated portions and follow existing structural status rules; do not treat a file read or a named behavior as sufficient. This does not require exhaustive control-flow enumeration or a second full investigation.

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
