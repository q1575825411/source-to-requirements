# Module boundary and investigation scope

Start from a user-provided module directory, library, package, or component. Do not broaden to a monorepo-wide survey by default.

## Module profile
Record only what can be verified:
- Module name/root and revision; languages and build targets, if known
- Public interfaces: exported functions, headers, classes, APIs, IPC endpoints, callbacks, CLI/configuration inputs
- Internal implementation and state ownership
- Dependencies and external interfaces; expected inputs, outputs, errors and side effects
- Product/build/runtime gates that materially affect reachable behavior
- Exclusions and unresolved boundaries

## Boundary policy
1. Inspect module internals sufficiently to establish observable contracts.
2. Follow external callers/callees only to the nearest boundary needed to establish a trigger, precondition, contract or externally visible outcome.
3. Do not treat a dependency's entire implementation as part of the target module.
4. Expand beyond the module only when evidence is insufficient, a cross-boundary transformation changes behavior, or the user explicitly requests it. Record why expansion was necessary.
5. If the module boundary is unclear, propose a provisional scope and mark it as provisional.

## Investigation budget and stopping conditions
Start with entry points and observable outputs, then follow only paths relevant to candidate behaviors. Stop a branch when its externally visible effect and important guards are established, when the next step is outside scope, or when evidence is unavailable. Stop overall when the requested behaviors have supporting and challenging evidence, meaningful error/state branches have been considered, and remaining gaps are explicit. Never equate a bounded search with exhaustive coverage.

## Compact profile
| Item | Finding | Evidence / uncertainty |
|---|---|---|
| Scope and revision | | |
| Languages | | |
| Public entry points | | |
| Outputs / side effects | | |
| Dependencies / boundaries | | |
| Build / runtime gates | | |
| Excluded / unresolved | | |
