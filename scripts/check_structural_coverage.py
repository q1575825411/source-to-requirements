"""Validate structural investigation accounting; not semantic completeness."""
import argparse
import json
import sys
from collections import Counter


def validate(record):
    errors = []
    counts = Counter()
    if not isinstance(record, dict):
        return ["record must be an object"], counts
    if type(record.get("schema")) is not int or record["schema"] != 1:
        errors.append("unsupported schema")
    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())
    for field in ("scope", "enumeration"):
        if not nonempty(record.get(field)):
            errors.append("missing " + field)
    def strings(value):
        return isinstance(value, list) and all(nonempty(x) for x in value)
    candidates = record.get("candidates")
    if not strings(candidates):
        errors.append("candidates must be a list of nonempty paths")
        candidates = []
    if len(set(candidates)) != len(candidates):
        errors.append("duplicate candidate paths")
    candidate_set = set(candidates)
    assigned = set()
    ids = set()
    units = record.get("units")
    if not isinstance(units, list):
        errors.append("units must be a list")
        units = []
    for index, unit in enumerate(units):
        prefix = "unit {}".format(index + 1)
        if not isinstance(unit, dict):
            errors.append(prefix + ": expected object")
            continue
        uid = unit.get("id")
        if not nonempty(uid) or uid in ids:
            errors.append(prefix + ": missing or duplicate id")
        else:
            ids.add(uid)
            prefix = uid
        if not nonempty(unit.get("scope")):
            errors.append(prefix + ": missing scope")
        paths = unit.get("paths")
        if not strings(paths) or not paths:
            errors.append(prefix + ": missing or invalid paths")
        else:
            assigned.update(paths)
            if set(paths) - candidate_set:
                errors.append(prefix + ": paths outside candidate list")
        status = unit.get("status")
        if not isinstance(status, str) or status not in (
            "pending", "in_progress", "inspected", "excluded", "blocked"
        ):
            errors.append(prefix + ": invalid status")
            continue
        counts[status] += 1
        evidence = unit.get("evidence")
        if not strings(evidence):
            errors.append(prefix + ": evidence must be a list of strings")
        elif status == "inspected" and not evidence:
            errors.append(prefix + ": inspected without evidence")
        if status in ("excluded", "blocked") and not nonempty(unit.get("reason")):
            errors.append(prefix + ": missing reason")
    for path in sorted(candidate_set - assigned):
        errors.append("unassigned candidate: " + path)
    return errors, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record")
    args = parser.parse_args()
    try:
        with open(args.record, encoding="utf-8-sig") as stream:
            record = json.load(stream)
        errors, counts = validate(record)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    incomplete = sum(counts[s] for s in ("pending", "in_progress", "blocked"))
    print(json.dumps({"status_counts": dict(counts), "errors": errors,
                      "structural_closure": not errors and not incomplete,
                      "semantic_completeness_verified": False}, ensure_ascii=True))
    return 1 if errors else 2 if incomplete else 0


if __name__ == "__main__":
    sys.exit(main())
