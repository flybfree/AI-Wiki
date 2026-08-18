---
title: PCA-guided Activation Scaling for Monotonic Bidirectional Control over LLM Sycophancy
published: 2026-08-17T14:48:49Z
authors: Zheng Chen, Zhaoxin Feng, Yip Tin Po, Jianfei Ma, Emmanuele Chersoni, Bo Li
url: http://arxiv.org/abs/2608.16650v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PCA-guided Activation Scaling for Monotonic Bidirectional Control over LLM Sycophancy

## Abstract
Large language models (LLMs) exhibit sycophancy, a tendency to agree with user beliefs regardless of factual accuracy. This can reinforce misconceptions, but eliminating it entirely risks over-correction against valid opinions. Effective control must therefore both reduce and increase sycophancy with predictable and gradual effect. Yet, existing methods fail to ensure a bidirectional and monotonic relationship between steering strength and behavioral outcome across models and datasets. We introduce PCA-guided Activation Scaling (PAS), an activation steering framework that decomposes residual stream activations into a PCA-identified sycophancy-honesty subspace and an orthogonal residual, then applies distinct scaling exponents to achieve monotonic, bidirectional control. Across three LLMs and three datasets, PAS achieves strong monotonicity (Spearman $ρ$ = +0.92) and an average shift of 15.4% per direction, compared with 8.7% for the baselines. Ablation studies confirm that the decomposition, asymmetric exponents, and layer selection are each essential for maintaining monotonic control. The data and code are available at https://github.com/Bellafc/PCS.

## Metadata
- **Published**: 2026-08-17T14:48:49Z
- **Authors**: Zheng Chen, Zhaoxin Feng, Yip Tin Po, Jianfei Ma, Emmanuele Chersoni, Bo Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16650v1)