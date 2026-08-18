---
title: Cost Scales with Change, Not Corpus Size: Incrementally Maintaining an Evolving Semantic Substrate
url: http://arxiv.org/abs/2608.16621v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_14-21-15Z_CostScaleswithChange_NotCorpusSize_IncrementallyMa.md
generated_at: 2026-08-17 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how to efficiently maintain a semantic substrate for retrieval-augmented QA systems as the corpus changes. It demonstrates that incremental updates are far cheaper than recomputing full singular value decompositions, showing that maintenance cost scales with change rather than corpus size. Experiments on synthetic data show low-rank incremental SVD is 33.7 times cheaper per update and cumulative savings of 23.8 times over a 50‑event growth.

## Key Takeaways
- Incremental low‑rank updates to an SVD are 33.7 times cheaper per update than recomputing the full decomposition, indicating that maintenance cost depends on the amount of change not total corpus size.
- The incremental subspace matches the true recomputed subspace within floating‑point precision, with maximum principal‑angle drift below 1e‑11 degrees and recall@10 equal to 1.0.
- An orthogonal Procrustes virtual axis update can recover most cosine similarity by re‑embedding only about 10 percent of the corpus, reducing computational load dramatically.

## Context
Current AI systems that rely on retrieval‑augmented QA often rebuild semantic representations from scratch each time a document is added or an embedding model changes. This leads to high latency and resource consumption as full SVD recomputations are required, limiting scalability in dynamic environments where frequent updates occur.

## Implications
Maintaining a compact semantic substrate can enable real‑time query answering with minimal overhead, supporting large‑scale deployment of evolving knowledge bases. Practitioners should adopt incremental update strategies to keep systems responsive and cost‑effective as data grows continuously.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16621v1)
