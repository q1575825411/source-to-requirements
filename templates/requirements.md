# Reconstructed requirements baseline: <module / feature / symbol>

- Target type / name: module | feature | symbol; name:
- Repository / commit:
- Module root(s) / inspected paths:
- Languages (C / C++ / Java / JNI / other, as applicable):
- Build target / configuration (if known):
- Product / Android version (if applicable):
- Mode / behavioral scope / exclusions:
- Important assumptions:

## Core outcome / formation contract (when identifiable)

Describe the primary observable result(s), decision(s), state change(s), or artifact(s) within the requested scope. Define what each represents, its inputs and triggering conditions, the operation/decision boundary, derivation and result/validity/failure semantics **only as supported by evidence**. Put independently testable obligations in the functional requirements table below and cross-reference their FR IDs; do not create duplicate normative statements or assume a single outcome. If none can be established, state the gap or omit this optional section for a narrow scope.

| Outcome / related FR | Meaning and unit | Formation trigger / boundary | Conditions / derivation | Result and failure semantics | Evidence / unknowns |
|---|---|---|---|---|---|

**Required check when an outcome is identifiable:** the first functional requirements must include a source-linked, testable formation contract defining its semantic unit, operation/decision boundaries, derivation, and success/failure meaning where evidenced. A filled outcome table or field list alone does not satisfy this check. Use `UNK` for unresolved formation semantics; do not infer original stakeholder intent. For multiple independent outcomes, cover each; for no supported primary outcome, omit the table without inventing one.

## Outcome dependencies / data lineage (when material)

| Producer / related FR | Input population / state | Transformation or gate | Consumer / resulting population | Evidence / unknowns |
|---|---|---|---|---|

Include only when related outcomes' data lineage materially affects interpretation, validity, or downstream outputs. Reference authoritative FRs rather than duplicating formulas; preserve branches and independent outcomes without forcing a linear pipeline.

## Component and interface scope (when multiple independent contracts exist)

| Component / interface | Entry / inputs | Modes / lifecycle | Outputs / failures | Evidence / coverage |
|---|---|---|---|---|

Identify independently invocable components and material interaction boundaries, not every source file. A system overview cannot replace component requirements.

## Reconstructed functional requirements (evidence-backed)

Organize by feature/scenario rather than by source file or function. Use one table for normal behavior, rejection, error/fallback, and compatibility paths. The behavior-kind label is optional; group branches that form one independently verifiable contract. Do not create a `BR` ID solely for a source conditional.

| ID | Feature / scenario | Trigger / precondition | Required observable outcome | Acceptance condition | Evidence (path:symbol:lines) | Confidence |
|---|---|---|---|---|---|---|
| FR-001 | | | | | | confirmed |

## Inter-component interface contracts (when relevant)

| Related FRs | Producer → consumer | Invocation / message / data contract | Ordering / timeout / failure semantics | Acceptance condition | Evidence |
|---|---|---|---|---|---|

Use this section for independently meaningful interface obligations; cross-reference FRs rather than repeating them. Omit for a single component without material boundaries.

## Technical and configuration constraints (when relevant)

Keep required protocol/compatibility parameters here or link them to their parent FR. Build flags, dependency lists and implementation mechanisms are supporting context, not automatically NFRs.

| Related requirement | Parameter / condition | Constraint | Evidence |
|---|---|---|---|

Use one authoritative home for each normative rule. If a quality property merely restates a functional check (for example, a hash verification or atomic replace), reference the parent FR's acceptance criteria rather than duplicating it here. Only include an NFR with a distinct, independently evidenced and testable quality obligation. Assign IDs after organizing the final requirements; keep normative table first appearances sequential.

## Nonfunctional requirements (only when evidenced)
| ID | Quality attribute / condition | Verifiable constraint | Acceptance condition | Evidence | Confidence |
|---|---|---|---|---|---|

## Inferred intent (only if supported as a hypothesis; not confirmed)
| Hypothesis | Rationale | Evidence | Validation needed |
|---|---|---|---|

## Defect hypotheses and evidence conflicts (only if found)
| Type | Related requirement ID | Observation / conflicting evidence | Validation needed |
|---|---|---|---|

## Extraction coverage reconciliation (when material)

| Component / interaction | Investigated behavior | Requirement / constraint / exclusion / unknown | Coverage gap |
|---|---|---|---|

Use this as a compact audit: inspected source alone is not sufficient to mark requirements coverage complete. Do not list every function.

## Unknowns and uncovered scope
| ID | Question | Inspected scope | Next verification |
|---|---|---|---|
| UNK-001 | | | |
