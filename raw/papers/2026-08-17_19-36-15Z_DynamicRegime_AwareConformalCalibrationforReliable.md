---
title: Dynamic Regime-Aware Conformal Calibration for Reliable Economic Forecast Intervals under Multiple Distribution Shifts
published: 2026-08-17T19:36:15Z
authors: Bogdan Oancea
url: http://arxiv.org/abs/2608.17079v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Regime-Aware Conformal Calibration for Reliable Economic Forecast Intervals under Multiple Distribution Shifts

## Abstract
Conformal prediction provides distribution-free prediction intervals but relies on exchangeability, an assumption often violated in economic forecasting because of covariate shift, concept drift, local heterogeneity and latent regimes. We propose Dynamic Regime-Aware Conformal Prediction (DRACP), which combines density-ratio, localized kernel and probabilistic regime-aware weighting with a self-tuning online significance controller in a unified weighted conformal calibration framework. We distinguish three theoretical results: finite-sample validity under oracle importance weights, a coverage-gap bound for estimated weights with rates in effective sample size, and deterministic or regret guarantees for the online controller. We evaluate DRACP against six baselines on 48 real forecasting series covering euro-area and EU-27 HICP inflation, US macroeconomic and energy indicators, and daily financial series. Recent online methods (FACI, strongly-adaptive online conformal prediction and conformal PID) were verified against the authors' implementations. DRACP is not the most efficient method: strongly-adaptive online conformal prediction achieves the best interval score and intervals about 20% narrower. Instead, DRACP provides the most reliable calibration, achieving coverage closest to the nominal 0.90 (0.890), never falling below 0.80 on any series, maintaining the best coverage at all forecast horizons, and performing best during the 2021-2023 inflation surge. The strongly-adaptive method undercovers on 20 of 48 series versus 10 for DRACP. DRACP therefore offers a principled trade-off between calibration and efficiency, favoring reliable coverage when prediction intervals must satisfy coverage standards. An ablation study shows that the online controller and conditional-scale normalization provide most of the performance gain, whereas the weighting components make a smaller contribution.

## Metadata
- **Published**: 2026-08-17T19:36:15Z
- **Authors**: Bogdan Oancea
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17079v1)