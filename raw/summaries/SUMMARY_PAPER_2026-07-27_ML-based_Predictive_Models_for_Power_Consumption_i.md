---
title: ML-based Predictive Models for Power Consumption in Virtualised O-RANs
url: http://arxiv.org/abs/2607.24256v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_10-46-29Z_ML_basedPredictiveModelsforPowerConsumptioninVirtu.md
generated_at: 2026-07-27 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes machine learning models to predict power consumption in virtualized O-RANs using hardware-instrumented data. It compares three deep neural network variants and a hybrid DNN-XGBoost approach, finding the hybrid achieves mean relative error below 0.5%.

## Key Takeaways
- The hybrid model combines DNN feature extraction with XGBoost regressor for superior accuracy.
- Mean relative error drops to under half percent across varied system parameters.
- Real‑world O-RAN management tools could leverage this accuracy for energy optimization.

## Context
Virtualized radio access networks demand precise power modeling beyond traditional linear methods. AI‑driven regression models address the nonlinear complexity of modern communication hardware, aligning with trends toward software-defined resource allocation.

## Implications
Practitioners can integrate these hybrid models into network orchestration platforms to reduce operational costs and carbon footprints. The findings set a benchmark for energy‑aware AI in edge communications, encouraging further research on scalability and robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24256v1)
