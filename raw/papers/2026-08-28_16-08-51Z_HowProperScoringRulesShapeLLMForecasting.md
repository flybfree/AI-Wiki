---
title: How Proper Scoring Rules Shape LLM Forecasting
published: 2026-08-28T16:08:51Z
authors: Benjamin Turtel, Paul Wilczewski, Kris Skotheim, Ville A. Satopää, Philip E. Tetlock
url: http://arxiv.org/abs/2608.28482v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Proper Scoring Rules Shape LLM Forecasting

## Abstract
This paper evaluates how reward function choice shapes the performance and behavior of LLM forecasters. We compare five proper scoring rules as training objectives for binary forecasts of resolved real-world events. Although the rules share the same theoretical incentive for truthful probability reporting, the resulting models differ in calibration, probability use, and estimated profiles of bias, information, and noise, with smaller differences in aggregate accuracy and discrimination. The Brier-trained model has the lowest observed Brier score and highest AUC-ROC, while the log-trained model has the highest observed log score and lowest calibration error. Models with similar aggregate performance also reach that performance through different combinations of bias, information, and noise. Proper scoring rules therefore need not behave interchangeably as training objectives. Reward choice may shape not only how well an LLM forecasts, but how its forecasting errors are structured. Each condition uses a single seed, so some differences may reflect training stochasticity.

## Metadata
- **Published**: 2026-08-28T16:08:51Z
- **Authors**: Benjamin Turtel, Paul Wilczewski, Kris Skotheim, Ville A. Satopää, Philip E. Tetlock
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28482v1)