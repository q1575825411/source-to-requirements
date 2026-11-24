import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_behavior_ledger import validate


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.structural = {"units": [{"id": "U-1", "status": "inspected", "dispositions": [{"fact_ids": ["B-1"]}]}]}
        self.fact = {"id": "B-1", "units": ["U-1"], "fact": "Reject invalid input.",
                     "evidence": ["a.py:10-12"], "confidence": "confirmed"}

    def check(self, records):
        return validate(self.structural, records)

    def test_valid(self):
        self.assertFalse(self.check([self.fact])[0])

    def test_missing(self):
        self.assertTrue(self.check([])[0])

    def test_no_material_reason(self):
        self.structural["units"][0]["dispositions"][0] = {"fact_ids": [], "reason": "Declaration only."}
        self.assertFalse(self.check([])[0])

    def test_missing_disposition_fact(self):
        self.structural["units"][0]["dispositions"].append({"fact_ids": ["B-2"]})
        self.assertTrue(self.check([self.fact])[0])

    def test_foreign_disposition_fact(self):
        self.structural["units"].append({"id": "U-2", "status": "pending"})
        self.assertTrue(self.check([dict(self.fact, units=["U-2"])])[0])

    def test_unknown_unit(self):
        self.assertTrue(self.check([dict(self.fact, units=["U-2"])])[0])

    def test_missing_evidence(self):
        self.assertTrue(self.check([dict(self.fact, evidence=[])])[0])

    def test_invalid_confidence(self):
        self.assertTrue(self.check([dict(self.fact, confidence="verified")])[0])

    def test_revision(self):
        errors, summary = self.check([self.fact, dict(self.fact, fact="Return error.")])
        self.assertFalse(errors)
        self.assertEqual(summary["active_facts"], 1)

    def test_withdrawal(self):
        errors, summary = self.check([self.fact, dict(self.fact, withdrawn_reason="Unreachable.")])
        self.assertTrue(errors)
        self.assertEqual(summary["active_facts"], 0)

    def test_invalid_withdrawal(self):
        self.assertTrue(self.check([dict(self.fact, withdrawn_reason="Unreachable.")])[0])

    def test_pending_unit(self):
        self.structural["units"][0]["status"] = "pending"
        self.structural["units"][0]["dispositions"] = []
        self.assertFalse(self.check([])[0])


if __name__ == "__main__":
    unittest.main()
