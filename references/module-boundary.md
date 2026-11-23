# Module boundary and investigation scope

Choose the investigation boundary from the **user's target**, not a universal module limit. For a module request, start at the provided directory/library/package/component. For a feature request, identify the entry-to-outcome path even when it crosses multiple modules. For a symbol request, start locally and expand only as necessary. Never broaden into unrelated repository areas.

## Scope routing
| User target | Boundary | Expansion rule |
|---|---|---|
| Module | Module contract, inputs, outputs, errors and relevant dependencies | Follow outside only as needed to establish the module's contract |
| Feature | End-to-end trigger-to-observable-outcome path | Cross every relevant module, process or language boundary until the requested outcome is explained |
| Symbol / function | Local behavior and relevant callers/callees | Expand when required to establish trigger or observable effect |

A module boundary is a navigation aid, **not** a reason to truncate an explicitly requested feature. For example, HOME-key interception may require InputDispatcher, policy, ATMS and Launcher paths if they affect the requested behavior.

## Module profile
Record only what can be verified:
- Module name/root and revision; languages and build targets, if known
- Public interfaces: exported functions, headers, classes, APIs, IPC endpoints, callbacks, CLI/configuration inputs
- Internal implementation and state ownership
- Dependencies and external interfaces; expected inputs, outputs, errors and side effects
- Product/build/runtime gates that materially affect reachable behavior
- Exclusions and unresolved boundaries

## Boundary policy
1. Respect the requested module, feature or symbol scope. Inspect relevant internals sufficiently to establish observable contracts.
2. For module requests, follow external callers/callees to the nearest boundary sufficient to establish the contract. For feature requests, continue across boundaries until the end-to-end observable outcome is explained.
3. Do not analyze unrelated parts of a dependency; inspect only the paths affecting the requested behavior.
4. Cross-module expansion is expected for feature requests and conditional for module/symbol requests. Record relevant edges and why they matter.
5. If the module boundary is unclear, propose a provisional scope and mark it as provisional.

## Investigation budget and stopping conditions
Start with entry points and observable outputs, then follow only paths relevant to candidate behaviors. Stop a branch when the requested observable effect and important guards are established, when the next step is unrelated to the requested scope, or when evidence is unavailable. Do not stop at a module boundary if it hides a feature outcome. Stop overall when the requested behaviors have supporting and challenging evidence, meaningful error/state branches have been considered, and remaining gaps are explicit. Never equate a bounded search with exhaustive coverage.

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
