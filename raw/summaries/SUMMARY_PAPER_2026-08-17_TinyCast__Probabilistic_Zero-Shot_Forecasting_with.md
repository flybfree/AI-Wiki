---
title: TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity
url: http://arxiv.org/abs/2608.15767v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_14-40-44Z_TinyCast_ProbabilisticZero_ShotForecastingwithComp.md
generated_at: 2026-08-17 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
TinyCast is an attention-free zero-shot forecaster that emits a predictive distribution using only computed periodicity information. It combines a spectral detector, phase‑folded context, dilated convolutional encoder and block‑autoregressive quantile decoder to achieve high accuracy while staying within 1.4 million parameters.

## Key Takeaways
- TinyCast defines the size‑accuracy frontier among zero-shot models that emit predictive distributions under 1.4 M parameters.
- It is orders of magnitude smaller than other zero‑shot entries that score better, requiring at least 28 times its parameter count to achieve comparable performance.
- The model exports to static INT8 and runs end‑to‑end on embedded devices without per‑signal fitting.

## Context
This research tackles the need for compact, accurate forecasters in time‑series prediction where periodic patterns dominate. By explicitly computing dominant periods rather than learning them, TinyCast replaces complex attention mechanisms with lightweight convolutions and matrix multiplications, advancing zero‑shot forecasting efficiency.

## Implications
Practitioners can deploy TinyCast on resource‑constrained devices such as IoT sensors or edge AI chips, enabling real‑time probabilistic inference. Its static INT8 deployment reduces memory overhead and supports widespread adoption of time‑series prediction in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15767v1)
