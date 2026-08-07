---
title: SAKI: Score-Aware Low-Rank Key Indexing with Random-Matrix Noise Correction for KV Retrieval
published: 2026-08-04T06:59:29Z
authors: Lin Zhang
url: http://arxiv.org/abs/2608.03228v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAKI: Score-Aware Low-Rank Key Indexing with Random-Matrix Noise Correction for KV Retrieval

## Abstract
Existing low rank KV cache methods preserve either model weights or key variance, neither of which directly reflects the attention scores used during inference. We derive the expected attention score distortion caused by rank r key compression and show that it yields a covariance weighted low rank objective. Under a margin condition, controlling this distortion also improves top k recall. The optimal rank r solution has a closed form asymmetric factorization obtained from the SVD of the covariance weighted query key operator. This motivates SAKI, a training free KV cache index that directly preserves attention scores rather than key reconstruction quality.   Across LLaMA 3.1 8B, Qwen 2.5 7B, Mistral 7B v0.1, and Llama 3.2 3B, SAKI outperforms key PCA at every tested rank. At rank 32, it removes 13 to 30 percent of PCA's remaining top 64 recall error, including improvements from 0.748 to 0.799 on LLaMA 3.1 8B and from 0.786 to 0.850 on Qwen 2.5 7B. It improves 68 to 89 percent of attention heads per model, with the largest gains in deeper layers. Predicted score MSE reductions closely match empirical measurements, with a Pearson correlation of 0.997, while ablation studies confirm that the gains arise from optimizing the attention score objective rather than covariance weighting alone. Analysis of the scoring operator further explains why weight only, invariant subspace, and key reconstruction methods can be suboptimal. SAKI uses random-matrix theory to separate genuine covariance signal from autocorrelated sampling noise, matching PCA with only 512 calibration tokens and adding value exactly where PCA sees no reliable signal.

## Metadata
- **Published**: 2026-08-04T06:59:29Z
- **Authors**: Lin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03228v2)