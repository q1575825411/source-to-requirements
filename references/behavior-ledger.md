# Behavior persistence (Phase 2)

Apply proportionally in all modes. Preserve discovered material behavior before context loss or abstraction. This is not a second source investigation, a historical baseline, or a requirement mapping mechanism.

## Working record

Use one run-local UTF-8 JSON Lines file outside the analyzed source and installed skill directories, alongside the structural coverage record. Append compact records in batches using available file tools. Each line is a JSON object:

```json
{"id":"B-001","units":["U-001"],"fact":"When the input is rejected, return the evidenced status without changing the stored state.","evidence":["relative/path:verified symbol or range"],"confidence":"confirmed"}
```

Use actual source facts and actual unit IDs, not the illustrative values above. IDs are stable within the run. Confidence is confirmed, inferred or unknown, following the existing evidence policy. Evidence must identify the relevant source location; for unavailable evidence, record the inspected location and specific limitation rather than inventing a citation. A fact may contain several closely related variants of one contract. No mandatory per-field prose, per-function record, requirement ID, or duplicate source quotation.

## Capture during investigation

- At natural investigation checkpoints, persist newly established material facts before moving to unrelated units or losing their source context. Before marking a unit inspected, capture its material findings or explicitly record why none were found. Use an optional unit field in the structural record, `no_material_behavior_reason`, for the latter; do not use it to hide uncertainty or unread source.
- Capture independently observable behavior, decisive inputs/guards, exact thresholds, formulas and units, ordering/state changes, output semantics, error propagation scope, compatibility variants, and material technical constraints where applicable. Include observed conflicts and specific unresolved questions. Do not invent absent fields or turn every branch into a requirement.
- Preserve precise semantics, not merely names or labels such as "uses source thresholds". Record relevant populations, validity rules and transformation edges. Existing outcome-formation and lineage records may be represented directly in ledger facts or referenced from a durable run-local record with precise source evidence; do not duplicate them or weaken their existing mandatory fields.
- Group related facts, reuse shared evidence, and write batches alongside structural checkpoints. No separate tool call per fact, no fixed record quota, no source-read budget. Reuse source already available; recover truncated or missing material source before claiming inspection.
- If a fact is corrected, append a replacement with the same ID and complete revised content; retain prior versions. If a fact is withdrawn, append the same ID with the original required fields and an additional nonempty `withdrawn_reason` explaining the evidence-based correction. Never silently discard a material finding. A withdrawn record does not count as active coverage.
- If persistence is unavailable, retain a compact in-context record and explicitly report the limitation; do not claim durable capture.

## Use and check

Use the active ledger facts as input to requirement abstraction, together with existing source-linked outcome and lineage records. Read by relevant unit or batch as needed; do not repeatedly dump the entire ledger. Retain all existing investigation, evidence, counterexample, abstraction and delivery gates. Do not replace source verification with ledger assertions.

Before delivery run:
`python <skill-root>/scripts/check_behavior_ledger.py <structural-record.json> <behavior-ledger.jsonl>`

Resolve the actual installed skill root as in Phase 1. Repair malformed records, unknown unit IDs and inspected units without active findings or a specific no-material-behavior reason. If the script or interpreter is unavailable, manually check the same invariants and disclose the fallback. Report compact counts and limitations in the existing coverage/provenance section; publish the ledger only when requested. The checker verifies bookkeeping, not whether all material behavior was discovered, whether evidence supports a fact, or whether the final document preserves it. Existing semantic review remains mandatory. Phase 3 will address explicit behavior-to-deliverable mapping.
