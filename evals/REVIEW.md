# Independent requirements quality review

## Purpose and boundaries
Review implementation-derived requirements, not the generator's compliance with a particular template. There is no unique correct decomposition or exhaustive reference answer. Use the requested scope, applicable source snapshot, and the document as the basis. Remain read-only. Do not infer original stakeholder intent or claim runtime verification from static evidence.

## Accuracy
- Check material claims against the applicable production path, including trigger, conditions, governing rules, observable results, state changes, failure propagation, and build/variant gates.
- Verify that evidence locations actually support the claim; a valid path or line alone is insufficient. Distinguish confirmed, inferred and unknown behavior.
- Independently investigate relevant entry points, core outcome formation, decisive branches and counterexamples, rather than only following document citations. Identify concrete omitted material contracts or missing conditions when source supports them. Do not claim exhaustive coverage or calculate recall from inspected paths.
- Distinguish actual contradictions from unavailable evidence. Record unresolved verification separately; unsupported certainty is a finding when the document claims confirmation without adequate support.

## Conformance
Review requirements engineering quality, not stylistic preferences:
- Clarity and consistency: unambiguous obligations, compatible conditions and results across views.
- Contract granularity: independently observable obligations with materially distinct inputs/results/failures are distinguishable; explicit subcontracts are acceptable.
- Self-containment and verifiability: material conditions, governing rules and outcomes are present or explicitly linked; acceptance specifies observable pass/fail criteria.
- Traceability and classification: evidence is resolvable where available; implemented behavior, inference, proposed changes and unknowns are distinct.
- Appropriate abstraction and non-redundancy: observable contracts rather than mechanical code narration; preserve material information, allow useful reference-based views for concrete review tasks.
- Respect requested scope and language; do not penalize valid alternative wording, grouping, IDs, section choices, or length. Identify a concrete consequence before calling an issue a defect.

## Findings and severity
For each distinct defect report ID, dimension (accuracy or conformance; cross-reference secondary impact without double counting), affected requirement or missing contract, specific issue, evidence (source path/symbol/verified lines or document excerpt and violated conformance principle), consequence, severity and suggested correction. For omissions explain why the behavior is material and in scope. For accuracy findings cite applicable source; if unavailable, report verification limitations rather than inventing contradictions.

- Critical: demonstrated error likely to invalidate a core result or critical safety/security contract.
- Major: material behavior error, omission or ambiguity that could cause incorrect implementation or acceptance.
- Minor: localized traceability or expression defect with limited behavioral impact.
- Suggestion: optional improvement without a demonstrated defect; report separately.

Severity depends on demonstrated impact, not category alone. Consolidate repeated manifestations of the same underlying defect. Distinguish confirmed findings, unresolved questions and suggestions. State inspected scope and limitations. Do not claim completeness, certification, or successful execution without evidence.

## Comparison
Review outputs independently using equivalent inputs and investigation budgets. Where practical blind version labels. Compare matched defects and substantive tradeoffs; a lower count alone does not establish improvement if review scope differs. Optional regression assertions test known issues only. Human adjudication may resolve disputed evidence or materiality.
