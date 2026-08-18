---
title: DeltaLog: Deferred Materialization of Recurrent States for Linear Attention Decoding
published: 2026-08-16T05:04:11Z
authors: Junqing Lin, Jingwei Sun, Guangzhong Sun
url: http://arxiv.org/abs/2608.15533v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeltaLog: Deferred Materialization of Recurrent States for Linear Attention Decoding

## Abstract
Linear attention models eliminate the quadratic prefix computation and context-growing KV cache of softmax attention by replacing pairwise token interactions with recurrent state updates. However, existing decoding implementations often materialize and write back the full recurrent state after every generated token, making state maintenance a major source of memory traffic, especially for models with large states and many heads. This paper presents DeltaLog, a recurrent-state decoding scheme that reduces this overhead without changing the model semantics. Specifically, DeltaLog represents the recurrent state as a dense base state together with a bounded log of recent compact updates. Most decode steps append only compact update factors to this log, while periodic merge steps fold the accumulated updates back into the dense base state. Thus, the model observes the same dense state as in eager decoding, but most full-state write-backs are replaced by lightweight append operations. We implement DeltaLog for GDN, KDA, and RWKV6 and integrate it into a prototype serving stack. Across these models, DeltaLog accelerates the recurrent-state update kernel by up to $1.86\times$, reduces profiled recurrent-state write traffic by up to $7.83\times$, and achieves $1.05$--$1.20\times$ end-to-end serving speedups over dense recurrent baselines.

## Metadata
- **Published**: 2026-08-16T05:04:11Z
- **Authors**: Junqing Lin, Jingwei Sun, Guangzhong Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15533v1)