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

## Requirement granularity
- Prefer one requirement per independently observable behavior or decision rule, not per function, line, or internal helper.
- Group multiple implementation branches when they implement one external contract; split when triggers, outcomes or independently testable conditions differ.
- Verify counters, thresholds and retry/reset semantics across their lifecycle before promoting an implementation constant to a behavioral requirement.
- Record internal algorithms, data structures, resource handling and optimization choices as implementation evidence unless they impose an observable contract.
- Distinguish deliberate compatibility behavior from inferred intent; a suspicious behavior is a defect hypothesis, not automatically a requirement.

Do not conflate:
1. **Implemented behavior**: code directly enforces it.
2. **Inferred intent**: hypothesis explaining the behavior, not a confirmed requirement.
3. **Proposed requirement**: a possible improvement, not present in code.
4. **Defect hypothesis**: suspicious mismatch requiring confirmation.
5. **Implementation decision**: internal mechanism not independently required by the external contract.
6. **Compatibility behavior**: observed legacy/variant behavior; rationale is unknown unless documented and verified.

A hardcoded value is an implementation fact; do not assert it is a product-level SLA. Performance, concurrency, and security properties need explicit evidence and scope.

Use EARS phrasing where helpful: ubiquitous (`The system shall...`), event-driven (`When...`), state-driven (`While...`), optional (`Where feature enabled...`), unwanted behavior (`If failure...`). Label such language as *reconstructed specification*, not original stakeholder specification.
