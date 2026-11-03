import pytest
from event_ticket_tier import process_ticket_manifest, monitor_gate_flow


def test_invalid_input():
    with pytest.raises(ValueError):
        process_ticket_manifest(None, 0.1)

    with pytest.raises(ValueError):
        process_ticket_manifest([], -0.1)


def test_all_ticket_tiers_and_discounts():
    manifests = [
        {
            "is_confirmed": True,
            "tier": "vip",
            "exclusive_lounge": True,
            "orders": [
                {"qty": 2, "promo": ""},
                {"qty": 1, "promo": "EARLYBIRD"}
            ]
        },
        {
            "is_confirmed": True,
            "tier": "premium",
            "exclusive_lounge": False,
            "orders": [
                {"qty": 5, "promo": ""},
                {"qty": 1, "promo": "EARLYBIRD"}
            ]
        },
        {
            "is_confirmed": True,
            "tier": "general",
            "exclusive_lounge": False,
            "orders": [{"qty": 1, "promo": ""}]
        }
    ]

    result = process_ticket_manifest(manifests, 0.1)
    assert result["status"] == "COMPLETED"
    assert result["total_revenue"] > 0


def test_unconfirmed_and_invalid_tier():
    manifests = [
        {
            "is_confirmed": False,
            "tier": "vip",
            "orders": [{"qty": 2, "promo": ""}]
        },
        {
            "is_confirmed": True,
            "tier": "student",
            "orders": [{"qty": 2, "promo": ""}]
        }
    ]

    result = process_ticket_manifest(manifests, 0.1)
    assert result["status"] == "ZERO_SALES"
    assert result["total_revenue"] == 0.0


def test_invalid_quantity_and_non_vip_fraud():
    manifests = [
        {
            "is_confirmed": True,
            "tier": "general",
            "orders": [
                {"qty": 0, "promo": ""},
                {"qty": 2, "promo": "FRAUD_RISK"}
            ]
        }
    ]

    result = process_ticket_manifest(manifests, 0.1)
    assert result["status"] == "COMPLETED"
    assert result["total_revenue"] == 99.0


def test_vip_fraud_rejection():
    manifests = [
        {
            "is_confirmed": True,
            "tier": "vip",
            "exclusive_lounge": False,
            "orders": [
                {"qty": 2, "promo": ""},
                {"qty": 1, "promo": "FRAUD_RISK"},
                {"qty": 3, "promo": ""}
            ]
        }
    ]

    result = process_ticket_manifest(manifests, 0.1)
    assert result["status"] == "ZERO_SALES"


def test_audit_rejection():
    manifests = [
        {
            "is_confirmed": True,
            "tier": "general",
            "orders": [{"qty": 0, "promo": ""} for _ in range(5)]
        }
    ]

    result = process_ticket_manifest(manifests, 0.1)
    assert result["status"] == "AUDIT_REJECTED"


def test_zero_sales():
    result = process_ticket_manifest([], 0.1)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_SALES"


def test_gate_flow_no_data():
    assert monitor_gate_flow([]) == "NO_DATA"


def test_gate_flow_overflow():
    assert monitor_gate_flow([[60, 55]]) == "OVERFLOW"


def test_gate_flow_normal():
    assert monitor_gate_flow([[60, 40, 60], [30, 45]]) == "FLOW_NORMAL"