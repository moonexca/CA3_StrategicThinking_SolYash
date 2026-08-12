"""Small-data, leakage-safe benchmark for Irish R&D expenditure.

The source alternates between actual totals in odd years and estimates in even
years. This module keeps that provenance, avoids target-derived predictors, and
uses a forward holdout instead of a random row split.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ACTUAL_LABEL = "Actual Total Research and Development Expenditure"
ESTIMATED_LABEL = "Estimated Total Research and Development Expenditure"
TARGET = "rd_expenditure"
FEATURES = ("year", "ownership")
EXCLUDED_AGGREGATE = "All nationalities of ownership"

TARGET_DERIVED_FEATURES = frozenset(
    {
        "log_rd_expenditure",
        "rd_intensity_per_enterprise",
        "log_rd_intensity_per_enterprise",
        "fdi_exposure_score",
    }
)


def load_panel(path: str | Path) -> pd.DataFrame:
    """Build one non-aggregate observation per ownership group and year."""

    raw = pd.read_csv(path)
    required = {"Statistic Label", "Year", "Nationality of Ownership", "VALUE"}
    missing = sorted(required.difference(raw.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    selected = raw.loc[
        raw["Statistic Label"].isin([ACTUAL_LABEL, ESTIMATED_LABEL]),
        ["Statistic Label", "Year", "Nationality of Ownership", "VALUE"],
    ].copy()
    selected = selected[selected["Nationality of Ownership"] != EXCLUDED_AGGREGATE]
    selected = selected.rename(
        columns={"Year": "year", "Nationality of Ownership": "ownership"}
    )
    selected["value_kind"] = np.where(
        selected["Statistic Label"].eq(ACTUAL_LABEL), "actual", "estimate"
    )
    selected = selected.dropna(subset=["VALUE"])

    duplicates = selected.duplicated(["year", "ownership"], keep=False)
    if duplicates.any():
        raise ValueError("More than one total R&D value exists for an ownership-year")

    panel = selected.rename(columns={"VALUE": TARGET}).drop(
        columns=["Statistic Label"]
    )
    panel = panel.sort_values(["year", "ownership"], ignore_index=True)

    if TARGET in FEATURES or set(FEATURES).intersection(TARGET_DERIVED_FEATURES):
        raise AssertionError("The feature set contains target-derived information")
    return panel


def _pipeline(model) -> Pipeline:
    preparation = ColumnTransformer(
        [
            ("year", StandardScaler(), ["year"]),
            ("ownership", OneHotEncoder(handle_unknown="ignore"), ["ownership"]),
        ]
    )
    return Pipeline([("prepare", preparation), ("model", model)])


def _smape(actual: np.ndarray, predicted: np.ndarray) -> float:
    denominator = np.abs(actual) + np.abs(predicted)
    ratio = np.divide(
        2 * np.abs(predicted - actual),
        denominator,
        out=np.zeros_like(actual, dtype=float),
        where=denominator != 0,
    )
    return float(100 * ratio.mean())


def _metric_row(name: str, actual: np.ndarray, predicted: np.ndarray) -> dict:
    return {
        "model": name,
        "rmse": float(root_mean_squared_error(actual, predicted)),
        "mae": float(mean_absolute_error(actual, predicted)),
        "smape_pct": _smape(actual, predicted),
        "r2": float(r2_score(actual, predicted)),
    }


def evaluate_forward_holdout(
    panel: pd.DataFrame, *, holdout_start: int = 2021, random_state: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Train on earlier years and evaluate only on later, unseen years."""

    train = panel[panel["year"] < holdout_start].copy()
    test = panel[panel["year"] >= holdout_start].copy()
    if train.empty or test.empty:
        raise ValueError("The chosen holdout does not create non-empty train and test sets")

    prediction_rows: list[pd.DataFrame] = []
    metric_rows: list[dict] = []

    last_by_owner = (
        train.sort_values("year").groupby("ownership")[TARGET].last().to_dict()
    )
    baseline = test["ownership"].map(last_by_owner).to_numpy(dtype=float)
    metric_rows.append(_metric_row("Last observation", test[TARGET].to_numpy(), baseline))
    prediction_rows.append(
        test.assign(model="Last observation", prediction=baseline)
    )

    candidates = {
        "Log-linear trend": _pipeline(Ridge(alpha=1.0)),
        "Random forest": _pipeline(
            RandomForestRegressor(
                n_estimators=300,
                min_samples_leaf=2,
                random_state=random_state,
                n_jobs=-1,
            )
        ),
    }
    X_train = train.loc[:, FEATURES]
    X_test = test.loc[:, FEATURES]
    y_train = np.log1p(train[TARGET].to_numpy())

    for name, model in candidates.items():
        model.fit(X_train, y_train)
        predicted = np.maximum(0, np.expm1(model.predict(X_test)))
        metric_rows.append(_metric_row(name, test[TARGET].to_numpy(), predicted))
        prediction_rows.append(test.assign(model=name, prediction=predicted))

    metrics = pd.DataFrame(metric_rows).sort_values("rmse", ignore_index=True)
    predictions = pd.concat(prediction_rows, ignore_index=True)
    return metrics, predictions


def save_results(
    panel: pd.DataFrame,
    metrics: pd.DataFrame,
    predictions: pd.DataFrame,
    output_dir: str | Path,
) -> None:
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    panel.to_csv(destination / "validated_rd_panel.csv", index=False)
    metrics.round(3).to_csv(destination / "forward_holdout_metrics.csv", index=False)
    predictions.round(3).to_csv(destination / "forward_holdout_predictions.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), sharey=True)
    for ax, ownership in zip(axes, sorted(predictions["ownership"].unique())):
        subset = predictions[predictions["ownership"].eq(ownership)]
        actual = subset.drop_duplicates("year")
        ax.plot(actual["year"], actual[TARGET], marker="o", label="Observed")
        for model_name, model_rows in subset.groupby("model"):
            ax.plot(
                model_rows["year"],
                model_rows["prediction"],
                marker="o",
                linestyle="--",
                label=model_name,
            )
        ax.set_title(ownership)
        ax.set_xlabel("Holdout year")
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("R&D expenditure (source units)")
    axes[1].legend(fontsize=8)
    fig.suptitle("Forward holdout: observed vs predicted R&D expenditure")
    fig.tight_layout()
    fig.savefig(destination / "forward_holdout_comparison.png", dpi=160)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default="BSA02.20250516T100541.csv")
    parser.add_argument("--output-dir", default="results")
    parser.add_argument("--holdout-start", type=int, default=2021)
    args = parser.parse_args()

    panel = load_panel(args.data)
    metrics, predictions = evaluate_forward_holdout(
        panel, holdout_start=args.holdout_start
    )
    save_results(panel, metrics, predictions, args.output_dir)
    print(metrics.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
