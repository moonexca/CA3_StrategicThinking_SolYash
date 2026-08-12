from pathlib import Path

import numpy as np

from src.modeling import (
    FEATURES,
    TARGET,
    TARGET_DERIVED_FEATURES,
    evaluate_forward_holdout,
    load_panel,
)


ROOT = Path(__file__).resolve().parents[1]


def test_feature_contract_has_no_target_leakage():
    assert TARGET not in FEATURES
    assert not set(FEATURES).intersection(TARGET_DERIVED_FEATURES)


def test_panel_is_unique_and_forward_metrics_are_finite():
    panel = load_panel(ROOT / "BSA02.20250516T100541.csv")
    assert not panel.duplicated(["year", "ownership"]).any()
    assert set(panel["value_kind"]) == {"actual", "estimate"}

    metrics, predictions = evaluate_forward_holdout(panel)
    assert set(metrics["model"]) == {
        "Last observation",
        "Log-linear trend",
        "Random forest",
    }
    assert np.isfinite(metrics[["rmse", "mae", "smape_pct", "r2"]]).all().all()
    assert predictions["year"].min() >= 2021
