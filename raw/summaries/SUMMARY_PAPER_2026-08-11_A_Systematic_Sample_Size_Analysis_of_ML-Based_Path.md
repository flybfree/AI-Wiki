---
title: A Systematic Sample Size Analysis of ML-Based Path Loss Prediction for LPWAN
url: http://arxiv.org/abs/2608.11083v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-48-54Z_ASystematicSampleSizeAnalysisofML_BasedPathLossPre.md
generated_at: 2026-08-11 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper aims to evaluate how machine learning models improve path loss prediction for LoRaWAN networks as the training set size grows, using real urban measurements. It compares a Random Forest and k-Nearest Neighbors model against traditional empirical and LPWAN-specific baselines across various split sizes.

## Key Takeaways
- The Random Forest achieves RMSE below 6.5 dB at maximum training size, significantly outperforming the best baseline’s 9.7 dB error.
- Leave-one-gateway-out testing shows RF suffers placement‑dependent transfer to held‑out gateways, with moderate errors for some and larger errors for others.
- k-Nearest Neighbors using only coordinates degrades substantially when a gateway location is unseen, highlighting the importance of terrain features.

## Context
This work contributes to AI applications in wireless communications by demonstrating that data‑driven models can surpass conventional propagation formulas even with limited labeled measurements. It underscores the value of incorporating sensor‑derived attributes such as LiDAR terrain for urban LoRa deployments.

## Implications
For network planners, the findings suggest that ML models enable more accurate path loss interpolation and better gap analysis in smart city rollouts. Practitioners should prioritize feature richness over raw data volume to achieve reliable predictions across diverse gateway locations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11083v1)
