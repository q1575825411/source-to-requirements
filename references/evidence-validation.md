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

## Evidence path eligibility
For each cited source file, confirm it belongs to the allowed scoped candidate set for its owning Git project: tracked, untracked non-ignored, or an explicitly named ignored-file exception. A direct file read, stack trace, call chain, test log, or generated report does not override Git exclusion. If a claim depends on an ignored untracked file without an authorized exception, remove that evidence and re-evaluate the claim or mark it unresolved. Record exceptions in the provenance/limitations. For plain-file scopes, mark Git ignore filtering unavailable rather than claiming compliance.

## Evidence provenance and confidence

- **Evidence source** (optional, per evidence item): `SOURCE` for inspected implementation, `RUNTIME` for an observed trace/execution, `TEST` for an existing test, `DOC` for documentation. Multiple sources may support or conflict on the same claim.
- **Claim confidence** (existing output field, per requirement): `confirmed`, `inferred`, or `unknown`. Do not add a second set of status labels.
- **Conflicts**: describe contradictory evidence explicitly in a separate issue/conflict record linked to the affected requirement ID when available; narrow the claim, qualify its build/runtime conditions, or downgrade confidence until reconciled. Do not convert a conflict into a functional requirement or a defect claim without further proof. A `SOURCE` item can conflict with another `SOURCE` or `RUNTIME` item.
- **Defect hypotheses and inferred intent**: keep separate from evidence-backed implemented behavior. An anomaly or conflict does not establish intent or a defect; state the missing validation.

A `confirmed` requirement means its described implementation behavior is supported by evidence within the stated scope; it does **not** mean the system was compiled, deployed or exercised successfully. State verification scope once in the deliverable and distinguish static confirmation, existing test evidence, and observed runtime validation. Avoid both blanket downgrading static evidence to `inferred` and implying unperformed runtime verification.

Static source can establish what code implements without establishing runtime reachability for a particular build. Record conditions and environment when interpreting runtime observations.

Evidence is context-dependent: runtime traces demonstrate observed behavior only in their recorded conditions; source demonstrates reachable logic only when build/dispatch gates are established; tests and documentation corroborate but can diverge. Do not impose a universal evidence hierarchy.

## Core outcome verification
Where the scope supports a primary observable outcome, check that its contract explicitly defines the result's semantic unit, formation trigger/boundary, conditions, derived meaning and failure/validity distinctions to the extent evidenced. Check that orchestrators, storage, reporting, and interface descriptions do not merely mention the result while omitting how it is formed. Trace dependent capabilities back to the core contract where useful. Challenge inferred formulas, thresholds, measurement boundaries and acceptance rules against actual code; unresolved semantics must remain unknown, not silently invented. Do not force a primary outcome for scopes without one.

### Explainability gate (must be checked before claiming completion)
For every identifiable core outcome, locate the foundational FR ID(s) and answer, **using only those FRs and their referenced constraints**: what is one result; what inputs and conditions produce it; where does formation start/end; how is it computed/decided; what is attempted, emitted, accepted or invalid; what evidence supports each? An outcome name, list of fields, component capability, or call chain is **not** a passing answer. If evidence exists but the FR omits it, revisit extraction and revise before delivery. If evidence is missing, state a targeted unknown and limit the completeness claim. For multiple outcomes check each; for no identifiable primary outcome record the scoped reason and do not force a fake goal.

Coverage conclusions must say "no unmapped material behavior found within the inspected scope" rather than claiming no material omissions or exhaustive requirements completeness. Independently inspect granularity: split unrelated triggers/outcomes even when implemented by one helper; cross-reference overlapping system/component/interface obligations rather than repeating normative text.

## Cross-result consistency, classification and source-scope gates
- For related results, verify producer/consumer edges, input population, filtering, aggregation, acceptance gates, and raw/derived/presentation distinctions against source. A list of outcomes without lineage is insufficient when the lineage affects interpretation; do not fabricate relationships for independent results.
- Compare every FR, NFR, interface constraint, outcome overview and acceptance scenario for duplicate normative rules. Keep one authoritative obligation and link it elsewhere. Distinct quality targets must have independently testable evidence, not merely reword a functional implementation.
- Verify that final normative FR/NFR IDs are sequential and first appear in document order within their respective normative tables (unless preserving established IDs); cross-references must resolve and no ID may denote two obligations.
- Audit every evidence path against Git tracked/non-ignored eligibility or an explicitly scoped ignored-file exception. Merely stating "inspected output directory structure" does not demonstrate compliance; when eligibility cannot be established, say so and do not claim the ignored-file gate passed.

## Normative self-containment and failure-scope checks
- For each material FR/NFR, temporarily hide outcome summaries and other non-normative prose. Verify the obligation still states decisive trigger/conditions, rules, output and applicable failure behavior, allowing references to explicitly normative shared constraints. Repair missing rules at the normative source rather than copying them into multiple overview tables.
- For divergent failure paths, trace catch/propagation boundaries and verify the requirements distinguish item-level, entity/batch-level and invocation-level effects **only where evidenced**. Confirm that a recorded parse error is not incorrectly described as a fatal exception or vice versa; link acceptance scenarios to each distinct observed outcome.

## Contract precision review
- Inspect each grouped FR/NFR for independently testable contracts; split or identify children when input, outcome or failure semantics materially differ. Check each child has evidence and its own observable acceptance oracle. Reject activity-only acceptance wording; distinguish a proposed test procedure from its expected result.
- For core entry/formation paths, decisive algorithms, security/permission gates and material failure paths with `line unverified`, perform a targeted second source read/search to locate the decisive statement or branch, using line-numbered reads when available (including plain-file workspaces). Prefer focused ranges over whole-file citations. If still unavailable, retain symbol and `line unverified`, record the specific limitation and qualify coverage; never fabricate lines or require Git for line numbering.
- Review all delivered views for repeated normative text or duplicated evidence mappings. Keep one authoritative contract and use IDs elsewhere; retain only distinct interface, lineage, state, failure or coverage information. Internal reconciliation remains mandatory even when its matrix is not published.

## Extraction coverage reconciliation
For module scopes with independent components, compare the investigation inventory to the deliverable by component and interaction edge. Check input/validation, modes, state/lifecycle, observable output, failure/exit semantics and material protocol details. Record each as covered by requirement ID, covered by a linked constraint, internal-only with justification, explicitly excluded, or unresolved. A source file marked inspected is not evidence that its component contract was specified. A system-level requirement or call-chain row does not by itself satisfy a missing independent component or interface contract.

For feature/symbol scopes, reconcile only behavior material to the requested boundary. Keep this audit compact and do not generate placeholder requirements for unobserved behavior.

Review the final requirement statements for independent testability, behavioral rather than incidental implementation wording, and explicit treatment of known behavior versus unknown intent. Technical constraints that affect a required measurement protocol or compatibility contract must not be lost through abstraction.

Traceability matrix columns: requirement ID, statement, condition, evidence location, confidence, validation scenario, gaps.

For absence claims, record exactly which relevant paths, modules and build variants were searched. State a stop reason and unvisited paths; do not equate scoped inspection with exhaustive proof. Mark uncertain results explicitly.
