---
title: Beyond the QBER Threshold: A Temporal QBER Based Machine Learning Framework for Multi Attack Detection in BB84 QKD
url: http://arxiv.org/abs/2608.04047v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_08-04-16Z_BeyondtheQBERThreshold_ATemporalQBERBasedMachineLe.md
generated_at: 2026-08-05 23:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a temporal QBER based machine learning framework for detecting multi‑attack eavesdropping in BB84 QKD, outperforming the conventional 11% threshold. XGBoost achieves high accuracy while SVM‑RBF is comparable, and SHAP explains feature importance.

## Key Takeaways
- The framework uses 63 physics‑informed temporal features to capture burst behavior and channel instability beyond average QBER.
- It reduces false negative rate from 0.8477 at the fixed threshold to 0.0198, enabling detection of stealthy attacks that stay below 11% QBER.
- XGBoost reaches 88.01% accuracy (0.47%) and macro F1 0.8803, showing robust performance across seven attack types.

## Context
This work extends AI‑driven security monitoring in quantum key distribution by integrating domain physics into feature engineering, moving beyond simple statistical thresholds. It demonstrates how machine learning can interpret temporal dynamics of QBER to improve detection reliability. Such integration could lower operational costs by automating decision making.

## Implications
Practitioners can implement a more sensitive and explainable surveillance system that adapts to varying attack strategies without manual threshold tuning. The approach may inspire similar physics‑aware AI in other quantum communication protocols.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04047v1)
