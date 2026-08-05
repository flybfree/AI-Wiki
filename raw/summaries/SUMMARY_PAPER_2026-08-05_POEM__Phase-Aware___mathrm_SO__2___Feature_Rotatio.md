---
title: POEM: Phase-Aware $\mathrm{SO}(2)$ Feature Rotation for Time Series Forecasting Under Periodicity Drift
url: http://arxiv.org/abs/2608.03630v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_13-16-07Z_POEM_Phase_Aware__mathrm_SO__2__FeatureRotationfor.md
generated_at: 2026-08-05 01:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces POEM, a phase‑aware forecasting method that uses latent feature rotation via the special orthogonal group SO(2) to correct time series with varying cycle timing and phase. It learns a correction coordinate from historical phase increments using Directional Phase Increment Attention, enabling accurate extrapolation beyond fixed grids. Experiments show competitive accuracy while visualizing smoother latent trajectories.

## Key Takeaways
- POEM employs an invertible SO(2) rotation to align paired latent features, reducing variability caused by shifting cycle phases.
- The framework learns a phase‑correction coordinate that is extrapolated using DPIA, which pulls in similar historical phase increments for future predictions.
- Visual analyses reveal that the learned transformation regularizes latent trajectories, making them more predictable.

## Context
Time series forecasting often assumes fixed temporal grids, limiting adaptability to real‑world data where cycles drift. This paper addresses that limitation by introducing a dynamic phase correction mechanism rooted in linear algebra and attention mechanisms.

## Implications
For practitioners, POEM offers a principled way to handle seasonality changes without retraining models for each new phase. In industry, it can improve reliability of forecasts in domains such as energy demand or retail sales where seasonal patterns evolve.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03630v1)
