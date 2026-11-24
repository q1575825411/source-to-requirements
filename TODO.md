# Roadmap: source-grounded quality review and reference examples

Status: review design established; execution and verified examples remain pending. Checked items denote delivered artifacts, not measured skill performance.

## P0 — Review foundation
- [x] Define case metadata and reproducible input format (evals/CASE_TEMPLATE.md); optional known-defect assertions replace a mandatory exhaustive oracle.
- [x] Define independent accuracy and conformance review criteria, including evidence, material omissions, unsupported claims, scope and language (evals/REVIEW.md).
- [x] Define run recording and comparative review protocol (evals/README.md).
- [ ] Add a small self-contained C/C++ fixture with success, failure and boundary paths.
- [ ] Add a Java/JNI/C++ cross-language fixture with a verifiable binding.
- [ ] Add an Android Framework end-to-end fixture with accessible pinned AOSP revision and product/build assumptions.
- [ ] Add negative fixtures: missing source, misleading comments/dead code and competing build variants.
- [ ] Establish baseline runs for Codex CLI and GitHub Copilot (where available); record actual inputs, outputs, environment and reviewed findings.
- [ ] Reserve at least one unseen case for generalization checks; keep reviewer-only regression notes separate from generation inputs.

## P0 — Complete reference examples
- [ ] Publish one independently reviewed C/C++ single-module example (source + prompt + requirements + evidence).
- [ ] Publish one independently reviewed Android Framework cross-module example (pinned source, gates, call chain, requirements).
- [ ] Publish one evidence-insufficient example showing unknowns, scoped stop conditions and no fabricated conclusions.
- [ ] Review each example against the accuracy/conformance protocol before labeling it verified.
- [ ] Keep examples illustrative and separate from unseen evaluation cases.

## P1 — Feedback loop
- [ ] Record evidence-backed defects and map actionable causes to instruction or reference-file changes.
- [ ] Rerun comparable cases after changes; track resolved, persistent, introduced and unverified defects.
- [ ] Consider lightweight structural validation/CI after review workflow stabilizes; no mandatory runtime dependency.

## Definition of done
- Cases are reproducible from recorded inputs without undocumented local state.
- Confirmed findings have checkable evidence and demonstrated consequences; unresolved questions are separate.
- At least three complete examples have independently reviewed evidence.
- No fixture/example is represented as validated until actually reviewed or executed.
- No aggregate score or exhaustive coverage claim is required.
