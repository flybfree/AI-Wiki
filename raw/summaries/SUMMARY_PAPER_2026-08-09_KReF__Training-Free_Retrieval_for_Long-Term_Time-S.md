---
title: KReF: Training-Free Retrieval for Long-Term Time-Series Forecasting and Predictive Uncertainty
url: http://arxiv.org/abs/2608.06748v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_03-16-25Z_KReF_Training_FreeRetrievalforLong_TermTime_Series.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KReF, a training-free retrieval method for long-term time-series forecasting that uses historical lookback-future pairs as an empirical predictive distribution. It achieves lower CRPS and IS90 than trained baselines across multiple benchmarks without gradient fitting.

## Key Takeaways
- KReF treats retrieved historical futures as a querylocal empirical predictive distribution, directly using similarity weights to define predictive masses, quantiles, CRPS, and weighted-mean forecasts.
- The method employs handcrafted statistics or frozen random Fourier features for robust preprocessing of lookback sequences, enabling retrieval without model training.
- Validation-selected expansion and shrinkage rates adapt interval boundaries via a probability-integral-transform map, improving uncertainty estimates.

## Context
Long-term forecasting often requires models that have been trained on data, limiting flexibility and interpretability. Retrieval-based approaches offer an alternative by leveraging past observations as priors, which can be especially useful when training is costly or impossible.

## Implications
This work demonstrates retrieval as a powerful inductive bias for LTSF, potentially reducing reliance on complex model fitting. Practitioners may adopt KReF to obtain more accurate uncertainty estimates and point forecasts with minimal computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06748v1)
