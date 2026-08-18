---
title: Cost Scales with Change, Not Corpus Size: Incrementally Maintaining an Evolving Semantic Substrate
published: 2026-08-17T14:21:15Z
authors: Yusuke Takahashi, Kyle Wild, Asako Uraki
url: http://arxiv.org/abs/2608.16621v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cost Scales with Change, Not Corpus Size: Incrementally Maintaining an Evolving Semantic Substrate

## Abstract
Retrieval-augmented and agentic question-answering systems increasingly re-derive the meaning of a corpus at query time. Put plainly, instead of re-deriving what a corpus means on every question, the work is done once when a document arrives and is thereafter merely consulted -- a compiler, not an interpreter, of meaning. An alternative is to compile that meaning once, at ingest time, into a compact, queryable semantic substrate and maintain it as the corpus evolves. The central objection is maintenance cost: rebuilding a truncated singular value decomposition (SVD) on every change appears prohibitive, and a change of embedding model seems to force a full re-embedding. We argue and show empirically that maintenance cost scales with the amount of change, not corpus size. On a controlled synthetic pilot (dimension 256, rank 32, a corpus grown from 3,000 to 9,000 documents over 50 update events), incremental low-rank updates were 33.7 times cheaper per update than full re-SVD and 23.8 times cheaper cumulatively, while the incremental subspace tracked the full recomputation to within floating-point precision (maximum principal-angle drift below 1e-11 degrees; recall@10 = 1.0). An orthogonal Procrustes virtual axis update recovered 0.95 mean cosine to truly re-embedded vectors by re-embedding only about 10 percent of the corpus. The results support maintaining, rather than repeatedly reconstructing, a semantic substrate.

## Metadata
- **Published**: 2026-08-17T14:21:15Z
- **Authors**: Yusuke Takahashi, Kyle Wild, Asako Uraki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16621v1)