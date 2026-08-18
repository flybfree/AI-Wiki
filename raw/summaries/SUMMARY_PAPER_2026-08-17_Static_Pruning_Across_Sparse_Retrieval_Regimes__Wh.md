---
title: Static Pruning Across Sparse Retrieval Regimes: What Transfers, What Breaks, and What Still Helps
url: http://arxiv.org/abs/2608.16309v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_09-19-49Z_StaticPruningAcrossSparseRetrievalRegimes_WhatTran.md
generated_at: 2026-08-17 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how static pruning strategies for sparse neural retrieval transfer across different index implementations and query densities. It evaluates document-side and query-side pruning on three engines with two encoders over MS MARCO and Natural Questions, finding that index-side pruning consistently speeds up retrieval while query pruning is already handled internally.

## Key Takeaways
- Index-side pruning reduces latency 1.2‑6.6 times and shrinks index size 18‑82% across all engines because sparse retrieval is memory bound.
- Query pruning yields 4‑11× speedup on the exhaustive pipeline but is already accounted for by BMP’s β and SEISMIC’s query_cut, so it does not add extra benefit.
- Combining document and query reduction on BMP gives a 2.5× speedup with NDCG@10 only slightly below the exact baseline.

## Context
Static pruning aims to cut computational cost in large‑scale retrieval systems where memory and latency dominate performance. Understanding which techniques transfer between hardware or software implementations is crucial for scalable deployment.

## Implications
Practitioners can safely push static pruning up to the NDCG@10 knee without hurting ranking, making it a portable optimization that works across diverse engines. This insight helps industry teams standardize pipeline design and avoid redundant work on query‑side reductions already handled internally.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16309v1)
