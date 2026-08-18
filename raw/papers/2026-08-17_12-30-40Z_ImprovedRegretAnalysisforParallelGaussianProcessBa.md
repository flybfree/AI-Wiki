---
title: Improved Regret Analysis for Parallel Gaussian Process Bandit Optimization
published: 2026-08-17T12:30:40Z
authors: Shion Takeno, Shogo Iwazaki
url: http://arxiv.org/abs/2608.16492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improved Regret Analysis for Parallel Gaussian Process Bandit Optimization

## Abstract
This paper studies the regret analysis for parallel Gaussian process (GP) bandit optimization. The known regret upper bounds for the widely used GP batched upper confidence bound and GP batched Thompson sampling (GP-BTS) suffer from a multiplicative factor with respect to the batch size $Q$. To avoid this degradation, existing analyses require a polynomial number of uncertainty sampling (US) for $Q$ at the beginning of optimization. However, this initial US phase is often ineffective in practice. This paper shows that the regret upper bound without the multiplicative factor on $Q$ can be achieved without the initial US phase, using GP-BTS as an example. Furthermore, we show much better regret upper bounds in the noiseless setting than in the noisy setting, as in the sequential GP bandit setting.

## Metadata
- **Published**: 2026-08-17T12:30:40Z
- **Authors**: Shion Takeno, Shogo Iwazaki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16492v1)