---
title: SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers
published: 2026-09-01T14:52:57Z
authors: Shaowen Wang, Ge Zhang, Kairong Luo, Yuhao Wu, Shaofan Liu, Jiaheng Liu, Wenhao Huang, Shen Yan, Jian Li
url: http://arxiv.org/abs/2609.01343v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers

## Abstract
Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs. We study looping on Mixture-of-Experts Transformers while closely matching per-token FLOPs, total non-embedding parameters, and KV cache. Through a series of ablations, we arrive at a recipe we call SMELT (Sparse MoE Transformer, middle layers Loop Twice), which loops the middle half of layers twice while matching the unlooped Baseline on all three budgets. We scale SMELT across four sizes up to 54B non-embedding parameters and fit a separate Chinchilla-style scaling law for each architecture. SMELT's loss drops faster with compute, saving 6.8--18.0\% of training FLOPs on the compute-optimal frontier. The advantage transfers to downstream benchmarks beyond what validation loss predicts, is largest on Code, and grows with sample length and the number of in-context examples. Mechanistic analysis shows that the second visit reduces the attention sink and redirects mass toward content-relevant tokens, an inductive bias that may underlie the observed performance gains. These results show that looping can improve Transformers even under budget matching, offering a practical recipe that turns depth reuse into measurable gains.

## Metadata
- **Published**: 2026-09-01T14:52:57Z
- **Authors**: Shaowen Wang, Ge Zhang, Kairong Luo, Yuhao Wu, Shaofan Liu, Jiaheng Liu, Wenhao Huang, Shen Yan, Jian Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01343v1)