# Model card: corrected R&D expenditure benchmark

## Intended use

This benchmark tests whether a simple time trend and ownership category can
generalise to later R&D expenditure observations. It is a portfolio validation
exercise, not a forecasting system for policy or investment decisions.

## Leakage corrected

The historical notebook predicted `rd_expenditure` while including
`log_rd_expenditure`, R&D intensity, and other values calculated from the target.
That made a near-perfect R² inevitable and invalid as evidence of generalisation.

The corrected feature contract contains only:

- reporting year
- ownership category

Rows for “All nationalities” are excluded from modelling because they aggregate
the Irish and non-Irish series already present in the panel.

## Validation design

- Training period: 2007–2020
- Forward holdout: 2021–2024
- Baseline: last observed training value by ownership
- Candidates: log-linear ridge trend and random forest
- Metrics: RMSE, MAE, sMAPE, and R²

Actual totals are used in odd years and official estimates in even years. The
`value_kind` field preserves that provenance. Exact results and predictions are
committed under [`results/`](results/).

## Limitations

The sample is extremely small, reporting alternates between actual and estimated
values, and the 2023 series contains a large structural jump. Results should be
read as a stress test of modelling discipline, not as operational forecasts.
