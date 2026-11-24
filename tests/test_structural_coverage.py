import importlib.util
import pathlib
import unittest

path = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "check_structural_coverage.py"
spec = importlib.util.spec_from_file_location("coverage_check", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CoverageTests(unittest.TestCase):
    def record(self):
        return {"schema": 2, "scope": "module", "enumeration": "git",
                "candidates": ["a.c", "README"],
                "structures": [
                    {"id":"S-1","path":"a.c","kind":"symbol","locator":"entry","description":"entry point"},
                    {"id":"S-2","path":"README","kind":"section","locator":"whole","description":"notes"}],
                "units": [
                    {"id": "U-1", "scope": "entry", "paths": ["a.c"], "structure_ids": ["S-1"],
                     "status": "inspected", "evidence": ["a.c:1-20"], "reason": ""},
                    {"id": "U-2", "scope": "notes", "paths": ["README"], "structure_ids": ["S-2"],
                     "status": "excluded", "evidence": [], "reason": "unrelated notes"}]}

    def test_valid(self):
        errors, counts = module.validate(self.record())
        self.assertEqual(errors, [])
        self.assertEqual(counts["inspected"], 1)

    def test_unassigned(self):
        record = self.record()
        record["candidates"].append("b.c")
        self.assertIn("unassigned candidate: b.c", module.validate(record)[0])

    def test_missing_evidence(self):
        record = self.record()
        record["units"][0]["evidence"] = []
        self.assertTrue(module.validate(record)[0])

    def test_missing_exclusion_reason(self):
        record = self.record()
        record["units"][1]["reason"] = ""
        self.assertTrue(module.validate(record)[0])

    def test_pending_is_accounted_not_inspected(self):
        record = self.record()
        record["units"][0]["status"] = "pending"
        errors, counts = module.validate(record)
        self.assertFalse(errors)
        self.assertEqual(counts["pending"], 1)

    def test_invalid_status(self):
        record = self.record()
        record["units"][0]["status"] = []
        self.assertTrue(module.validate(record)[0])

    def test_unassigned_internal_structure(self):
        record = self.record()
        record["structures"].append({"id":"S-3","path":"a.c","kind":"symbol",
                                     "locator":"other","description":"another contract"})
        self.assertIn("unassigned structure: S-3", module.validate(record)[0])

    def test_file_only_schema_rejected(self):
        record = self.record()
        record["schema"] = 1
        del record["structures"]
        self.assertTrue(module.validate(record)[0])

    def test_unknown_structure(self):
        record = self.record()
        record["units"][0]["structure_ids"] = ["missing"]
        self.assertTrue(module.validate(record)[0])

    def test_path_mismatch(self):
        record = self.record()
        record["units"][0]["structure_ids"] = ["S-2"]
        self.assertIn("U-1: paths do not match structures", module.validate(record)[0])

    def test_duplicate_id(self):
        record = self.record()
        record["units"][1]["id"] = "U-1"
        self.assertTrue(module.validate(record)[0])


if __name__ == "__main__":
    unittest.main()
