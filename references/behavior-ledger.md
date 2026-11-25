# Behavior persistence (Phase 2)

Apply proportionally in all modes. Preserve discovered material behavior before context loss or abstraction. This is not a second source investigation, a historical baseline, or a requirement mapping mechanism.

## Working record

Use one run-local UTF-8 JSON Lines file outside the analyzed source and installed skill directories, alongside the structural coverage record. Append compact records in batches using available file tools. Each line is a JSON object:

```json
{"id":"B-001","units":["U-001"],"fact":"When the input is rejected, return the evidenced status without changing the stored state.","evidence":["relative/path:verified symbol or range"],"confidence":"confirmed"}
```

Use actual source facts and actual unit IDs, not the illustrative values above. IDs are stable within the run. Confidence is confirmed, inferred or unknown, following the existing evidence policy. Evidence must identify the relevant source location; for unavailable evidence, record the inspected location and specific limitation rather than inventing a citation. A fact may contain several closely related variants of one contract. No mandatory per-field prose, per-function record, requirement ID, or duplicate source quotation.

## Capture during investigation

Use a repeating investigation checkpoint, not a post-investigation summarization phase: select a coherent batch of units, inspect their source, append established facts to the ledger, then persist the corresponding structural status changes before starting an unrelated batch. Initialize the ledger before structural source inspection or contract discovery; basic path enumeration may precede initialization. Capture material findings from structural discovery, contract discovery and tracing; establish the corresponding unit before persisting its facts. A narrow single-batch task may use one checkpoint. For multiple unrelated batches, a single end-of-investigation ledger write is not compliant. Keep unfinished units in progress. A checkpoint may combine ledger and structural writes only if ledger append succeeds before any corresponding structural inspected status is written; otherwise use separate ordered calls; do not mark a unit inspected if its findings could not be persisted (except the explicitly disclosed in-context fallback). Do not wait for all source reads, outcome grouping or drafting before the first capture.

- At natural investigation checkpoints, persist newly established material facts before moving to unrelated units or losing their source context. Before marking a unit inspected, capture its material findings or explicitly record why none were found.
- Treat each fact as a recoverable source-backed contract fragment, not a topic label. A reader with the fact and its linked durable records must be able to recover the material trigger, governing rule, result and applicable failure semantics without relying on remembered source text. Preserve exact conditions, boundary inclusivity, defaults, units, formulas, precedence, exceptions and conditional applicability when evidenced. Split independently meaningful rules when grouping would obscure them; related variants may remain together. Do not substitute a symbol citation for the rule itself. Capture independently observable behavior, decisive inputs/guards, exact thresholds, formulas and units, ordering/state changes, output semantics, error propagation scope, compatibility variants, and material technical constraints where applicable. Include observed conflicts and specific unresolved questions. Do not invent absent fields or turn every branch into a requirement.
- Preserve precise semantics, not merely names or labels such as "uses source thresholds". Record relevant populations, validity rules and transformation edges. Existing outcome-formation and lineage records may be represented directly in ledger facts or referenced from a durable run-local record with precise source evidence; do not duplicate them or weaken their existing mandatory fields.
- Group related facts, reuse shared evidence, and write batches alongside structural checkpoints. No separate tool call per fact, no fixed record quota, no source-read budget. Reuse source already available; recover truncated or missing material source before claiming inspection.
- If a fact is corrected, append a replacement with the same ID and complete revised content; retain prior versions. If a fact is withdrawn, append the same ID with the original required fields and an additional nonempty `withdrawn_reason` explaining the evidence-based correction. Never silently discard a material finding. A withdrawn record does not count as active coverage.
- If persistence is unavailable, retain a compact in-context record and explicitly report the limitation; do not claim durable capture.

## Use and check

At outcome reconstruction, counterexample review and drafting, append newly established material facts or corrections before proceeding. If a material source-backed rule, conflict or unresolved question is present in working notes or the draft but absent or less precise in the ledger, repair the ledger using available evidence before delivery. This is a targeted capture check, not a second full investigation or explicit requirement mapping. Keep observed implementation facts distinct from inferred defects and unknowns; do not force all findings to confirmed.

Use the active ledger facts as input to requirement abstraction, together with existing source-linked outcome and lineage records. Read by relevant unit or batch as needed; do not repeatedly dump the entire ledger. Retain all existing investigation, evidence, counterexample, abstraction and delivery gates. Do not replace source verification with ledger assertions.

Before delivery run:
`python <skill-root>/scripts/check_behavior_ledger.py <structural-record.json> <behavior-ledger.jsonl>`

Resolve the actual installed skill root as in Phase 1. Repair malformed records, unknown unit IDs and inspected units without active facts or a specific no-material-behavior reason. If the script or interpreter is unavailable, manually check the same invariants and disclose the fallback. Report compact counts and limitations in the existing coverage/provenance section; publish the ledger only when requested. Review the actual checkpoint execution for deferred capture; a final valid ledger cannot establish when its records were written. Disclose any deferred capture as a process limitation rather than claiming incremental persistence. The checker verifies bookkeeping, not whether all material behavior was discovered, whether evidence supports a fact, or whether the final document preserves it. Existing semantic review remains mandatory. Use the input-driven semantic reconciliation in [evidence validation](evidence-validation.md) for behavior-to-deliverable coverage; the ledger itself does not require mapping fields.
