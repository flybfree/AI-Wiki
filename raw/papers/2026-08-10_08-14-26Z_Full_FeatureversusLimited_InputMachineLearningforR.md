---
title: Full-Feature versus Limited-Input Machine Learning for Residential Energy Estimation: A Comparative Analysis of RECS and ResStock Under Realistic Input Constraints
published: 2026-08-10T08:14:26Z
authors: Aditya Ramnarayan, Fatih Evren, Patti Gunderson, Samuel Rosenberg
url: http://arxiv.org/abs/2608.09255v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Full-Feature versus Limited-Input Machine Learning for Residential Energy Estimation: A Comparative Analysis of RECS and ResStock Under Realistic Input Constraints

## Abstract
Residential energy estimates are often needed before detailed envelope characteristics, equipment efficiencies, infiltration, sensor, or billing data are available. This study quantifies the trade-off between predictive accuracy and input accessibility using two nationally representative U.S. residential-energy datasets: the survey-based Residential Energy Consumption Survey (RECS) and the simulation-based ResStock dataset. Full-feature models were first used to establish dataset-specific performance benchmarks. For total-energy estimation, the models were subsequently restricted to ten low-burden variables obtainable from occupants, administrative records, or location-based weather data without an on-site energy audit. Among CatBoost, XGBoost, LightGBM, Random Forest, and Neural Networks, CatBoost consistently achieved the highest predictive performance for the full-feature analysis, reaching R2 = 0.90 for ResStock and R2 = 0.73 for RECS. When the feature set was restricted to ten homeowner-accessible inputs to simulate realistic deployment conditions, model performance converged to R2 = 0.61 for RECS and R2 = 0.62 for ResStock, showing that algorithmic complexity cannot fully compensate for missing physical and behavioral information. However, for a more homogeneous ResStock cohort consisting of single-family detached, natural-gas-heated homes in Climate Zone 6A constructed between 2000 and 2010, a reduced-input model improved accuracy to R2 = 0.85, demonstrating the value of targeted modeling for homogeneous populations. The results indicate that tree-based ensemble models can serve as high-fidelity emulators of national-scale residential energy datasets. However, careful consideration of feature availability, dataset origin (empirical vs. synthetic), and applicable use cases are also important.

## Metadata
- **Published**: 2026-08-10T08:14:26Z
- **Authors**: Aditya Ramnarayan, Fatih Evren, Patti Gunderson, Samuel Rosenberg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09255v1)