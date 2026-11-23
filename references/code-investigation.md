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
