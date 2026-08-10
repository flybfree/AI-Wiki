---
title: KReF: Training-Free Retrieval for Long-Term Time-Series Forecasting and Predictive Uncertainty
published: 2026-08-07T03:16:25Z
authors: Yang Zhang, Rui Su
url: http://arxiv.org/abs/2608.06748v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KReF: Training-Free Retrieval for Long-Term Time-Series Forecasting and Predictive Uncertainty

## Abstract
Probabilistic long-term time-series forecasting commonly relies on trained models. Training-free conformal methods typically construct intervals around a pre-existing point forecaster and do not natively represent a complete predictive distribution; sequential variants additionally suffer from increasingly delayed feedback at long horizons. We propose KReF, a training-free retrieval framework that treats retrieved historical futures as a querylocal empirical predictive distribution. After robust preprocessing, KReF embeds each lookback using handcrafted statistics or frozen random Fourier features and retrieves similar historical lookback-future pairs. Their similarity weights directly define predictive masses, quantiles, CRPS, and a weighted-mean point forecast. KReF further uses the observed query lookback to construct a probability-integral-transform map and applies validation-selected expansion and shrinkage rates to adapt interval boundaries. Across six LTSF benchmarks and four horizons, KReF obtains the lowest CRPS in all 12 dataset-embedding settings and the lowest IS90 in 9 settings. Without gradient-based fitting, its point forecasts also match or surpass trained baselines on two of six datasets. An archive-oracle analysis further reveals substantial headroom under finer horizon- and channel-wise routing. These results establish retrieval as a useful and underexplored inductive bias for LTSF.

## Metadata
- **Published**: 2026-08-07T03:16:25Z
- **Authors**: Yang Zhang, Rui Su
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06748v1)