---
title: Extreme Volatility Warning under Label Scarcity via Multi-Source Anomaly Fusion
published: 2026-07-26T14:30:58Z
authors: Jin Qian, Zhangzhi Xiong, Mingrui Li, Zhen Liu
url: http://arxiv.org/abs/2607.23682v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Extreme Volatility Warning under Label Scarcity via Multi-Source Anomaly Fusion

## Abstract
Early warning of extreme market volatility is central to financial risk management, but actionable events are rare, nonstationary, and often triggered by exogenous information shocks. In our CSI~300 setting, only $\sim$80 positive samples are observed across 791 training days, making heavily supervised multi-source models unstable. We first analyze a 100K-parameter hierarchical text-signal fusion model (HTSF) and find that added parameterization hurts in this low-label regime. Motivated by this failure, we propose \textbf{AAMSF} (Anomaly-Augmented Multi-Signal Fusion), a semisupervised framework that combines Isolation Forest anomaly scores over market indicators, GDELT events, Chinese financial news, and English media with lightweight Ridge score fusion. We further introduce \textbf{T-AAMSF}, a temporal extension for multi-day anomaly accumulation. On CSI~300 (2018--2023), AAMSF achieves test AUC-ROC \textbf{0.680}, outperforming the strongest unsupervised baseline (0.630) and neural baseline (0.588), while T-AAMSF improves PR-AUC to 0.291. Ablations reveal strong source asymmetry: GDELT and domestic financial news provide complementary risk signals, whereas English media consistently reduces performance, and learned weighting is unreliable under validation noise. These results suggest an empirical design principle for label-scarce financial risk warning: robust anomaly geometry and source reliability can matter more than supervised representation capacity.

## Metadata
- **Published**: 2026-07-26T14:30:58Z
- **Authors**: Jin Qian, Zhangzhi Xiong, Mingrui Li, Zhen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23682v1)