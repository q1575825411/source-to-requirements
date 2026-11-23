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

Do not conflate:
1. **Implemented behavior**: code directly enforces it.
2. **Inferred intent**: hypothesis explaining the behavior, not a confirmed requirement.
3. **Proposed requirement**: a possible improvement, not present in code.
4. **Defect hypothesis**: suspicious mismatch requiring confirmation.

A hardcoded value is an implementation fact; do not assert it is a product-level SLA. Performance, concurrency, and security properties need explicit evidence and scope.

Use EARS phrasing where helpful: ubiquitous (`The system shall...`), event-driven (`When...`), state-driven (`While...`), optional (`Where feature enabled...`), unwanted behavior (`If failure...`). Label such language as *reconstructed specification*, not original stakeholder specification.
