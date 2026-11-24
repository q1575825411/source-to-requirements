"""Check Phase 2 bookkeeping, not semantic completeness."""
import json
import sys
from collections import Counter


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(structural, records):
    errors = []
    units = {u["id"]: u for u in structural["units"]}
    active = {}
    seen = set()
    for line, rec in enumerate(records, 1):
        if not isinstance(rec, dict):
            errors.append(f"record {line}: expected object")
            continue
        bid = rec.get("id")
        owners = rec.get("units")
        evidence = rec.get("evidence")
        if not nonempty(bid) or not nonempty(rec.get("fact")):
            errors.append(f"record {line}: missing id or fact")
            continue
        if (not isinstance(owners, list) or not owners
                or any(not nonempty(u) or u not in units for u in owners)):
            errors.append(f"{bid}: invalid unit references")
            continue
        if not isinstance(evidence, list) or not evidence or any(not nonempty(e) for e in evidence):
            errors.append(f"{bid}: missing evidence or limitation")
            continue
        if rec.get("confidence") not in ("confirmed", "inferred", "unknown"):
            errors.append(f"{bid}: invalid confidence")
            continue
        if "withdrawn_reason" in rec:
            if bid not in active or not nonempty(rec["withdrawn_reason"]):
                errors.append(f"{bid}: invalid withdrawal")
                continue
            del active[bid]
        else:
            active[bid] = rec
        seen.add(bid)
    covered = {u for rec in active.values() for u in rec["units"]}
    for uid, unit in units.items():
        for disposition in unit.get("dispositions", []):
            for bid in disposition["fact_ids"]:
                if bid not in active or uid not in active[bid]["units"]:
                    errors.append(f"{uid}: inactive or foreign disposition fact {bid}")
        if unit["status"] == "inspected" and not unit.get("dispositions"):
            errors.append(f"{uid}: inspected without structure dispositions")
    return errors, {
        "records": len(records),
        "distinct_ids": len(seen),
        "active_facts": len(active),
        "units_with_active_facts": len(covered),
        "confidence_counts": dict(Counter(r["confidence"] for r in active.values())),
    }


def main():
    if len(sys.argv) != 3:
        print("usage: check_behavior_ledger.py structural.json ledger.jsonl", file=sys.stderr)
        return 1
    try:
        with open(sys.argv[1], encoding="utf-8-sig") as f:
            structural = json.load(f)
        from check_structural_coverage import validate as validate_structure
        structural_errors, counts = validate_structure(structural)
        if structural_errors:
            raise ValueError("invalid structural record: " + str(structural_errors))
        with open(sys.argv[2], encoding="utf-8-sig") as f:
            records = [json.loads(line) for line in f if line.strip()]
        errors, summary = validate(structural, records)
    except (OSError, ValueError, TypeError, KeyError, ImportError) as exc:
        print(json.dumps({"errors": [str(exc)], "ledger_valid": False,
                          "semantic_completeness_verified": False}))
        return 1
    print(json.dumps({**summary, "errors": errors, "ledger_valid": not errors,
                      "semantic_completeness_verified": False}, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
