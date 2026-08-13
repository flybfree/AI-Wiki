---
title: SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges
published: 2026-08-12T14:49:40Z
authors: Yuchao Wu, Junqin Li, XingCheng Liang, Yongjie Chen, Yinghao Liang, Linyuan Mo, Guanxian Li
url: http://arxiv.org/abs/2608.12129v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges

## Abstract
While retrieval-augmented generation (RAG) has proven effective at giving LLMs access to external knowledge, mainstream dense-retrieval implementations remain inherently limited in handling structured constraints and multi-hop reasoning. Graph-based methods address this by constructing knowledge graphs offline, but they often fragment semantics, incur high maintenance, and complicate incremental updates. We propose SAG (SQL-Retrieval Augmented Generation), a structured retrieval architecture that organizes documents into an event-entity index without building a global knowledge graph. SAG represents each chunk as a semantically complete event paired with its entities, forming a latent hyperedge that preserves n-ary relations without decomposing them into triples. At query time, SAG treats shared entities as join keys to connect related chunks. This dynamically yields a query-scoped neighborhood of events, and yet every piece of evidence remains the original chunk throughout. Experiments on HotpotQA, 2WikiMultiHopQA, and MuSiQue show that SAG achieves the best retrieval and end-to-end QA performance on every benchmark, with gains that widen as reasoning-chain complexity increases. On MuSiQue, where multi-hop evidence chaining is most demanding, SAG reaches 80.36% Recall@5, outperforming the strongest baseline by 11.52 points. This work paves the way for knowledge infrastructure that enables LLM agents to retrieve and reason over continually growing organizational knowledge.

## Metadata
- **Published**: 2026-08-12T14:49:40Z
- **Authors**: Yuchao Wu, Junqin Li, XingCheng Liang, Yongjie Chen, Yinghao Liang, Linyuan Mo, Guanxian Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12129v1)