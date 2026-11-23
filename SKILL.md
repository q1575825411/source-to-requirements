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
- Output: Markdown in conversation by default. Create files only when explicitly requested; do not create three files merely because three templates exist.

## Procedure
1. **Scope**: State feature, boundaries, repository/commit, configuration assumptions, and exclusions. Define observable entry and outcome.
2. **Discover**: Search narrowly for symbols, APIs, manifest declarations, flags, tests, config overlays, and entry points. Prefer `rg`, `git grep`, `git log` and focused file reads. Do not dump large trees. See [code-investigation](references/code-investigation.md).
3. **Trace**: Follow callers and callees, branches, permission checks, state mutations, persistence, IPC, callbacks, errors and lifecycle. Distinguish production paths from dead code and tests. For Android use [Android guide](references/android-framework.md).
4. **Extract**: Express each implemented rule in actor/trigger/precondition/behavior/outcome terms. Separate behavior from design-intent hypothesis and proposed improvements. See [extraction rules](references/requirement-extraction.md).
5. **Verify**: For every assertion locate supporting source location and check competing branches, gates, and overrides. Use [evidence validation](references/evidence-validation.md). Never invent file paths, line numbers, tests, or historical intent.
6. **Deliver**: Follow the [output routing guide](references/output-template.md). Always use [requirements template](templates/requirements.md) as the requirements-table skeleton. Read [call-chain template](templates/call-chain.md) only for nontrivial multi-step/cross-boundary flows or when requested. Read [acceptance scenarios template](templates/test-scenarios.md) only when test coverage, boundary cases, or acceptance criteria are relevant or requested. For deep mode also use the compact matrices in the output routing guide. Highlight unknowns and suggested validation steps.

## Modes and output routing
| Mode | Investigation | Default output |
|---|---|---|
| quick | One narrow flow; critical branches | Compact requirements table with evidence; optional brief flow note |
| standard | End-to-end feature, configurations and relevant error paths | **Required** requirements table; **conditional** call-chain and acceptance sections |
| deep | Cross-service/vendor differences, state and branch coverage, history where accessible | Requirements table plus branch/state, traceability and scoped coverage matrices; conditional detailed call-chain/test sections |

- Include a call-chain section when the evidence crosses meaningful boundaries (e.g. Binder, callbacks, multiple services) or when the flow is essential to explain behavior. Otherwise omit it.
- Include acceptance scenarios when behavior has meaningful branches, failures, permissions, configuration variants, or the user asks for tests. Do not invent test execution results.
- Keep sections together in one answer/document by default. Split into `requirements.md`, `call-chain.md`, and `test-scenarios.md` **only when the user requests separate artifacts**.
- Expand investigation depth only when evidence demands it. Report partial coverage instead of claiming exhaustive analysis.

## Output constraints
- IDs: `FR-001` functional, `BR-001` business/decision rule, `NFR-001` nonfunctional only when evidence supports it, `UNK-001` unresolved.
- Evidence: repository-relative path + symbol + line range when verified. For changing worktrees, include commit hash. If line range unavailable, cite symbol and mark `line unverified`.
- Confidence: `confirmed` (direct implementation/test), `inferred` (reasonable interpretation), `unknown` (insufficient evidence). **Never present inferred requirements as original intent.**
- Negative claims require comprehensive search within explicitly stated scope; otherwise say `not found in inspected paths`.
- Test cases must distinguish existing tests from proposed tests. No unexecuted tests may be reported as passed.
- Security/permission findings: document observed checks and missing evidence; do not assert exploitability without verification.
