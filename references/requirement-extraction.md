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

## Requirements abstraction: contract versus mechanism
- Write requirements from the perspective of the system's observable obligations: trigger, conditions, outcome, rejection/failure behavior and relevant constraints. Organize by feature and scenario, not by implementation file/function order.
- Preserve an implementation-specific parameter, API, timing or method when it defines the tested contract, interoperability, compatibility, or an essential measurement protocol. Otherwise retain it in technical notes/evidence rather than making it a standalone requirement.
- Classify build architecture, compiler flags, linked libraries, and internal algorithms as build/deployment facts or implementation notes unless evidence establishes a genuine product-level requirement. Do not label all technical facts `NFR`.
- A source-observed behavior is a candidate reconstructed requirement, not proof that stakeholders intended or approved it. When suspicious, state the observed contract separately from its defect hypothesis and desired change.
- Distinguish **known behavior** from **unknown intent**: a verified fixed path or guard is not `UNK` merely because its rationale is unclear; put the rationale question in `UNK` and link the observed behavior.

## Requirement quality gate
Before delivery, check each material requirement:
1. **Clarity**: actor, trigger, preconditions, and outcome are unambiguous.
2. **Verifiability**: an observer or test can determine pass/fail; add acceptance conditions or a linked proposed scenario where useful.
3. **Boundary coverage**: relevant rejection, timeout, failure, recovery and variant paths are addressed or explicitly scoped out.
4. **Consistency**: no contradictory requirements or unsupported normative claims; conflicts are recorded separately.
5. **Traceability**: evidence location, revision/build context, and confidence are stated.
If a criterion cannot be established, narrow the statement or record the gap instead of inventing a requirement.

## Requirement granularity
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
