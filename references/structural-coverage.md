# Structural coverage (Phase 1)

Apply to quick, standard and deep runs, proportional to the requested scope. This is a source investigation control, not a behavior ledger or a requirement-count target.

## Inventory
After preflight and scope definition, enumerate eligible paths in each relevant owning project using the existing Git eligibility rules (use NUL-delimited Git output where supported); for plain files use a bounded directory enumeration without following directory symlinks. Record the enumeration method, root/revision and limitations. Never silently discard a candidate based on extension, name, size or apparent relevance. For feature/symbol requests, inventory the local boundary and expand along material dependencies; do not inventory an entire monorepo. Record inaccessible paths and explicit ignored exceptions. Do not read ignored untracked inputs without authorization.

Create a run-local JSON record outside the analyzed source tree and skill installation, using a writable temporary directory or authorized output location. Do not overwrite another run's record. If no writable location is available, keep an explicit in-context record and report that persistent validation is unavailable. Do not modify source, install dependencies, or require Python to continue analysis.

Schema (version 2; version 1 is not sufficient for closure):
```json
{
  "schema": 2,
  "scope": "requested boundary and mode",
  "enumeration": "commands, roots, revisions and limitations",
  "candidates": ["project-relative-or-qualified/path"],
  "structures": [
    {"id":"S-001","path":"project-relative-or-qualified/path","kind":"symbol","locator":"qualified symbol or verified range"}
  ],
  "units": [
    {"id":"U-001","scope":"logical component or symbol range","paths":["project-relative-or-qualified/path"],"structure_ids":["S-001"],"status":"pending","evidence":[],"reason":""}
  ]
}
```
Use unique project-qualified paths for multiple projects. Each enumerated candidate must be assigned to at least one unit, including explicitly excluded non-source or unrelated files. Group related paths when useful; split large or heterogeneous files into logical units as investigation reveals distinct contracts. Units may overlap. Keep the original candidate set and append newly discovered eligible dependencies; do not remove candidates to make closure pass. A missing/deleted/unreadable candidate is blocked, not silently dropped.

## Internal structure discovery (mandatory before unit closure)
For each candidate, inventory its internal source structures independently of the eventual requirements and investigation units. Use available language-aware symbol listing, parser, editor index, or targeted declaration/configuration searches plus source inspection; record the method and limitations in enumeration. Include functions/methods, entry points, declarations, state/configuration tables, top-level executable logic and other material non-symbol regions as applicable. For formats without symbols, enumerate logical sections/keys/records or verified source regions. Do not require a particular parser, language, line-count threshold, or one unit per function. Record inaccessible or opaque candidates as explicit structures assigned to blocked units; trivial/non-behavioral files may have a single structure with a justified exclusion.

Each structure has a stable ID, candidate path, kind and locator. No per-symbol prose description is required. Prefer compact machine-generated records from available discovery tools; a structure may represent a coherent symbol group or verified source region rather than an individual declaration. Retain the discovery output or its compact index as the reconciliation basis. Do not manually transcribe every symbol when a grouped locator can account for it precisely. Preserve the independently discovered list; reconcile against the discovery output before closure, including unassigned symbols and residual regions. Append newly discovered structures rather than deleting inconvenient entries. A whole-file placeholder is not a substitute for discoverable internal structures. If discovery cannot establish internal structure, record the limitation and keep affected units blocked rather than claiming inspection.

A structure accounts for source coverage; a unit defines a coherent investigation objective; a batch groups related units for actual investigation and capture. These are not one-to-one. Group related structures into units with a coherent behavior investigation objective; use compact grouped locators where they preserve independent discovery coverage. Source adjacency alone does not establish a coherent unit. Use compact lists of structure IDs for batch ownership; trivial files may use one structure and one unit. Scale granularity to distinct material contracts, not symbol count. Avoid redundant inventories, descriptions and status updates. This reduces bookkeeping only, never source investigation depth or evidence precision. Separate independently observable contracts or materially different decision, transformation, lifecycle, configuration or failure mechanisms when they require distinct investigation objectives; keep related variants together when their coverage remains explicit. Shared helpers may belong to multiple units. Every structure must map to at least one unit, and each unit's paths must exactly match the paths of its referenced structures. For a multi-contract file, explicitly check that the unit partition separates those contracts before marking any unit inspected. Do not use a single catch-all unit with a list of unrelated functions. Structural inventory is not a behavior ledger: no requirement IDs or extracted behavioral rules are required here.

Do not copy discovery locators as investigation evidence unless the corresponding source was actually investigated. A declaration listing is not investigation of its body. Account for relevant residual regions and material alternatives using targeted reads or equivalent source evidence.

## Investigation lifecycle
- pending: identified, not yet investigated.
- in_progress: investigation started, relevant portions remain.
- inspected: relevant entry points, modes, conditions, outputs, failures and interaction edges have been examined to the extent applicable; record actual source locations/ranges or symbols in evidence. A file read or grep hit alone does not qualify.
- excluded: outside behavioral scope or non-material input; give a specific reason. Do not exclude relevant code merely because it is complex, internal, large or not on the primary flow.
- blocked: a concrete evidence, access or execution limitation prevents further investigation; record the limitation and partial evidence. Unfinished but feasible work remains pending or in_progress.

Persist updates in batches at natural investigation checkpoints and before context compaction if possible. When applying Phase 2, persist material behavior facts successfully first, then mark the corresponding completed units inspected; follow the checkpoint and fallback rules in [behavior persistence](behavior-ledger.md). Reuse existing discovery results; do not repeatedly enumerate or reload the full inventory. Use targeted reads and validator summaries for unresolved items. No separate tool call is required for each structure or unit. Reopen units when new branches, configurations, dependencies or unresolved questions emerge. Record newly discovered units before following them. Do not use the inventory to cap source reads or replace existing call-chain, outcome, evidence or counterexample checks.

## Closure
At the investigation completion step in SKILL.md reconcile the candidate list and internal structure list with the original discovery outputs and subsequent expansions. Check unit coherence and distinct contract partitioning; the validator cannot judge semantic grouping. After feasible investigation and affected outcome/lineage updates are complete, run the bundled validator on current records with an available Python 3 interpreter:
`python <skill-root>/scripts/check_structural_coverage.py <run-record.json>`
Resolve the actual installed skill root from the loaded SKILL.md location, not the analyzed repository or current directory. Check the bundled script exists there; if missing, report incomplete skill packaging and use the manual fallback without claiming automatic validation. Use the actual interpreter and path for the platform. If unavailable, manually check the same invariants and explicitly state that the script was not run. Repair structural errors and continue pending/in-progress units while investigation remains feasible within scope. A valid ledger is not a substitute for closure. If a concrete evidence, access or execution limit prevents completion, record affected units and reasons (mark blocked where appropriate), and permit partial conversion of established evidence only. Recheck affected records if later review reopens investigation; never claim false completion.

The validator checks record structure and status accounting only; it cannot prove enumeration completeness, source reachability, semantic understanding or requirement coverage. Report candidate, structure and unit counts separately, explicitly state that semantic completeness is not verified by the validator, counts by status, material exclusions, blocked/unvisited units and limitations in the existing provenance/coverage section. Do not publish the full inventory unless requested. Preserve existing quality gates and output routing. Phase 2 adds a separate behavior ledger linked to unit IDs; this structural record remains an investigation inventory. No historical requirements baseline or explicit behavior-to-requirement mapping is required.
