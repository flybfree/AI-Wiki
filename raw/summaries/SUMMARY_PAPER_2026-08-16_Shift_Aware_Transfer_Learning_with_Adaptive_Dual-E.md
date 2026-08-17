---
title: Shift Aware Transfer Learning with Adaptive Dual-Encoder Fusion for PM Forecasting in Data-Limited Environments
url: http://arxiv.org/abs/2608.14456v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_16-41-16Z_ShiftAwareTransferLearningwithAdaptiveDual_Encoder.md
generated_at: 2026-08-16 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a shift-aware dual-encoder transfer learning framework for short‑horizon PM2.5 forecasting when source data are limited and domain distributions differ. The framework combines a pretrained source encoder with a target‑specific branch, avoiding negative transfer while preserving temporal dynamics. Experiments on Taiwan hourly data show that allowing the source encoder to adapt yields the lowest MSE (21.66) compared with frozen models.

## Key Takeaways
- The frozen-source dual‑encoder model achieved an MSE of 21.8960, MAE of 3.1597 and R² of 0.8725, outperforming four baselines by up to 7.1% in MSE reduction.
- Ablation results indicate that removing the Taiwan‑specific branch causes the largest performance drop, highlighting the importance of domain adaptation.
- SHAP analysis reveals predictions rely heavily on recent PM2.5 observations and meteorological variables influencing pollutant transport.

## Context
Transfer learning for environmental forecasting is challenged by limited target data and domain shift, making robust representation learning essential. This work contributes a practical dual‑encoder method that can be applied to other time‑series tasks with sparse supervision.

## Implications
The approach offers practitioners a way to improve forecast accuracy without collecting large amounts of new data. By preserving source knowledge while allowing adaptation, it reduces computational cost and enhances reliability in real‑time air quality monitoring systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14456v1)
