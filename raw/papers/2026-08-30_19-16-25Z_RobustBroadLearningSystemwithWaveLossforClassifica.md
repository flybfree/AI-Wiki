---
title: Robust Broad Learning System with Wave Loss for Classification under Data Uncertainty
published: 2026-08-30T19:16:25Z
authors: Mushir Akhtar, A. Varshney, A. Quadir, A. Rahaman, M. Tanveer, Mohd. Arshad
url: http://arxiv.org/abs/2608.29983v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Broad Learning System with Wave Loss for Classification under Data Uncertainty

## Abstract
Broad Learning System (BLS) offers an efficient alternative to deep architectures by enabling fast learning through randomized feature mapping and closed-form solutions. However, its reliance on squared error loss makes it highly sensitive to noise, outliers, and corrupted labels, limiting its reliability in real-world scenarios. To address this limitation, we propose Wave-BLS, a robust broad learning framework that integrates the wave loss function, which is asymmetric, bounded, and smooth, enabling controlled penalization of large errors. The proposed formulation replaces the standard least-squares objective with a wave-loss-based optimization problem, solved efficiently using a Nesterov accelerated gradient (NAG)-based scheme without requiring matrix inversion, thereby improving scalability. Extensive experiments on 30 UCI benchmark datasets demonstrate that Wave-BLS consistently outperforms classical BLS and several robust variants. Statistical validation using Friedman and Nemenyi post-hoc tests confirms the significance of the observed improvements. Furthermore, robustness evaluations under controlled noise and outlier injection reveal that Wave-BLS exhibits substantially slower performance degradation compared to BLS, even in challenging contamination settings. These results establish Wave-BLS as a stable and robust alternative to existing broad learning models for learning under data uncertainty.

## Metadata
- **Published**: 2026-08-30T19:16:25Z
- **Authors**: Mushir Akhtar, A. Varshney, A. Quadir, A. Rahaman, M. Tanveer, Mohd. Arshad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29983v1)