---
title: Trust the Mass: Forced Weights in KV-Cache Eviction
published: 2026-08-25T23:40:39Z
authors: Jack Shi, Jerry Gu
url: http://arxiv.org/abs/2608.25230v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trust the Mass: Forced Weights in KV-Cache Eviction

## Abstract
Every deployed sparse-attention or KV-cache-eviction rule keeps a subset of the keys, discards the rest, and renormalizes the attention weights over the kept set. Enumerating the exact best subset under that constraint on $168{,}192$ attention rows from five models shows that keeping the largest weights is already near-optimal, since the best subset closes only a median $2$ to $5\%$ of the remaining gap to full attention. If selection closes this little, published margins between eviction methods must come from elsewhere, so we measure the bytes each method holds. In the shared evaluation pipeline, the strongest query-agnostic methods hold the full cache because their per-head selections are stored as masks, and only ragged per-head storage frees that memory. Enforcing a nominal budget on one fixed selection costs $14$ to $62$ benchmark points. We trace an $87.6$-point retrieval margin to rankings computed while the question is visible. ContourKV, a training-free allocator built from the dropped-mass statistic, wins $93$ of $160$ paired comparisons against that state of the art and loses $22$ at the byte count of the budget-enforcing baselines, and it ties the strongest of them.

## Metadata
- **Published**: 2026-08-25T23:40:39Z
- **Authors**: Jack Shi, Jerry Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25230v1)