# Output routing and format

Default to a single Markdown answer in conversation. Do not write files unless requested. A mode controls **investigation depth**, not a mandatory count of documents or sections.

## Template routing

| Template | When to read/use | Required? |
|---|---|---|
| [Requirements](../templates/requirements.md) | Any mode with accessible source evidence; adapt table length to scope | Yes, when source evidence exists |
| [Call chain](../templates/call-chain.md) | Cross-service/IPC/async flows, multi-step state changes, ambiguous dispatch, or explicit request | Conditional |
| [Acceptance scenarios](../templates/test-scenarios.md) | Meaningful branches, permissions, failure/recovery paths, configuration variants, coverage questions, or explicit request | Conditional |

For `quick`, a short requirements table with evidence is enough unless complexity warrants more.

For `standard`, the requirements table is mandatory when source evidence is available; otherwise provide an investigation plan. Add compact call-chain and/or acceptance sections **only if the corresponding conditions above apply**. Do not force all three templates into every response. Combine selected sections in one answer/document. Create separate files only on explicit request for independent deliverables.

For `deep`, include evidence-backed requirements and the three compact matrices below when source is available, limited to the inspected user-requested behavioral scope. Add detailed call-chain and acceptance sections when justified. Do not infer completeness from the number of inspected files.

## Minimum content when source is available
- Target type, requested behavioral scope, module root(s), languages, revision/build when known, assumptions, and inspected paths
- Observed behavior and requirements (ID, trigger/precondition, outcome, evidence, confidence)
- Important gates/failures when present
- Unknowns and limitations, with inferred intent clearly separated

Omit empty optional sections. Cite repository-relative paths with symbol and verified line range; include links only when a known repository URL is available. If no source is supplied, provide an investigation plan, not fabricated requirements.

## Deep-mode compact matrices

### Branch / state matrix
| Branch or state | Trigger / gate | Observed transition / outcome | Evidence | Status |
|---|---|---|---|---|
| B-001 | | | path:symbol:lines | verified / inferred / not inspected |

Include relevant failure, permission, lifecycle, and configuration branches. Use `not inspected` rather than guessing.

### Requirement-to-evidence traceability
| Requirement ID | Implementation evidence | Existing test evidence | Proposed validation | Confidence |
|---|---|---|---|---|
| FR-001 | path:symbol:lines | test path or none found in inspected scope | | confirmed / inferred / unknown |

Existing test presence is not proof of execution. Do not label proposed tests as passed.

### Scoped coverage assessment
| Dimension | Inspected / verified | Not inspected or unresolved | Next step |
|---|---|---|---|
| Entry points | | | |
| Branches / states | | | |
| Permissions / config | | | |
| IPC / lifecycle / failures | | | |
| Tests / variants | | | |

Coverage means **coverage of the declared investigation scope**, not code or test coverage percentage unless measured with appropriate tooling. Enumerate inspected entry points and paths, known unvisited branches, assumptions and possible alternate implementations. Never equate `not found` with `does not exist`. If completeness cannot be established, say so.
