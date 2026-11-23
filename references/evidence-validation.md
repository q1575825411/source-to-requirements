# Evidence validation checklist

For each candidate requirement, seek both supporting and **challenging** evidence. Attempt to falsify the proposed statement by looking for alternate dispatch targets, guards, error paths, overrides, build variants and conflicting tests. Revise, narrow or mark a claim unresolved if a counterexample is found.

For each requirement:
- Is there an executable production path proving the behavior?
- Have guards, early returns, exceptions and failure branches been inspected?
- Does the call cross Binder, callbacks, asynchronous tasks or a native boundary?
- Is it affected by build target, product overlays, properties, permissions, SELinux or flags?
- Is the behavior overridden by subclasses, plugins, vendor hooks or device-specific config?
- Are source path, symbol and line numbers verified against this checkout?
- Is the claim about implementation, intent, proposed behavior or defect?
- Are existing tests distinguished from proposed acceptance tests?
- What observation or alternate path would disprove this claim, and was that path inspected?
- Is the cited path reachable in the module/build under analysis?

## Evidence provenance and confidence

- **Evidence source** (optional, per evidence item): `SOURCE` for inspected implementation, `RUNTIME` for an observed trace/execution, `TEST` for an existing test, `DOC` for documentation. Multiple sources may support or conflict on the same claim.
- **Claim confidence** (existing output field, per requirement): `confirmed`, `inferred`, or `unknown`. Do not add a second set of status labels.
- **Conflicts**: describe contradictory evidence explicitly in the requirement's notes/gaps; narrow or downgrade confidence until reconciled. A `SOURCE` item can conflict with another `SOURCE` or `RUNTIME` item.

Static source can establish what code implements without establishing runtime reachability for a particular build. Record conditions and environment when interpreting runtime observations.

Evidence is context-dependent: runtime traces demonstrate observed behavior only in their recorded conditions; source demonstrates reachable logic only when build/dispatch gates are established; tests and documentation corroborate but can diverge. Do not impose a universal evidence hierarchy.

Traceability matrix columns: requirement ID, statement, condition, evidence location, confidence, validation scenario, gaps.

For absence claims, record exactly which relevant paths, modules and build variants were searched. State a stop reason and unvisited paths; do not equate scoped inspection with exhaustive proof. Mark uncertain results explicitly.
