"""
default_probability_scorer.py - Calculates corporate debt-to-equity ratio and risk tier classification
"""
import sys
import json


def score_default_risk(balance_sheet_json: str, max_de_ratio: float = 3.5):
    import json
    data = json.loads(balance_sheet_json) if isinstance(balance_sheet_json, str) else balance_sheet_json
    debt = data.get("total_debt", 300000.0)
    equity = max(data.get("equity_value", 100000.0), 1.0)
    ratio = debt / equity
    is_safe = ratio <= max_de_ratio
    return {
        "total_debt": debt,
        "equity": equity,
        "debt_to_equity": round(ratio, 2),
        "risk_tier": "LOW_RISK" if ratio <= 2.0 else ("MODERATE_RISK" if is_safe else "HIGH_DEFAULT_RISK"),
        "status": "APPROVED_LEVERAGE" if is_safe else "EXCESSIVE_LEVERAGE"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "default-probability-scorer"}))
