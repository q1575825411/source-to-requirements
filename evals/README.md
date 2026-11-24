# Requirements quality review

Status: review protocol defined; no completed benchmark runs or verified reference examples are claimed.

Evaluate reconstructed requirements against accessible source and the requested scope, not a canonical requirements document. Different valid abstractions, grouping and wording are acceptable. The two review dimensions are **accuracy** and **conformance**. See [review protocol](REVIEW.md).

## Run protocol
1. Record source snapshot/revision (including relevant local changes or plain-file snapshot), build assumptions, exact task, scope, mode and language using [case template](CASE_TEMPLATE.md).
2. Generate the requirements with the selected agent and skill revision. Keep reviewer-only regression notes out of the generation context.
3. In a fresh review context, provide the source, original task, requirements and review protocol. Do not provide the generator's self-assessment. Review independently; record actual inspected paths and limitations.
4. Record evidence-backed findings and unresolved verification questions. Optional known-defect checks supplement open-ended review; they are not a complete oracle.
5. For version comparison, use the same source, task, mode, language and comparable agent/tool environment. Hide version labels from reviewers where practical. Compare confirmed findings by underlying defect, not raw counts or document length; distinguish resolved, persistent, introduced and unverified issues. Repeat or seek human adjudication when results disagree.

No aggregate score, fixed requirement count, exhaustive coverage claim or universal pass threshold is required. No findings means only that none were established within the reviewed scope.

Review artifacts are development-only, not runtime dependencies. Keep confidential source and outputs outside the public repository. See [roadmap](../TODO.md).
