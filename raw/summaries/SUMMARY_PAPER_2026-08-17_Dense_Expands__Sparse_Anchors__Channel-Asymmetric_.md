---
title: Dense Expands, Sparse Anchors: Channel-Asymmetric Query Expansion for Hybrid Retrieval
url: http://arxiv.org/abs/2608.15851v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_16-43-49Z_DenseExpands_SparseAnchors_Channel_AsymmetricQuery.md
generated_at: 2026-08-17 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the limitations of hybrid retrieval systems where dense and sparse rankings are fused using a fixed top‑L cutoff, causing gains to be unstable across different $L$ values. It proposes DESA (Dense Expansion and Sparse Anchoring), which treats channel contributions asymmetrically: an LLM generates orthogonal reference passages for dense expansion while score‑product anchoring injects lexical cues into sparse retrieval without expanding the original query’s vocabulary. Across seven BEIR datasets, DESA raises nDCG@10 by 3.82% and Recall@20 by 2.38%, while reducing average access depths in both channels by about 36%.

## Key Takeaways
- The fixed top‑L fusion can cause retrieval gains to reverse when $L$ changes, highlighting the need for channel‑specific evaluation.
- DESA separates dense and sparse contributions: LLM passages are added only to the dense side, preserving lexical integrity of the original query in sparse search.
- On average, both dense and sparse access depths drop by ~36%, indicating that DESA achieves strong ranking improvements with fewer retrieved documents.

## Context
Hybrid retrieval aims to combine the strengths of dense semantic expansion and sparse lexical matching, yet most systems rely on a single fused cutoff that blurs channel responsibilities. This paper introduces a method that explicitly separates these roles, offering a more nuanced view of how generated passages affect each component.

## Implications
Practitioners can adopt DESA to improve retrieval performance without sacrificing query simplicity or increasing computational load. The channel‑specific approach provides insights for designing future hybrid models where dense and sparse pathways are optimized independently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15851v1)
