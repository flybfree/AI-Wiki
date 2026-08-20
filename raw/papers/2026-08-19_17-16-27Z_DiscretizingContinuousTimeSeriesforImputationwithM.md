---
title: Discretizing Continuous Time Series for Imputation with Masked Diffusion Training
published: 2026-08-19T17:16:27Z
authors: Dongbin Kim, Seungyun Lee, Geonwoo Shin, Jaewook Lee
url: http://arxiv.org/abs/2608.19119v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Discretizing Continuous Time Series for Imputation with Masked Diffusion Training

## Abstract
Time series imputation is a crucial area for reliable time series analysis, yet it remains challenging due to the complex temporal dynamics and noise of real-world data. Existing approaches, however, exhibit two limitations: missing and observed values are embedded within the same representation space without explicit structural separation, and continuous diffusion-based methods are trained to predict added noise rather than the original signal. To address these, we propose the Masked Diffusion Time-series Imputation Model (MDTIM), which leverages the training paradigm of masked diffusion model for imputation tasks. The MASK token is structurally orthogonal to valid observations, and the model directly predicts the original values, naturally aligning both the representation and the learning objective with the imputation task. To bridge the gap between discrete masked diffusion and the continuous, ordinal nature of time series, we further introduce Stochastic Discretization, which maps continuous values to ordinal-aware tokens while preserving continuous dynamics. Our experiments on diverse benchmarks confirm that MDTIM achieves superior robustness and scalability, consistently outperforming state-of-the-art deterministic and generative baselines across various missing scenarios.

## Metadata
- **Published**: 2026-08-19T17:16:27Z
- **Authors**: Dongbin Kim, Seungyun Lee, Geonwoo Shin, Jaewook Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19119v1)