# Evaluations (placeholder)

**Status:** planned. No fixtures or evaluation runs have been completed.

Purpose: evaluate whether this skill reconstructs source-backed observable behavior, not merely whether its Markdown output matches a template.

## Proposed layout
```text
evals/
  README.md
  CASE_TEMPLATE.md
  cases/           # future self-contained or pinned-source fixtures
  runs/            # future run records and rubric scores
```

## Run protocol (TODO)
1. Pin fixture source revision and build/product assumptions.
2. Supply only the fixture's prompt and source to the agent; do not reveal expected answers or held-out labels.
3. Record skill commit, agent/model version, date, mode, language, and output.
4. Score correctness, evidence, missed branches, unsupported claims, scope and language consistency.
5. Compare with prior baseline and note regressions.

See [case template](CASE_TEMPLATE.md) and [roadmap](../TODO.md). Scores and acceptance thresholds are not yet defined.
