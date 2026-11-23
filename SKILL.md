---
name: source-to-requirements
description: Reverse-engineer verifiable functional requirements, rules, and acceptance tests from existing source code. Use when asked to infer requirements, document implemented behavior, trace a feature, or compare AOSP and vendor implementations. Supports quick, standard, and deep modes.
---

# Source to Requirements

## Mission
Recover **observable implemented behavior** from source, not imagined original product intent. Treat source as evidence, not as proof of what stakeholders wanted. Read only; never modify analyzed source unless separately authorized.

## Inputs and defaults
- Target: a feature, symbol, path, or subsystem. If unspecified, ask for one target rather than scanning an entire monorepo.
- Mode: `standard` by default; `quick` for a narrow question, `deep` for cross-service, multi-repository, or high-risk behavior.
- Version/build: record branch, commit, Android version and relevant product/variant when available; otherwise mark unknown.
- Output: Markdown in conversation by default. Write files only when requested or when the user's workflow clearly calls for deliverables.

## Procedure
1. **Scope**: State feature, boundaries, repository/commit, configuration assumptions, and exclusions. Define observable entry and outcome.
2. **Discover**: Search narrowly for symbols, APIs, manifest declarations, flags, tests, config overlays, and entry points. Prefer `rg`, `git grep`, `git log` and focused file reads. Do not dump large trees. See [code-investigation](references/code-investigation.md).
3. **Trace**: Follow callers and callees, branches, permission checks, state mutations, persistence, IPC, callbacks, errors and lifecycle. Distinguish production paths from dead code and tests. For Android use [Android guide](references/android-framework.md).
4. **Extract**: Express each implemented rule in actor/trigger/precondition/behavior/outcome terms. Separate behavior from design-intent hypothesis and proposed improvements. See [extraction rules](references/requirement-extraction.md).
5. **Verify**: For every assertion locate supporting source location and check competing branches, gates, and overrides. Use [evidence validation](references/evidence-validation.md). Never invent file paths, line numbers, tests, or historical intent.
6. **Deliver**: Use [output format](references/output-template.md) and templates as needed. Highlight unknowns and suggested validation steps.

## Modes
| Mode | Investigation | Deliverables |
|---|---|---|
| quick | One narrow flow; critical branches | Concise requirements and source references |
| standard | End-to-end feature, configurations, error paths | Requirements, call chain, acceptance scenarios |
| deep | Cross-service/vendor differences, state matrix, history where accessible | Full spec, traceability matrix, risks, coverage gaps |

Expand depth only if evidence demands it. Report partial coverage instead of claiming exhaustive analysis.

## Output constraints
- IDs: `FR-001` functional, `BR-001` business/decision rule, `NFR-001` nonfunctional only when evidence supports it, `UNK-001` unresolved.
- Evidence: repository-relative path + symbol + line range when verified. For changing worktrees, include commit hash. If line range unavailable, cite symbol and mark `line unverified`.
- Confidence: `confirmed` (direct implementation/test), `inferred` (reasonable interpretation), `unknown` (insufficient evidence). **Never present inferred requirements as original intent.**
- Negative claims require comprehensive search within explicitly stated scope; otherwise say `not found in inspected paths`.
- Test cases must distinguish existing tests from proposed tests. No unexecuted tests may be reported as passed.
- Security/permission findings: document observed checks and missing evidence; do not assert exploitability without verification.
