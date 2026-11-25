# Requirement extraction

## Behavioral record
- Actor/caller
- Trigger and preconditions
- Configuration/build/permission guards
- Decision branches and thresholds
- Observable behavior and side effects
- Error, fallback, timeout, cancellation
- State persistence and cleanup
- Evidence and confidence

Convert to verifiable statements: `When [trigger], if [conditions], the system [observable behavior]; otherwise [fallback].`

## Fact-driven organization and abstraction
Use the explicitly reloaded active ledger facts and source-linked outcome/lineage records as input. Work through coherent behavior groups rather than summarizing the entire investigation at once. For each group:

1. Identify the distinct material rules and variants in the input; organize them by observable contract before choosing FR/NFR or supporting context. Core outcomes determine presentation order, not which material facts survive.
2. Express shared rules and material variants, preserving exact conditions, results, failure scope, compatibility and evidence. Classify obligations and supporting facts only after their meaning is established; retain technical facts, conflicts and unknowns in appropriate destinations.
3. Compare the resulting draft statements and linked constraints directly with the group's input semantics using [evidence validation](evidence-validation.md). Repair missing or weakened rules before moving to an unrelated group; split or cross-reference if needed to preserve meaning. A topic match is not sufficient.

Integrate the groups and reconcile cross-group relationships and changes. This is the existing abstraction operation, not a new mapping artifact, mandatory per-fact write or second source investigation. Its coverage target is recorded material behavior, not all possible source behavior.

## Requirements abstraction: contract versus mechanism
- Write requirements from the perspective of the system's observable obligations: trigger, conditions, outcome, rejection/failure behavior and relevant constraints. Organize by feature and scenario, not by implementation file/function order.
- Preserve an implementation-specific parameter, API, timing or method when it defines the tested contract, interoperability, compatibility, or an essential measurement protocol. Otherwise retain it in technical notes/evidence rather than making it a standalone requirement.
- Classify build architecture, compiler flags, linked libraries, and internal algorithms as build/deployment facts or implementation notes unless evidence establishes a genuine product-level requirement. Do not label all technical facts `NFR`.
- A source-observed behavior is a candidate reconstructed requirement, not proof that stakeholders intended or approved it. When suspicious, state the observed contract separately from its defect hypothesis and desired change.
- Distinguish **known behavior** from **unknown intent**: a verified fixed path or guard is not `UNK` merely because its rationale is unclear; put the rationale question in `UNK` and link the observed behavior.

## Core outcome and formation-contract reconstruction
Before consolidating a capability inventory into requirements, ask within the requested scope:
1. What observable result, decision, state transition, or artifact is the system/feature principally producing? There may be multiple; for a narrow symbol or generic library, a primary outcome may be indeterminate.
2. What is the semantic unit of that result, its inputs and conditions, and what precisely initiates and completes its formation? Identify the boundary of the operation/decision, not merely the presence of output fields.
3. How is the result derived or classified, including relevant algorithms/formulas, timing/ordering, units, validity, errors, and distinction between attempted, produced, and accepted results **when supported by evidence**?
4. Which observed capabilities directly produce the result, establish its conditions, coordinate repetition, or preserve/report it? Express those as supporting or constraining contracts rather than substituting them for the foundational contract.
5. Can a reader understand how the key outcome arises without first reading orchestration, persistence, or implementation walkthroughs? If not, revise the requirements order or fill a substantiated contract gap.

Treat this as **goal-oriented reverse inference from implemented behavior**, not proof of original business intent. Do not assert an original stakeholder objective, SLA, success threshold, quality guarantee, or result-validity rule merely because code has a field, constant, or comment. Mark unsupported semantics unresolved. Preserve multiple equally important outcomes when appropriate; do not force a single central requirement for utility libraries, narrowly scoped symbols, or systems where the evidence does not identify one. The foundational contract can be a small group of existing FRs, not a mandatory new ID series or a boilerplate section.

## Outcome-formation working record (required when identifiable)
Build this **before** assigning or grouping functional requirements. For each primary outcome, capture: (a) observable meaning and unit, (b) inputs, conditions and actor, (c) exact initiation/completion or decision boundary, (d) derivation/transform/decision logic including units and formulas if evidenced, (e) attempted versus emitted versus accepted/successful result and error behavior, (f) source evidence or unresolved question for each field, (g) producing, conditioning, coordinating and preserving capabilities. Do not substitute a log schema, function name, process topology, or output count for (c)–(e).

Convert the record into one or more **independently verifiable foundational FRs**, and put these before dependent orchestration and lifecycle FRs in the final baseline. Other components may refer to these FRs while retaining their own contracts. If a field is not provable, say so specifically rather than fabricating a formula or validity rule. For multi-outcome systems, repeat only for material outcomes; for a utility or narrow symbol with no supported primary outcome, document that finding briefly and use normal scoped reconstruction.

**Failure example (generic):** a report lists a computed metric and its output fields, then exhaustively documents scheduling and archiving, but never defines the metric's measurement/decision boundary or calculation. **Passing example (generic):** the report first defines what one result represents, when the operation begins and ends, how it is computed/classified, and how failure differs from a valid result, then traces orchestration and storage to that contract. These are structural tests, not domain-specific requirements.

## Related outcomes and data lineage (conditional)
When several material outcomes are connected, construct a compact **source-linked dependency map before drafting**: producer outcome and input population → transformation/filter/aggregation/decision gate → consumer outcome and population. Record whether each is raw, filtered, derived, accepted, persisted, or presentation-only **only if code establishes that distinction**. Check whether filtering mutates the source record or creates a separate view, whether validation and performance judgments use different populations, and which downstream outputs/caches are invalidated by a rule change. Preserve branching, fan-in, fan-out, and independent outcomes; do not force a single pipeline or make a diagram mandatory. Use `unknown` for unsupported edges. Include a small lineage table or prose only when it materially improves the final requirements.

## FR/NFR and normative-rule ownership
First extract candidate contracts without IDs. Classify an **FR** as an independently observable behavior, including rejection, validation, reproducible algorithmic output, and persistence operations. Classify an **NFR** only when evidence establishes an independently testable quality constraint, not merely a positive label for the same FR implementation. A deterministic seed rule, integrity hash check, or atomic rename can be a technical constraint or acceptance property of its parent FR; it is not automatically an additional NFR. Genuine distinct quality obligations may remain NFRs, but specify their own measurable condition and link their supporting FRs. Place each normative rule in exactly one authoritative location; summaries, outcome tables, interface tables and acceptance scenarios reference it rather than redefining it. Keep implementation mechanisms as evidence/context unless they are contractually observable.

After final grouping and section ordering, assign sequential IDs to normative FRs and NFRs, then update all references, outcome summaries, interface links, scenarios and coverage tables. Do not number by discovery order. In a document with an early outcome overview, references to later FR IDs are fine, but the **normative FR table's first appearances** should be ordered consistently. Preserve pre-existing IDs only when updating an established externally referenced baseline, and state that exception.

## Multi-level requirement reconstruction
- **System level**: describe the end-to-end outcome and lifecycle without absorbing all independently observable component obligations.
- **Component level**: preserve each in-scope independently exercisable component's significant input validation, operating modes, behavior/state, output and error/exit semantics. Consolidate related branches within that component, but do not discard its contract merely because an orchestrator invokes it.
- **Interface level**: specify material cross-component contracts: invocation arguments, messages/handshakes, ordering/timeouts, output schema, exit/failure propagation, and compatibility conditions when supported. A call-chain narrative alone is not an interface contract.
- Cross-reference shared requirements instead of duplicating full statements. Do not require a fixed number of component sections or separate documents; choose structure based on observable contract boundaries, not file layout.
- Before delivery, apply the input-driven semantic reconciliation in [evidence validation](evidence-validation.md); retain material technical context even when it is not a normative obligation.

## Two lightweight precision gates
- **Self-contained normative obligation**: Read each FR/NFR without its explanatory overview. Can a reviewer identify the decisive condition, rule, observable outcome and material failure behavior, using only that requirement plus explicitly linked *normative* constraints? If not, move the missing rule into the authoritative FR/NFR or linked normative constraint, then reduce the overview to a summary. Avoid duplicating a shared formula across multiple FRs.
- **Failure propagation scope**: For each materially different error path, trace where it is caught or propagated and identify its observable blast radius: individual input/event, current entity/batch, or whole invocation (including exit status when evidenced). Distinguish retained invalid records, skipped items, retries and fatal exceptions. Do not invent a recovery or exit code; only distinguish levels actually supported by the inspected source.

## Requirement quality gate
Before delivery, check each material requirement:
1. **Core meaning**: where identifiable, the primary outcome and its formation/validity semantics are independently understandable before supporting orchestration; otherwise the uncertainty is explicit.
2. **Clarity**: actor, trigger, preconditions, and outcome are unambiguous.
3. **Verifiability**: an observer or test can determine pass/fail; add acceptance conditions or a linked proposed scenario where useful.
4. **Boundary coverage**: relevant rejection, timeout, failure, recovery and variant paths are addressed or explicitly scoped out.
5. **Consistency**: no contradictory requirements or unsupported normative claims; conflicts are recorded separately.
6. **Traceability**: evidence location, revision/build context, and confidence are stated.
If a criterion cannot be established, narrow the statement or record the gap instead of inventing a requirement.

## Requirement granularity
- Before final IDs, inspect grouped operations for independently observable input/output/error contracts. Shared domain nouns or a common dispatcher do not justify grouping. Split materially distinct contracts, or give each explicit stable child identifier (e.g. FR-001.a), trigger/input, result, applicable error semantics, evidence and acceptance criterion. Parent IDs remain sequential; child references must resolve. Keep variants of one obligation together; do not split by function count.
- An acceptance criterion is a pass/fail oracle, not a test activity: specify the relevant input/condition and observable expected value, state, output, rejection or invariant. Replace vague 'verify correctness' or 'test error handling' with source-backed expectations; link exact normative constraints when shared. If a decisive expectation is unknown, mark that gap instead of inventing a value or error code.
- Prefer one requirement per independently observable behavior or decision outcome, not per function, line, or internal helper. A source-level decision branch is not automatically a business rule.
- Group multiple implementation branches when they implement one external contract; split when triggers, outcomes or independently testable conditions differ. Keep repetitive configuration ranges in a subordinate constraints table if they do not warrant separate top-level requirements.
- Verify counters, thresholds and retry/reset semantics across their lifecycle before promoting an implementation constant to a behavioral requirement.
- Record internal algorithms, data structures, resource handling and optimization choices as implementation evidence unless they impose an observable contract.
- Distinguish deliberate compatibility behavior from inferred intent; a suspicious behavior is a defect hypothesis, not automatically a requirement.

## Classification and identifiers
- Use `FR` for observable functional contracts, including success, denial, error/fallback, and compatibility behavior; group related branches under one ID when they form one independently testable contract.
- Use `NFR` only for evidence-backed nonfunctional constraints and `UNK` for unresolved questions. Do not create a default `BR` series from conditionals or special cases.
- An optional behavior-kind label may help readers distinguish normal, rejection, error/fallback, or compatibility behavior. It does not determine IDs or require separate sections.
- Keep inferred intent, defect hypotheses, proposed requirements, and implementation decisions out of the implemented-behavior table. Record them separately only when material and supported by the investigation.

Do not conflate:
1. **Implemented behavior**: code directly enforces it.
2. **Inferred intent**: hypothesis explaining the behavior, not a confirmed requirement.
3. **Proposed requirement**: a possible improvement, not present in code.
4. **Defect hypothesis**: suspicious mismatch requiring confirmation.
5. **Implementation decision**: internal mechanism not independently required by the external contract.
6. **Compatibility behavior**: observed legacy/variant behavior; rationale is unknown unless documented and verified.

A hardcoded value is an implementation fact; do not assert it is a product-level SLA. Performance, concurrency, and security properties need explicit evidence and scope.

Use EARS phrasing where helpful: ubiquitous (`The system shall...`), event-driven (`When...`), state-driven (`While...`), optional (`Where feature enabled...`), unwanted behavior (`If failure...`). Label such language as *reconstructed specification*, not original stakeholder specification.
