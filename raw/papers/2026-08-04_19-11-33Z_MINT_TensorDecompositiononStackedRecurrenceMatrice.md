---
title: MINT: Tensor Decomposition on Stacked Recurrence Matrices for Time Series Data Mining
published: 2026-08-04T19:11:33Z
authors: Kaamil Kaka, Audrey Der, Evangelos E. Papalexakis, Zachary Zimmerman, Vikram Jayaram
url: http://arxiv.org/abs/2608.04157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MINT: Tensor Decomposition on Stacked Recurrence Matrices for Time Series Data Mining

## Abstract
Recurrence plots are a time series data mining primitive applied to a variety of domains (e.g. star light curves, sound waveforms, CCT telemetry). This work proposes tensorized self-similarity matrices as a primitive for univariate time series datasets ($N\times n$) of $N$ time series of length $n$ with a subsequence window of length $m$, and whose tensor-based nature is naturally extensible to multivariate datasets. The proposed method to compute this primitive computes dot plots of size $N \times (n-m+1) \times (n-m+ 1)$ from these datasets, where the subsequent tensor is mined using tensor decomposition methods to mine for co-clustered patterns. We demonstrate our results in mass rapid transit, electricity demand, wind turbine, and car traffic data, finding the MINT pipeline effectively co-clusters cross-sensor patterns in highly regular datasets containing motifs at regular intervals.

## Metadata
- **Published**: 2026-08-04T19:11:33Z
- **Authors**: Kaamil Kaka, Audrey Der, Evangelos E. Papalexakis, Zachary Zimmerman, Vikram Jayaram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04157v1)