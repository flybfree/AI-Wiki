---
title: Sparse Mutual Information Graph Averaging for Improving Random Indexing Embeddings
url: http://arxiv.org/abs/2608.05724v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_08-07-18Z_SparseMutualInformationGraphAveragingforImprovingR.md
generated_at: 2026-08-06 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a sparse Positive Pointwise Mutual Information (PPMI) graph averaging technique to repair weak Random Indexing embeddings for semantic analogy tasks. On the fairytales dataset it raises accuracy from 19.4 ± 0.7 % to 30.7 ± 2.9 %, demonstrating a notable improvement despite not matching neural baselines.

## Key Takeaways
- The method repairs weak Random Indexing initialization by averaging PPMI graph top‑K, boosting analogy accuracy on the fairytales dataset.
- It achieves near‑zero strict similarity correlation on SimLex‑999, indicating limited semantic alignment beyond the task.
- Neural baselines outperform it on text8 and other tasks, showing that non‑gradient repair remains suboptimal.

## Context
Sparse word embedding pipelines aim to avoid dense co‑occurrence matrices while still leveraging global corpus statistics. Random Indexing provides a fast initialization but often yields poor semantic quality; this work explores a simple graph averaging approach as a lightweight alternative.

## Implications
The technique offers a low‑cost repair strategy for sparse embeddings, useful in resource‑constrained settings where training is impractical. Practitioners may adopt PPMI top‑K averaging to improve baseline performance without the overhead of full neural models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05724v1)
