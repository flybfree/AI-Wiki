---
title: Static Pruning Across Sparse Retrieval Regimes: What Transfers, What Breaks, and What Still Helps
published: 2026-08-17T09:19:49Z
authors: Zirui Song, Yuye Zhu, Yang Yang
url: http://arxiv.org/abs/2608.16309v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Static Pruning Across Sparse Retrieval Regimes: What Transfers, What Breaks, and What Still Helps

## Abstract
Static pruning is widely used to accelerate sparse neural retrieval, yet existing studies each validate their conclusions within a single custom pipeline, leaving it unclear which findings transfer to modern engines with different index organizations and dynamic pruning mechanisms. We present the first cross-engine pruning portability study, evaluating static pruning strategies across three engines - a controlled C++ pipeline (exhaustive inverted index), BMP (block-max pruning), and SEISMIC (clustered inverted indexes) - on two benchmarks (MS MARCO, Natural Questions) with two encoders spanning opposite query-density regimes (SPLADE: 44 avg. query terms; V3-GTE: 7 avg. query terms), totaling 1,140 experimental configurations, with an additional deep-judgment validation on TREC DL 2019/2020. We find that index-side pruning (document and posting-list) is portable: it consistently reduces latency (1.2-6.6$\times$) and index size (18-82%) across all engines because sparse retrieval is memory-bound - a conclusion we support with cache-miss, TLB, and IPC profiling. In contrast, query pruning is already internalized by modern engines: it yields 4-11$\times$ speedup on the exhaustive pipeline but is subsumed by BMP's $β$ and SEISMIC's query_cut. Static pruning complements dynamic pruning: on BMP, combining document and query reduction yields 2.5$\times$ speedup with NDCG@10 within 0.003 of the exact baseline. Finally, NDCG@10 saturates while Recall@10 is still in the ${\sim}$85-95% range across all three engines, providing a portable stopping criterion: practitioners can push pruning to this knee without visible ranking degradation. Together, these findings answer what transfers (index-side pruning), what breaks (query pruning), and what still helps (static atop dynamic pruning).

## Metadata
- **Published**: 2026-08-17T09:19:49Z
- **Authors**: Zirui Song, Yuye Zhu, Yang Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16309v1)