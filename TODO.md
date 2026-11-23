# Roadmap: reproducible evaluations and reference examples

This is a planning scaffold only. No evaluation results, passing scores, or verified reference outputs are claimed.

## P0 — Evaluation fixtures and rubric
- [ ] Define a deterministic fixture format: case ID, source snapshot/revision, prompt, mode, language, expected behaviors, evidence anchors, and known exclusions.
- [ ] Add a small self-contained C/C++ fixture with success, failure, and boundary paths.
- [ ] Add a Java/JNI/C++ cross-language fixture with a verifiable binding.
- [ ] Add an Android Framework end-to-end fixture, pinning an accessible AOSP revision and product/build assumptions.
- [ ] Add negative fixtures: missing source, misleading comments/dead code, and competing build variants.
- [ ] Define rubric: behavioral correctness, evidence validity, branch coverage, unsupported claims, scope adherence, and language consistency.
- [ ] Establish baseline runs for Codex CLI and GitHub Copilot (VS Code/CLI where available); record agent/model versions, run date, inputs, and outcomes.
- [ ] Keep at least one held-out evaluation case unavailable to the agent during execution.

## P0 — Complete reference examples
- [ ] Publish one verified C/C++ single-module example (source + prompt + requirements + evidence).
- [ ] Publish one verified Android Framework cross-module example (pinned source revision, gates, call chain, requirements).
- [ ] Publish one evidence-insufficient example showing unknowns, scoped stop conditions, and no fabricated conclusions.
- [ ] Review each example against the evaluation rubric before labeling it a reference.
- [ ] Ensure examples are illustrative, not copied as answers into held-out evaluations.

## P1 — Feedback loop
- [ ] Record failures by category and map each to a specific instruction or reference-file change.
- [ ] Rerun the fixed test set after changes; compare with baseline and track regressions.
- [ ] Add lightweight structural validation/CI only after the fixture schema stabilizes.

## Definition of done
- Evaluation cases can be rerun from pinned inputs without relying on undocumented local state.
- Every scored claim has a checkable expected behavior and evidence anchor.
- At least three complete examples have independently reviewed evidence.
- No fixture/example is represented as validated until actually reviewed or executed.
