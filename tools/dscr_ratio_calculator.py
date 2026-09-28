"""
dscr_ratio_calculator.py - Calculates Debt Service Coverage Ratio (DSCR) from Net Operating Income and Total Debt Service
"""
import sys
import json


def calculate_dscr(financials_json: str, min_required_dscr: float = 1.25):
    import json
    data = json.loads(financials_json) if isinstance(financials_json, str) else financials_json
    noi = data.get("net_operating_income", 150000.0)
    debt_service = max(data.get("annual_debt_service", 100000.0), 1.0)
    dscr = noi / debt_service
    approved = dscr >= min_required_dscr
    return {
        "noi": noi,
        "debt_service": debt_service,
        "dscr": round(dscr, 2),
        "compliant": approved,
        "status": "DSCR_APPROVED" if approved else "DSCR_INSUFFICIENT"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "dscr-ratio-calculator"}))
