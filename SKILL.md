---
name: source-to-requirements
description: Reverse-engineer verifiable requirements and acceptance criteria from C, C++, Java, JNI or mixed-language source code. Use for module behavior analysis, end-to-end feature tracing across modules, or focused symbol investigation, including Android/AOSP and vendor implementations. Supports quick, standard and deep modes.
---

# Source to Requirements

## Mission
Reverse-engineer a **usable, evidence-backed requirements baseline** from existing source code. The final deliverable is a requirements specification that developers can implement against, testers can validate, and maintainers can use to assess behavior changes. Source investigation, evidence traceability, and classification are indispensable quality controls, not substitutes for the requirements deliverable. Reconstruct the current implemented contract without inventing original stakeholder intent or treating every implementation detail or suspected defect as a normative requirement. Read only; never modify analyzed source unless separately authorized.

## Inputs and defaults
- Target: a module, feature, symbol, or path. **User-specified scope takes precedence**: a module request uses a module boundary; a feature request follows its end-to-end observable behavior across modules as needed; a symbol request starts locally and expands only as necessary. If unspecified, ask for one target rather than scanning an entire monorepo.
- Mode: `standard` by default; `quick` for a narrow behavior, `deep` for complex state, cross-language boundaries, or high-risk behavior.
- Version/build: record repository/commit, module root(s), languages, build target and relevant product/variant when available; record Android version only if applicable. Mark unavailable fields unknown.
- Output: Markdown in conversation by default. Create user-facing deliverable files only when explicitly requested; run-local investigation records follow their own persistence rules; do not create three files merely because three templates exist.
- Output language: follow the user's request language unless explicitly overridden; see the output language policy below.

## Output language policy
- Default to the language used in the user's request, regardless of the language of source code, templates, or this skill's instructions.
- An explicit language request or `output_language` setting takes precedence. Supported values: `zh-CN` (Simplified Chinese), `en` (English), and `bilingual` (Chinese-English). If language cannot be determined, default to English.
- Do not generate bilingual output unless explicitly requested. In bilingual mode, provide aligned Chinese and English descriptions under the **same** requirement IDs, evidence references, and confidence classifications; do not generate duplicate independent requirement sets.
- Translate explanatory headings, table labels, requirements, scenarios, and summaries as appropriate. Treat the templates as structural skeletons, not mandatory English wording.
- Preserve identifiers, APIs, symbols, file paths, commands, log messages, literal configuration values, and source quotations exactly as written. Do not translate or alter evidence.
- Keep the technical meaning and coverage consistent across languages; avoid unnecessary duplication outside explicitly requested bilingual mode.

## Shared workflow principles
- **Reference and working input reliability gate:** Use the complete injected SKILL.md when available. Load each required reference in full before its first dependent operation, not in a bulk preflight dump. Keep file boundaries identifiable; use bounded reads or verified ranges and recover truncated, missing or garbled material in references, source and working records (including evidence and confidence). Do not assume a requested output limit overrides the host. Reuse loaded material; if recovery is impossible, disclose the concrete limitation and affected scope; do not mark unavailable material inspected or reconciled. No fixed platform token limit or reduced investigation scope.
- **Iteration and termination:** Continue or reopen work only for a concrete unresolved in-scope issue with a feasible next action. Obtain or assess evidence, correct facts or expression, or establish a concrete limitation. Never repeat the same action for the same issue under unchanged evidence and conditions. If stalled, try a materially different feasible approach; reopen resolved work only when affected by new evidence or changes. If no feasible path remains, retain the specific unknown or limitation and proceed with established evidence. Exit when completion conditions are met. Never skip feasible investigation or mandatory checks, or impose fixed iteration, token or tool-call budgets.
- **Quality:** Preserve material behavior, exact rules and evidence; distinguish implemented behavior from intent, proposed changes, defects and unknowns. Mechanical validation is not semantic completeness; static confirmation is not runtime verification. Never invent evidence or test results. Reuse checks and recheck affected claims only.
- The main workflow owns dependencies and stopping conditions; linked guides define required methods, not extra passes.

## Preparation
Load [environment preflight](references/environment-preflight.md) and [scope and module boundary](references/module-boundary.md). Perform targeted read-only checks; establish source readability, Git/Repo/plain-file context, relevant project revisions, dirty paths, languages, build/variant, observable entry and outcome, interfaces, assumptions and exclusions. Missing Git/Repo does not block readable file analysis; never sync, install or modify the workspace automatically.

Before eligibility/discovery load [code investigation](references/code-investigation.md). Apply Git source eligibility per owning project: tracked files (even if matching ignore patterns) plus non-ignored untracked files; ignored untracked files require explicit user-selected exceptions limited to the selected paths. Apply throughout discovery, tracing and evidence review. Do not bypass ignore rules with unrestricted searches; when Git is unavailable, use scoped files and disclose the limitation.

## Core workflow
Understand, Express and Review are three reasoning perspectives of one agent, not separate agents or handoff protocols. Iterate locally within each goal and return to affected work when necessary; complete feasible investigation before formal conversion.

### Understand
Establish what the source does, not how to classify it as requirements.

#### Investigation setup
Load [structural coverage](references/structural-coverage.md) and [behavior persistence](references/behavior-ledger.md). Initialize the ledger before structural source inspection or contract discovery (basic path enumeration may precede it). Establish the scoped candidate paths, independently discovered internal structures and coherent units using schema 2, not a file-only inventory. Apply in every mode proportionally; record exclusions and blocked paths.

#### Local investigation loop
Use coherent behavior batches, not separate global passes:
- Discover and refine independent component contracts and interaction boundaries using the boundary and code investigation guides. Use a compact target inventory, not a separate behavior analysis; capture established facts from discovery onward. Prefer targeted symbol, registration, test and configuration searches (`rg`, `git grep`, `git log`) and focused reads.
- Apply the four local behavior-analysis actions in [code investigation](references/code-investigation.md): define behavior, trace formation paths, compare material alternatives, record facts. Distinguish production paths from dead code/tests. Cross relevant boundaries to explain the requested outcome; avoid unrelated dependencies. Load [language analysis](references/language-analysis.md) in full before relevant C/C++/Java or mixed-language tracing; apply only relevant sections; optionally load [Android guidance](references/android-framework.md) for Android targets. Load [evidence validation](references/evidence-validation.md) before any evidence review, including local counterexample checks.
- Load [requirement extraction](references/requirement-extraction.md) before outcome reconstruction. Build and refine the required source-linked formation record for every identifiable core outcome and material lineage relationships during investigation, using the guide's mandatory fields. Multiple or no provable primary outcomes are legitimate; do not force a single root or invent intent. Every field must be evidenced or explicitly unresolved; a named outcome or output-field list is insufficient. Keep these internal records current as findings change.
- Follow the ledger checkpoint and structural lifecycle rules: persist recoverable material facts before corresponding inspected status and unrelated work, except disclosed in-context fallback. Combine writes only if ledger success precedes inspected status; otherwise use ordered separate writes. Never defer multiple batches to final capture. Keep unfinished units in progress and distinguish actual investigation from reads; update discovered dependencies, structures and affected records.

#### Investigation completion
Reconcile candidate/structure discovery, expansions and distinct contract partitioning. Continue feasible pending/in-progress work until requested behavior and material alternatives are checked, or concrete evidence/access/execution limitations prevent further work. Record actual blockers, unvisited paths and affected outcomes; permit partial conversion only of established evidence.

Ensure outcome/lineage records are current, persist findings, then perform the structural and ledger checks in their guides, including actual checkpoint execution. Repair accounting errors; resume affected investigation when feasible work remains. Disclose capture and validation limitations. Neither structural closure nor ledger validity proves semantic completeness.

### Express
Organize established behavior into verifiable requirements without losing material meaning.

#### Prepare conversion inputs
After Understand completion, explicitly reload current active ledger facts, evidence, confidence, unit associations and outcome/lineage records in coherent groups using the ledger guide. Use disclosed in-context fallback only if persistence is unavailable. Load [output routing](references/output-template.md) and applicable templates before drafting.

#### Local conversion loop
Apply the extraction guide's fact-driven organization and abstraction method. Identify distinct rules and variants before classification; express observable system, component and interface contracts, not source-file summaries. Preserve decisive conditions, thresholds, formulas, results, compatibility, failure scope, acceptance oracles and material technical context. A system requirement cannot replace an independent component contract; a call chain cannot substitute for an interface contract. Reconcile each group's actual draft against its input semantics and repair omissions before unrelated conversion.

#### Expression completion
Integrate groups and cross-group relationships; account for every active material rule in requirements, linked constraints, supporting context, conflicts, justified exclusions or unresolved issues. Apply the extraction guide's classification, granularity, normative ownership and final ID ordering rules. If inputs cannot be recovered after feasible attempts, convert reliable evidence only and disclose affected groups and incomplete reconciliation; do not claim complete expression.

### Review
Challenge established understanding and its expression, reusing local checks.

#### Review understanding
Apply both directions of [evidence validation](references/evidence-validation.md): seek supporting evidence and counterexamples for every assertion; use declared scope, structural/component inventories and outcome/lineage evidence to question missing material behavior. Do not treat the ledger as the limit of possible findings. Target evidence-based suspected omissions, insufficient or contradictory evidence, or affected conclusions, not another full investigation.

#### Review expression and integration
Complete the evidence guide's semantic reconciliation and quality checks against the actual draft, including core-outcome explainability from foundational FRs alone, normative self-containment, failure scope, contract granularity, acceptance precision, lineage consistency, ID/reference consistency, evidence precision and eligibility, and lossless view selection. Use existing local checks rather than duplicate passes. Understand covers identified material behavior in investigated source; Express covers expression of recorded behavior. Neither establishes exhaustive source coverage.

#### Resolve findings and confirm completion
For understanding errors, new evidence or unfinished investigation, return to affected Understand work, update records and repeat relevant completion checks; then reload affected Express inputs, revise and reconcile affected statements. For expression-only errors, return directly to affected Express work. Resume the interrupted goal (Express or Review) after repair. Recheck affected conclusions, final counts and limitations; apply the shared termination rule. Surface unresolved gaps and incomplete review honestly.

## Delivery
Follow [output routing](references/output-template.md), including its template conditions and lossless view selection. With source evidence, use [requirements template](templates/requirements.md) as the skeleton; otherwise provide an investigation plan. Read [call-chain template](templates/call-chain.md) only for meaningful multi-step/cross-boundary flows or explicit request; read [acceptance scenarios template](templates/test-scenarios.md) when meaningful branches, failures, permissions, variants, coverage or acceptance criteria are relevant or requested.

Lead with the reconstructed requirements baseline. Put identifiable core formation contracts before dependent capabilities; retain independently verifiable component/interface obligations. Provide verifiable acceptance conditions, traceable evidence, unknowns and limitations. Default to one Markdown answer/document; split into separate files only when requested.

| Mode | Investigation | Delivery |
|---|---|---|
| quick | Narrow behavior, critical branches | Compact requirements with evidence and verifiable outcomes |
| standard | Scoped module or end-to-end feature, interfaces, configuration and failure paths | Requirements; conditional flow and acceptance sections |
| deep | Complex state, cross-language/module differences, history where accessible | Same baseline plus applicable detailed views; perform branch/state, traceability and scoped coverage checks internally |

Expand depth only when evidence warrants it. Publish only supporting views with material information or a concrete review purpose, without dropping requested views or material semantics.

## Output constraints
- Use FR for observable functional contracts (including rejection, fallback and compatibility), NFR only for independently verifiable evidence-backed quality constraints, and UNK for unresolved questions. No default BR series. Follow extraction guidance for optional behavior-kind labels, granularity, stable IDs and authoritative normative ownership.
- Evidence: repository-relative path, symbol and verified line range, owning project commit for version-controlled paths and relevant uncommitted changes. If precise lines remain unavailable after required targeted verification, retain symbol and `line unverified` with the limitation. Confidence: confirmed, inferred or unknown per evidence validation. Negative claims require comprehensive search within stated scope; otherwise say `not found in inspected paths`.
- Every material FR/NFR must be independently verifiable and contain its material trigger/preconditions, governing rule (including decisive thresholds/formulas), observable result and applicable failure semantics, or explicitly link normative constraints. Acceptance criteria must state expected observable results, not test activities. Keep distinct failure propagation levels and independently observable obligations separate where evidenced.
- Keep material technical context, conflicts, inferred intent, defect hypotheses and proposed changes appropriately separate from normative behavior. Do not assert exploitability without verification. Distinguish existing tests from proposed tests; never claim unexecuted tests passed.
- Apply the detailed extraction, evidence validation and output routing quality checks at their relevant work goals. Keep normative rules in one authoritative location, preserve all material meaning and evidence, and report partial coverage rather than claiming exhaustive analysis.
