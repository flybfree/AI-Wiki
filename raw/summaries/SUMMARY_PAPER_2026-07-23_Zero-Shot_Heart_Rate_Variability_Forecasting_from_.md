---
title: Zero-Shot Heart Rate Variability Forecasting from Consumer Wearables Using Time Series Foundation Models
url: http://arxiv.org/abs/2607.20027v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_11-12-07Z_Zero_ShotHeartRateVariabilityForecastingfromConsum.md
generated_at: 2026-07-23 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates short‑term heart rate variability forecasting using three time series foundation models on fragmented wearable data from 49 healthy individuals, showing that TSFMs surpass traditional baselines without fine‑tuning and achieve low MASE values up to a two‑hour horizon.  

## Key Takeaways
- The study demonstrates that TimesFM, Chronos, and MOIRAI outperform mean, exponential smoothing, and EWMA methods on real‑world HRV signals, with average MASE between 0.81 and 0.87 across both 32‑ and 64‑step contexts.  
- A variability‑preserving imputation technique that combines linear interpolation with locally adaptive stochastic noise is introduced to maintain physiological dynamics despite data fragmentation.  
- Chronos and TimesFM are identified as the top performing models, while MOIRAI offers only marginal improvements over baseline methods.  

## Context
Time series foundation models have recently demonstrated strong performance on diverse sequence tasks, yet their application to medical signal forecasting remains limited due to challenges posed by noisy, incomplete data streams from consumer devices. This work bridges that gap by applying TSFMs directly to HRV, highlighting the potential of model‑agnostic architectures for health monitoring applications.  

## Implications
These results suggest that TSFMs can serve as a reliable baseline for short‑term physiological forecasting without extensive customization, encouraging further research into domain‑specific fine‑tuning and clinical integration. The approach may streamline deployment of wearable‑based health analytics, offering early warnings for autonomic dysfunction or cardiac events with minimal additional development effort.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20027v1)
