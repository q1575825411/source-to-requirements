# Code investigation

1. Capture repository root, branch, commit, target product and build flavor if available.
2. Start with target symbol/path and search definitions, references, registrations, tests and config.
3. Follow entry -> guards -> delegation -> side effects -> result/error. Record cross-thread/cross-process transitions.
4. Check feature flags, defaults, runtime properties, compile-time guards, resources, overlays and dependency injection.
5. For each edge note: caller, callee, file, verified lines, condition, sync/async, observed effect.
6. When tracing becomes too broad, stop at boundary and label it `not inspected`.
7. Compare branches/versions only when both source trees or trustworthy diffs are available.

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
