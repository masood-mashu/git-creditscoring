"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitCreditScoring.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.dscr_ratio_calculator import *
from tools.default_probability_scorer import *
from tools.credit_covenant_auditor import *

class TestGitCreditScoringPredictability(unittest.TestCase):

    def test_dscr_ratio_calculator(self):
        res = calculate_dscr('{"net_operating_income": 150000, "annual_debt_service": 100000}')
        self.assertTrue(res["compliant"])
        self.assertEqual(res["status"], "DSCR_APPROVED")

    def test_default_probability_scorer(self):
        res = score_default_risk('{"total_debt": 250000, "equity_value": 100000}')
        self.assertEqual(res["risk_tier"], "MODERATE_RISK")
        self.assertEqual(res["status"], "APPROVED_LEVERAGE")

    def test_credit_covenant_auditor(self):
        res = audit_credit_covenants('{"loan_amount": 700000, "appraised_property_value": 1000000}')
        self.assertTrue(res["compliant"])
        self.assertEqual(res["status"], "LTV_COMPLIANT")


if __name__ == "__main__":
    unittest.main()
