"""
credit_covenant_auditor.py - Audits borrower loan-to-value (LTV) percentage against commercial collateral limits
"""
import sys
import json


def audit_credit_covenants(collateral_data_json: str, max_ltv_pct: float = 75.0):
    import json
    data = json.loads(collateral_data_json) if isinstance(collateral_data_json, str) else collateral_data_json
    loan = data.get("loan_amount", 600000.0)
    value = max(data.get("appraised_property_value", 1000000.0), 1.0)
    ltv = (loan / value) * 100.0
    compliant = ltv <= max_ltv_pct
    return {
        "loan_amount": loan,
        "collateral_value": value,
        "ltv_percentage": round(ltv, 2),
        "compliant": compliant,
        "status": "LTV_COMPLIANT" if compliant else "LTV_EXCEEDED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "credit-covenant-auditor"}))
