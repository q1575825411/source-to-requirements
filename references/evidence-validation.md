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

Evidence labels: `SOURCE` (static implementation), `RUNTIME` (observed execution with environment recorded), `INFERRED` (interpretation), `UNKNOWN` (insufficient evidence), `CONTRADICTED` (conflicting evidence). These labels describe evidence type/status; retain the output's `confirmed / inferred / unknown` confidence field separately. A source path can confirm static behavior without proving runtime reachability. Conflicts must be surfaced, not silently resolved.

Evidence is context-dependent: runtime traces demonstrate observed behavior only in their recorded conditions; source demonstrates reachable logic only when build/dispatch gates are established; tests and documentation corroborate but can diverge. Do not impose a universal evidence hierarchy.

Traceability matrix columns: requirement ID, statement, condition, evidence location, confidence, validation scenario, gaps.

For absence claims, record exactly which module paths and build variants were searched. State a stop reason and unvisited paths; do not equate scoped inspection with exhaustive proof. Mark uncertain results explicitly.
