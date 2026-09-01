---
title: Improving Argument Saliency Coverage in Small LLMs for Long Legal Opinion Summarization via Sequence-Level Distillation
url: http://arxiv.org/abs/2608.29884v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_16-27-09Z_ImprovingArgumentSaliencyCoverageinSmallLLMsforLon.md
generated_at: 2026-08-31 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how sequence-level distillation from a large teacher model can boost argument saliency coverage in summarizing long legal opinions, showing that small LLMs improve significantly. Distillation outperforms tuning on expert summaries and requires only about ten training examples.

## Key Takeaways
- Sequence-level distillation provides annotation-free, data-efficient supervision that yields higher saliency coverage than fine-tuning.
- The method works across various student model sizes, consistently surpassing expert-written summary performance.
- Even a small number of teacher-generated summaries (~10) is enough to achieve most gains.

## Context
Large language models face challenges in retaining key argumentative content when summarizing lengthy legal documents. This work addresses the gap by showing that distillation can compensate for limited data and compute, offering a scalable solution.

## Implications
Practitioners can adopt distillation pipelines without needing large labeled datasets, reducing costs and accelerating deployment of accurate legal summaries. The approach also suggests that reasoning-chain distillation offers modest extra benefit when combined with summary supervision.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29884v1)
