---
title: SAKI: Score-Aware Low-Rank Key Indexing for Long-Context KV Retrieval
url: http://arxiv.org/abs/2608.03228v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_06-59-29Z_SAKI_Score_AwareLow_RankKeyIndexingforLong_Context.md
generated_at: 2026-08-05 01:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SAKI, a training-free low-rank key indexing method that directly preserves attention scores instead of compressing keys or weights. It shows that rank‑r compression distorts scores and derives a covariance‑weighted objective to minimize this distortion. The optimal rank solution is obtained from the SVD of the covariance weighted query key operator.

## Key Takeaways
- SAKI replaces key PCA with an objective that minimizes expected attention score distortion, leading to better recall than PCA at every tested rank.
- At rank 32 SAKI cuts PCA’s top‑64 recall error by 13–30 percent and improves model scores such as LLaMA 3.1 8B from 0.748 to 0.799 and Qwen 2.5 7B from 0.786 to 0.850.
- The method preserves attention scores across all models, achieving gains of 68–89 percent in per‑head score accuracy, especially in deeper layers.

## Context
Low-rank key compression is a common technique for reducing KV cache size but often sacrifices the quality of attention scores used during inference. Existing approaches either compress keys or weights, which do not directly reflect the learned scores and can degrade performance on long contexts.

## Implications
SAKI demonstrates that optimizing the score objective itself yields superior results without retraining, offering a practical path to longer context handling for large language models. Practitioners can adopt SAKI to improve recall and efficiency on inference‑critical applications such as chatbots and retrieval systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03228v1)
