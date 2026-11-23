---
name: source-to-requirements
description: Reverse-engineer verifiable requirements and acceptance criteria from C, C++, Java, JNI or mixed-language source code. Use for module behavior analysis, end-to-end feature tracing across modules, or focused symbol investigation, including Android/AOSP and vendor implementations. Supports quick, standard and deep modes.
---

# Source to Requirements

## Mission
Recover **observable implemented behavior** from source, not imagined original product intent. Treat source as evidence, not as proof of what stakeholders wanted. Read only; never modify analyzed source unless separately authorized.

## Inputs and defaults
- Target: a module, feature, symbol, or path. **User-specified scope takes precedence**: a module request uses a module boundary; a feature request follows its end-to-end observable behavior across modules as needed; a symbol request starts locally and expands only as necessary. If unspecified, ask for one target rather than scanning an entire monorepo.
- Mode: `standard` by default; `quick` for a narrow behavior, `deep` for complex state, cross-language boundaries, or high-risk behavior.
- Version/build: record repository/commit, module root(s), languages, build target and relevant product/variant when available; record Android version only if applicable. Mark unavailable fields unknown.
- Output: Markdown in conversation by default. Create files only when explicitly requested; do not create three files merely because three templates exist.

## Procedure
1. **Scope**: Classify the request as module, feature or symbol analysis. State the user-requested behavioral boundary, relevant module root(s), repository/commit, languages, build target, interfaces, assumptions and exclusions. Use [scope and module boundary guide](references/module-boundary.md). Define observable entry and outcome.
2. **Discover**: Search narrowly for symbols, APIs, manifest declarations, flags, tests, config overlays, and entry points. Prefer `rg`, `git grep`, `git log` and focused file reads. Do not dump large trees. See [code-investigation](references/code-investigation.md).
3. **Trace**: Follow callers and callees, branches, permission checks, state mutations, persistence, IPC, callbacks, errors and lifecycle **within the requested behavioral scope**. For feature requests, cross module/process boundaries whenever needed to establish the end-to-end outcome. Apply only relevant [language investigation guidance](references/language-analysis.md) for C, C++, Java or mixed-language boundaries. Distinguish production paths from dead code and tests. For Android-specific modules optionally use [Android guide](references/android-framework.md).
4. **Extract**: Group implementation branches into verifiable observable behaviors; do not make one requirement per function or statement. Express each implemented rule in actor/trigger/precondition/behavior/outcome terms. Separate behavior from design-intent hypothesis and proposed improvements. See [extraction rules](references/requirement-extraction.md).
5. **Verify**: For every assertion locate supporting source location, actively seek counterexamples and conflicting paths, and check competing branches, gates, and overrides. Use [evidence validation](references/evidence-validation.md). Never invent file paths, line numbers, tests, or historical intent.
6. **Stop**: Stop when the **user-requested behavior** and material alternatives have been checked, or evidence is exhausted. For a feature request, do not stop at a module boundary that prevents explaining the requested outcome. Mark unvisited paths and unresolved edges; do not expand into unrelated code.
7. **Deliver**: Follow the [output routing guide](references/output-template.md). When source evidence is available, use [requirements template](templates/requirements.md) as the requirements-table skeleton. If source is unavailable, provide an investigation plan instead of fabricated requirements. Read [call-chain template](templates/call-chain.md) only for nontrivial multi-step/cross-boundary flows or when requested. Read [acceptance scenarios template](templates/test-scenarios.md) only when test coverage, boundary cases, or acceptance criteria are relevant or requested. For deep mode also use the compact matrices in the output routing guide. Highlight unknowns and suggested validation steps.

## Modes and output routing
| Mode | Investigation | Default output |
|---|---|---|
| quick | One narrow flow; critical branches | Compact requirements table with evidence; optional brief flow note |
| standard | Requested module or end-to-end feature behavior, interfaces, configurations and error paths | **Required** requirements table; **conditional** call-chain and acceptance sections |
| deep | Complex state, cross-language/cross-module differences, history where accessible | Requirements table plus branch/state, traceability and scoped coverage matrices; conditional detailed call-chain/test sections |

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
