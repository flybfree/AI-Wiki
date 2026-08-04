---
title: DSETA: A Dual-Stage Continual Learning Framework for Travel Time Prediction in Dynamic Traffic Environments
published: 2026-08-01T02:55:14Z
authors: Yanming Lyu, Yue Cheng, Lingkun Li, Ruipeng Gao, Xinyue Liu, Hui Gao, Qiang Ni
url: http://arxiv.org/abs/2608.00402v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DSETA: A Dual-Stage Continual Learning Framework for Travel Time Prediction in Dynamic Traffic Environments

## Abstract
Estimated Time of Arrival (ETA) prediction is a core component of intelligent transportation systems. As traffic congestion patterns become increasingly dynamic in large cities, maintaining high prediction accuracy poses a major challenge for ride-hailing platforms. Existing methods either fail to adapt to irregular traffic patterns and sudden congestion, or suffer from new distributions without disentangling long-term trends from short-term fluctuations, thereby degrading model performance in real-world scenarios. To address this challenge, we propose DSETA, an incrementally updated Dual-Stage ETA prediction framework. Specifically, the continual learning process is divided into \textit{inter-day} and \textit{intra-day} stages. We first design the \textit{intra-day} learning stage, which relies entirely on real-time data to enable dynamic adaptation to short-term traffic patterns caused by events like holidays or accidents. Next, we develop the \textit{inter-day} learning stage, which leverages aggregated historical data from a short time window to capture knowledge of long-term distribution shifts, such as seasonal trends and traffic network evolution. Subsequently, to prevent catastrophic forgetting and preserve knowledge of regular patterns, we explore a \textit{Historical Traffic Knowledge Consolidation} module. Finally, we validate DSETA's effectiveness and robustness through extensive offline and online experiments conducted on real-world datasets from DiDi's platform. Online A/B tests across three major cities including Beijing, Wuhan, and Xi'an consistently demonstrated performance gains, achieving MAE reductions of 6.62\%, 0.73\%, and 2.40\% respectively. This framework has been successfully deployed in DiDi's production environment, processing hundreds of millions of daily requests and validating its strong performance in industrial applications.

## Metadata
- **Published**: 2026-08-01T02:55:14Z
- **Authors**: Yanming Lyu, Yue Cheng, Lingkun Li, Ruipeng Gao, Xinyue Liu, Hui Gao, Qiang Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00402v1)