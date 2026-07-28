---
title: MAPLE: Efficient and Diverse Multi-Alpha Generation for Portfolio Construction
published: 2026-07-27T08:14:29Z
authors: Yu-Chen Den, Kuan-Yu Chen, Kendro Vincent, Tien-Hao Chang
url: http://arxiv.org/abs/2607.24131v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAPLE: Efficient and Diverse Multi-Alpha Generation for Portfolio Construction

## Abstract
Classical alpha mining achieves strong risk-adjusted returns by combining many low-correlated predictive signals, yet deep learning stock-ranking methods typically produce a single alpha per stock, rely on increasingly complex architectures with diminishing gains, and obtain diversity only through separate models or implicit routing, without explicitly controlling inter-alpha correlation. We introduce MAPLE (Multi-Alpha Position-aware Listwise Ensembling), a backbone-agnostic framework that recovers this diversity principle within a single training pass. MAPLE combines a unified, capacity-scaled prediction head with an extreme-rank weighted listwise ranking loss and a diversity regularizer that explicitly penalizes pairwise correlation across alphas. Across four equity markets spanning the US, China, and Japan, MAPLE achieves the best average Sharpe and Calmar ratios among nine baselines, using up to 55x fewer parameters and 2.5x less training time, and generalizes across five backbone architectures with Sharpe and Calmar Ratio gains of 10-23% and 17-43%, respectively. Behavioral analysis further shows why each component works: the unified head already reduces inter-alpha correlation before any diversity loss is applied, and the extreme-rank loss lets diversity regularization improve rather than erode per-alpha ranking quality as capacity scaling sustains this balance at scale. These results show that principled loss design and capacity allocation, rather than architectural complexity, drive diverse and effective multi-alpha generation.

## Metadata
- **Published**: 2026-07-27T08:14:29Z
- **Authors**: Yu-Chen Den, Kuan-Yu Chen, Kendro Vincent, Tien-Hao Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24131v1)