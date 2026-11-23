# Evidence validation checklist

For each requirement:
- Is there an executable production path proving the behavior?
- Have guards, early returns, exceptions and failure branches been inspected?
- Does the call cross Binder, callbacks, asynchronous tasks or a native boundary?
- Is it affected by build target, product overlays, properties, permissions, SELinux or flags?
- Is the behavior overridden by subclasses, plugins, vendor hooks or device-specific config?
- Are source path, symbol and line numbers verified against this checkout?
- Is the claim about implementation, intent, proposed behavior or defect?
- Are existing tests distinguished from proposed acceptance tests?

Evidence strength: direct control-flow/source > executed test and runtime trace (if supplied) > relevant existing test > current documentation > naming/comments. Conflicts must be surfaced, not silently resolved.

Traceability matrix columns: requirement ID, statement, condition, evidence location, confidence, validation scenario, gaps.

For absence claims, record exactly which directories and build variants were searched. Mark uncertain results explicitly.
