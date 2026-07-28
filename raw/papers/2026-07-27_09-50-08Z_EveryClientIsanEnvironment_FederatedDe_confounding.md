---
title: Every Client Is an Environment: Federated De-confounding for Spatio-Temporal Forecasting
published: 2026-07-27T09:50:08Z
authors: Qingxiang Liu, Anqi Liang, Heng Wang, Yuxuan Liang
url: http://arxiv.org/abs/2607.24218v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Every Client Is an Environment: Federated De-confounding for Spatio-Temporal Forecasting

## Abstract
Federated learning has emerged as a promising paradigm for spatio-temporal forecasting (STF), enabling collaborative model training without sharing raw observations. Existing federated STF methods primarily regard cross-client heterogeneity as an optimization challenge and mitigate it through personalized approaches. However, such heterogeneity fundamentally stems from diverse \emph{environmental conditions}, and these methods capture environment-specific forecasting patterns, hardly generalizing under environmental shifts. Our key insight is that the environmental diversity across federated clients should be exploited, as they provide \emph{complementary observations of the same underlying spatio-temporal system}. Based on this insight, we propose \method, a novel federated de-confounding framework that \textbf{treats clients as distinct causal environments}. \method leverages the client heterogeneity as distributed environmental evidence and learns a global prototype codebook to capture shared environmental regimes. We further derive a theoretical federated de-confounding bound that is linearly controlled by the averaged confounding strength. Extensive experiments demonstrate that \method consistently outperforms federated baselines, while providing transferable, interpretable, and communication-efficient environmental representations.

## Metadata
- **Published**: 2026-07-27T09:50:08Z
- **Authors**: Qingxiang Liu, Anqi Liang, Heng Wang, Yuxuan Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24218v1)