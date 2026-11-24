# Structural coverage (Phase 1)

Apply to quick, standard and deep runs, proportional to the requested scope. This is a source investigation control, not a behavior ledger or a requirement-count target.

## Inventory
After preflight and scope definition, enumerate eligible paths in each relevant owning project using the existing Git eligibility rules (use NUL-delimited Git output where supported); for plain files use a bounded directory enumeration without following directory symlinks. Record the enumeration method, root/revision and limitations. Never silently discard a candidate based on extension, name, size or apparent relevance. For feature/symbol requests, inventory the local boundary and expand along material dependencies; do not inventory an entire monorepo. Record inaccessible paths and explicit ignored exceptions. Do not read ignored untracked inputs without authorization.

Create a run-local JSON record outside the analyzed source tree and skill installation, using a writable temporary directory or authorized output location. Do not overwrite another run's record. If no writable location is available, keep an explicit in-context record and report that persistent validation is unavailable. Do not modify source, install dependencies, or require Python to continue analysis.

Schema (version 1):
```json
{
  "schema": 1,
  "scope": "requested boundary and mode",
  "enumeration": "commands, roots, revisions and limitations",
  "candidates": ["project-relative-or-qualified/path"],
  "units": [
    {"id":"U-001","scope":"logical component or symbol range","paths":["project-relative-or-qualified/path"],"status":"pending","evidence":[],"reason":""}
  ]
}
```
Use unique project-qualified paths for multiple projects. Each enumerated candidate must be assigned to at least one unit, including explicitly excluded non-source or unrelated files. Group related paths when useful; split large or heterogeneous files into logical units as investigation reveals distinct contracts. Units may overlap. Keep the original candidate set and append newly discovered eligible dependencies; do not remove candidates to make closure pass. A missing/deleted/unreadable candidate is blocked, not silently dropped.

## Investigation lifecycle
- pending: identified, not yet investigated.
- in_progress: investigation started, relevant portions remain.
- inspected: relevant entry points, modes, conditions, outputs, failures and interaction edges have been examined to the extent applicable; record actual source locations/ranges or symbols in evidence. A file read or grep hit alone does not qualify.
- excluded: outside behavioral scope or non-material input; give a specific reason. Do not exclude relevant code merely because it is complex, internal, large or not on the primary flow.
- blocked: evidence unavailable or investigation incomplete; record the concrete limitation and any partial evidence.

Persist updates during investigation, after each logical unit or batch, and before context compaction if possible. Reopen units when new branches, configurations, dependencies or unresolved questions emerge. Record newly discovered units before following them. Do not use the inventory to cap source reads or replace existing call-chain, outcome, evidence or counterexample checks.

## Closure
Before delivery reconcile the candidate list with the original enumeration and subsequent expansions. Run the bundled validator with an available Python 3 interpreter:
`python <skill-root>/scripts/check_structural_coverage.py <run-record.json>`
Use the actual interpreter and path for the platform. If unavailable, manually check the same invariants and explicitly state that the script was not run. Repair structural errors; continue investigating pending/in-progress units when possible. If evidence or execution limits prevent completion, retain their status or mark blocked with a concrete reason and deliver partial coverage, never a false completion claim.

The validator checks record structure and status accounting only; it cannot prove enumeration completeness, source reachability, semantic understanding or requirement coverage. Report concise counts by status, material exclusions, blocked/unvisited units and limitations in the existing provenance/coverage section. Do not publish the full inventory unless requested. Preserve existing quality gates and output routing. No historical requirements baseline, behavior ledger or behavior-to-requirement mapping is introduced in this phase.
