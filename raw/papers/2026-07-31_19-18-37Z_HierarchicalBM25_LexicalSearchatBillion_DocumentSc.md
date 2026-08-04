---
title: Hierarchical BM25: Lexical Search at Billion-Document Scale
published: 2026-07-31T19:18:37Z
authors: Umesh Deshpande, Swaminathan Sundararaman
url: http://arxiv.org/abs/2608.00229v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical BM25: Lexical Search at Billion-Document Scale

## Abstract
A flat BM25 index over one billion documents occupies about 400 GB. Holding it in memory requires DRAM proportional to corpus size. Serving it from disk takes 4-12 seconds per query. Exact top-k lexical retrieval at this scale is therefore impractical within an interactive latency budget.   Hierarchical BM25 gives up exact ranking in exchange for fixed bounds on memory and latency. A resident coarse index selects which of ~1K topical, size-balanced document groups a query visits, using two signals: the total frequency of each query term within a group, and, for informative terms spread too thinly across groups for frequency totals to reflect, whether several of them appear together in one document. Selected groups are then searched exhaustively and scored against ~100 KB of global statistics. Every returned score therefore equals the flat index's score, and the approximation is confined to selection alone. The resident footprint is ~4.4 GB, independent of corpus size. Sixteen-term queries over one billion documents return in ~300 ms (4.7x to 5.6x the throughput of a flat multi-threaded index), and a warmed cache sustains ~32 queries per second versus under 3 for flat indexing. At a 500K-document configuration, visiting 5-10% of clusters recovers 0.83-0.92 of the exhaustive result score. Billion-scale recall and a direct comparison against document-reordered BlockMax-WAND remain open.

## Metadata
- **Published**: 2026-07-31T19:18:37Z
- **Authors**: Umesh Deshpande, Swaminathan Sundararaman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00229v1)