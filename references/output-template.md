# Output routing and format

Default to a single Markdown **reconstructed requirements specification** in conversation. Do not write files unless requested. The specification is the deliverable; source analysis, call chains and evidence classification substantiate it. A mode controls **investigation depth**, not a mandatory count of documents or sections.

## Template routing

| Template | When to read/use | Required? |
|---|---|---|
| [Requirements](../templates/requirements.md) | Any mode with accessible source evidence; adapt table length to scope | Yes, when source evidence exists |
| [Call chain](../templates/call-chain.md) | Cross-service/IPC/async flows, multi-step state changes, ambiguous dispatch, or explicit request | Conditional |
| [Acceptance scenarios](../templates/test-scenarios.md) | Meaningful branches, permissions, failure/recovery paths, configuration variants, coverage questions, or explicit request | Conditional |

For `quick`, a short scenario-oriented requirements table with evidence and verifiable outcomes is enough unless complexity warrants more.

For `standard`, the requirements table with verifiable acceptance conditions is mandatory when source evidence is available; otherwise provide an investigation plan. Add compact call-chain and/or acceptance sections **only if the corresponding conditions above apply**. Do not force all three templates into every response. Combine selected sections in one answer/document. Create separate files only on explicit request for independent deliverables.

For `deep`, include evidence-backed requirements and the three compact matrices below when source is available, limited to the inspected user-requested behavioral scope. Add detailed call-chain and acceptance sections when justified. Do not infer completeness from the number of inspected files.

## Outcome-first organization
When source evidence identifies one or more primary observable outcomes, define their formation and interpretation contracts early in the requirements baseline, before extensive orchestration, lifecycle, storage, and reporting detail. Describe the semantic unit, trigger/boundary, relevant conditions, derivation/decision, result and failure/validity meaning as supported. Connect supporting capabilities to these foundational requirements without replacing independently testable component/interface contracts. This is an ordering and completeness principle, **not** a mandatory new section, ID category, or single business goal. If the primary outcome or part of its meaning cannot be established from inspected evidence, state the limitation and do not manufacture it.

## Deliverable priority
1. **Requirements baseline**: feature/scenario-oriented requirements, observable outcomes, relevant failure/variant constraints, and acceptance conditions. This is the main body, not a function inventory.
2. **Supporting traceability**: source locations, confidence, build/revision assumptions, and optional call-chain/state details necessary to justify the baseline.
3. **Unresolved decisions**: unknown intent, possible defects, evidence conflicts, and unvisited scope, clearly separated from requirements.

Preserve essential technical contracts (for example, a mandatory measurement protocol) while moving incidental implementation details, compiler flags, and library lists to a concise technical context section when relevant. Do not turn these facts into `NFR` without a justified quality constraint. Use compact parameter tables rather than repetitive top-level FRs when appropriate. Omit empty optional sections.

## Multi-component delivery and coverage
When the requested scope contains multiple independently observable components, organize the baseline with a concise system overview, component-level requirements for each material component, and a clearly identifiable inter-component interface contract. Sections may be grouped in one document; avoid duplicate normative statements by linking requirement IDs. Do not replace a component contract with an end-to-end description, and do not treat call-chain documentation as the sole interface specification.

Before finalizing, reconcile investigated behavior against requirements/constraints/exclusions/unknowns. Include a compact component-and-interface coverage summary when omission risk is material; it is a quality check, not a requirement to produce large matrices for single-component or narrow symbol work.

## Minimum content when source is available
- Target type, requested behavioral scope, module root(s), languages, revision/build when known, assumptions, and inspected paths
- Core observable outcome(s) and formation/interpretation contracts when identifiable, with explicit unknown semantics where evidence is insufficient
- Reconstructed requirements (ID, optional behavior kind, trigger/precondition, observable obligation, acceptance condition, evidence, confidence), grouped by feature/scenario. Normal, rejection, failure/fallback and compatibility paths belong to the same functional-behavior table when independently observable.
- Important gates/failures and relevant technical constraints when present; explicit acceptance criteria for material requirements
- Unknowns and limitations, with inferred intent, defect hypotheses, proposed changes, and evidence conflicts kept separate from implemented behavior when relevant

Do not require a separate rules/exceptional-behavior table or assign `BR` IDs to conditional branches. Keep one functional-behavior table, grouping branches when they form a single contract. Issue/conflict notes should link affected requirement IDs where available. Omit empty optional sections. Cite repository-relative paths with symbol and verified line range; include links only when a known repository URL is available. If no source is supplied, provide an investigation plan, not fabricated requirements.

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
