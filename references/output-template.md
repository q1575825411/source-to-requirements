# Output routing and format

Default to a single Markdown **reconstructed requirements specification** in conversation. Do not write user-facing deliverable files unless requested; run-local investigation records follow their own persistence rules. The specification is the deliverable; source analysis, call chains and evidence classification substantiate it. A mode controls **investigation depth**, not a mandatory count of documents or sections.

## Template routing

| Template | When to read/use | Required? |
|---|---|---|
| [Requirements](../templates/requirements.md) | Any mode with accessible source evidence; adapt table length to scope | Yes, when source evidence exists |
| [Call chain](../templates/call-chain.md) | Cross-service/IPC/async flows, multi-step state changes, ambiguous dispatch, or explicit request | Conditional |
| [Acceptance scenarios](../templates/test-scenarios.md) | Meaningful branches, permissions, failure/recovery paths, configuration variants, coverage questions, or explicit request | Conditional |

For `quick`, a short scenario-oriented requirements table with evidence and verifiable outcomes is enough unless complexity warrants more.

For `standard`, the requirements table with verifiable acceptance conditions is mandatory when source evidence is available; otherwise provide an investigation plan. Add compact call-chain and/or acceptance sections **only if the corresponding conditions above apply**. Do not force all three templates into every response. Combine selected sections in one answer/document. Create separate files only on explicit request for independent deliverables.

For `deep`, perform branch/state, traceability and scoped coverage checks internally. Publish the compact matrices below only where they add material information not already represented, limited to the inspected user-requested behavioral scope. Add detailed call-chain and acceptance sections when justified. Do not infer completeness from the number of inspected files.

## Outcome-first organization
**Required when a core outcome is identifiable:** present its evidence-backed foundational FR(s), following [outcome reconstruction](requirement-extraction.md), before dependent component capabilities, orchestration, lifecycle, storage and reporting. Connect supporting capabilities without replacing independent component/interface contracts. A field/schema table or optional overview cannot substitute for formation and interpretation requirements. This is an ordering and completeness principle, not a mandatory section, ID category or single goal. If outcome semantics cannot be established, retain the limitation; if no primary outcome is supportable, use scoped contracts and state why if material.

## Dependency clarity and single-source requirements
For systems with materially connected results, briefly show the evidenced transformations between input populations, core outcomes and downstream consumers (for example raw → filtered → aggregated), with validity/acceptance gates where relevant. Use a compact table or prose only if needed; do not mandate diagrams or invent linear dependencies. The foundational FR(s) remain the authoritative specification; an outcome overview is explanatory and should reference, not duplicate, their rules.

Follow [FR/NFR classification, normative ownership and ID ordering](requirement-extraction.md). A non-normative outcome summary may refer forward to an FR; keep references resolvable and do not restate obligations.

## Supporting view ownership
FR/NFR (or explicitly linked normative constraints/subcontracts) own the full obligation and acceptance oracle. Outcome views summarize meaning and formation boundaries; component/interface views add responsibility and protocol; lineage adds transformation and dependency edges; state/failure views add transitions and propagation relationships; traceability adds missing evidence/test mappings; coverage adds scope and gaps. Reference authoritative IDs instead of copying conditions, results and failure rules. Merge or omit views that add no distinct information, including in deep mode; preserve material evidence and internal coverage checks. Use a compact structured subsection for a complex contract when a table cell is insufficient, rather than forcing long prose into repeated matrices.

## Information value and lossless view selection
Apply this check to optional views in every mode, not to the eligibility of material requirements. Do not use subjective numerical scores or length targets.
1. Identify the facts, obligations, evidence, acceptance oracles, relationships and gaps carried by the candidate view. Counterfactually remove the view: would a reader lose material behavioral meaning, implementation or acceptance determinacy, evidence reviewability, or understanding of dependencies/state/failure relationships? If yes, retain that information in an authoritative location or a linked supporting view.
2. If no material information is lost, retain a compact reference-based view only if it supports a concrete review task that would otherwise require reconstructing relationships across dispersed requirements (e.g. comparing permission gates, tracing failure propagation, or mapping tests to contracts). State its purpose through its heading or content; novelty alone is not required.
3. Otherwise merge or omit the redundant view. Prefer references over repeated normative text. When uncertain whether information is material, preserve it compactly and qualify uncertainty rather than silently dropping it.
4. Reuse the input-driven reconciliation in [evidence validation](evidence-validation.md) during consolidation, rechecking affected facts after changes. All material obligations, decisive conditions, acceptance criteria, evidence, relationships and known gaps must remain accessible through resolvable IDs or locations. Explicitly requested views remain in scope.

## Deliverable priority
1. **Requirements baseline**: feature/scenario-oriented requirements, observable outcomes, relevant failure/variant constraints, and acceptance conditions. This is the main body, not a function inventory.
2. **Supporting traceability**: source locations, confidence, build/revision assumptions, and optional call-chain/state details necessary to justify the baseline.
3. **Unresolved decisions**: unknown intent, possible defects, evidence conflicts, and unvisited scope, clearly separated from requirements.

Preserve essential technical contracts and relevant technical context according to the extraction guide; use compact parameter tables when appropriate. Omit empty optional sections.

## Multi-component delivery and coverage
When the requested scope contains multiple independently observable components, organize the baseline with a concise system overview, component-level requirements for each material component, and a clearly identifiable inter-component interface contract. Sections may be grouped in one document; avoid duplicate normative statements by linking requirement IDs. Do not replace a component contract with an end-to-end description, and do not treat call-chain documentation as the sole interface specification.

During integration, reuse the input-driven reconciliation in the evidence validation guide against requirements/constraints/exclusions/unknowns; recheck only affected statements after changes. Include a compact component-and-interface coverage summary when omission risk is material; it is a quality check, not a requirement to produce large matrices for single-component or narrow symbol work.

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
