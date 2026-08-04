---
title: Beyond Magnitude and Shape: A Direction-Aware Loss for Time Series Forecasting
url: http://arxiv.org/abs/2608.01857v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_08-06-39Z_BeyondMagnitudeandShape_ADirection_AwareLossforTim.md
generated_at: 2026-08-03 23:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CosDir, a direction‑aware loss for time series forecasting that focuses on the sign of change rather than magnitude or shape. It shows that standard MSE losses ignore small directional moves and proposes CosDir to align prediction vectors using cosine similarity. Experiments demonstrate improved directional accuracy while maintaining magnitude performance.

## Key Takeaways
- CosDir uses cosine similarity to enforce alignment between predicted and target direction, making it scale‑invariant for small changes.
- The loss is lightweight and can be added as a plug‑in term without altering the model architecture.
- An adaptive version CosDir‑UW learns the optimal mixing weight per dataset during training.

## Context
Time series forecasting often relies on losses that optimize magnitude or shape, but they overlook the critical information of whether a series will increase or decrease. This gap limits performance in applications where direction matters, such as risk management and finance. The paper addresses this by introducing a simple yet effective directional loss.

## Implications
For practitioners, CosDir can be integrated into existing forecasting models to boost accuracy on subtle up‑down movements without retraining the whole network. In industry, this leads to more reliable predictions for financial risk and supply chain planning where direction is as important as magnitude. The adaptive extension further reduces the need for manual tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01857v1)
