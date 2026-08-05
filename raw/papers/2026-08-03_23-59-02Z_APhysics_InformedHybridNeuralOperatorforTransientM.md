---
title: A Physics-Informed Hybrid Neural Operator for Transient Magnetization Prediction in Power Magnetics
published: 2026-08-03T23:59:02Z
authors: Yachao Zhu, Qiujie Huang, Sinan Li, Yang Li, Gang Lei, Jianguo Zhu
url: http://arxiv.org/abs/2608.02965v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Physics-Informed Hybrid Neural Operator for Transient Magnetization Prediction in Power Magnetics

## Abstract
Magnetic components in high-frequency, high-power-density converters are increasingly driven by non-sinusoidal flux-density waveforms with fast transitions, minor-loop operation, dc bias, and temperature variation. Under these conditions, steady-state core-loss formulas and single-valued material curves cannot fully capture transient magnetization responses. This work proposes the Physics-Informed Hybrid Neural Operator (PI-HNO), a compact material-specific neural model with B-H energy-consistency regularization for core-loss-oriented transient magnetization prediction. Given the measured B(t)-H(t) history, the input B(t) series over the prediction interval and operating-condition information, PI-HNO predicts the H(t) series and the corresponding reconstructed B-H trajectory. The model integrates a local recurrent branch for boundary-state representation and rate-dependent response evolution with a Preisach-inspired global branch that extracts waveform-level hysteresis context. Evaluation on the MagNetX transient database using material-specific models for 14 ferrite materials demonstrates that PI-HNO achieves a compact trade-off between sequence accuracy and B(t)-H(t) energy consistency, with the mean and 95th percentile B(t)-H(t) energy consistency errors of 1.92% and 7.60%, respectively, using only 4777 trainable parameters per model. Ablation studies further demonstrate that the local, global, and energy-aware regularized components provide distinct contributions to transient magnetization prediction.

## Metadata
- **Published**: 2026-08-03T23:59:02Z
- **Authors**: Yachao Zhu, Qiujie Huang, Sinan Li, Yang Li, Gang Lei, Jianguo Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02965v1)