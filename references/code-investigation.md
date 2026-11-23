# Code investigation

1. Capture requested target type (module / feature / symbol), relevant module root(s), behavioral boundary, repository branch/commit, languages and build target/flavor if available. Use [module boundary](module-boundary.md) before expanding scope.
2. Start with target symbol/path and search definitions, references, registrations, tests and config.
3. Follow entry -> guards -> delegation -> side effects -> result/error. Record cross-thread/cross-process and cross-language transitions using [language analysis](language-analysis.md) when relevant.
4. Check feature flags, defaults, runtime properties, compile-time guards, resources, overlays and dependency injection.
5. For each edge note: caller, callee, file, verified lines, condition, sync/async, observed effect.
6. When tracing becomes too broad, stop at the nearest boundary that does not hide the user-requested outcome; for end-to-end features, cross relevant module boundaries and label only genuinely uninspected paths `not inspected`.
7. Compare branches/versions only when both source trees or trustworthy diffs are available.
8. Before finalizing, search for competing registrations, overrides, alternate branches and failure paths that could falsify each proposed behavior. Stop when material behaviors and alternatives are evidenced or explicitly unresolved.

Suggested commands (adapt to repository):
```bash
git rev-parse HEAD
git status --short
rg -n 'TargetSymbol|related_flag' relevant/path
rg -n 'TargetSymbol' --glob '*Test*' --glob '*test*'
git log --oneline -- relevant/path
nl -ba path/to/file | sed -n '120,190p'
```

Never infer runtime behavior solely from a symbol name or comment. Tests and documentation corroborate but may diverge from current implementation.
