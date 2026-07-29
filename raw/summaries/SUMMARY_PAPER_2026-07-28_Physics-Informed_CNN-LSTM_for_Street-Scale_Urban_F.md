---
title: Physics-Informed CNN-LSTM for Street-Scale Urban Flood Prediction: Reconciling Aggregate Accuracy and Street-Level Plausibility
url: http://arxiv.org/abs/2607.25148v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_23-46-25Z_Physics_InformedCNN_LSTMforStreet_ScaleUrbanFloodP.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a physics-informed CNN-LSTM model for predicting urban flood depths on a street-scale grid, aiming to improve both statistical accuracy and physical plausibility. It demonstrates that adding gravity, continuity, and topography-aware penalties reduces unrealistic predictions such as uphill flow while preserving high recall in street channels. The constrained model outperforms the baseline on street-level metrics, especially under realistic conditions.

## Key Takeaways
- The gravity loss penalizes depth increases that violate the water-surface-elevation gradient, achieving near-zero violations of order 1e-6.
- The continuity loss enforces local mass conservation with rainfall-adaptive thresholds, ensuring physically consistent flow across the grid.
- The TWI-modulated false-alarm penalty balances accuracy and street recall, recovering 60% higher street recall at the lowest MAE among constrained variants.

## Context
Urban flood prediction requires models that respect physical laws to be useful for traffic routing and emergency response. Existing deep learning surrogates often ignore constraints leading to implausible outputs, limiting real-world deployment. This work bridges the gap between statistical performance and domain-specific feasibility, highlighting a need for physics-aware loss functions in AI.

## Implications
Practitioners can adopt differentiable penalty terms to enforce physical consistency without sacrificing accuracy, improving reliability of flood forecasts for urban infrastructure management. The approach offers a template for integrating environmental constraints into neural network training across other geospatial applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25148v1)
