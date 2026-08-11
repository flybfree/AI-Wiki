---
title: KGCache: Amortized Subgraph Retrieval for KG Reasoning with LLMs
published: 2026-08-08T06:36:24Z
authors: Uros Stanic, Changcheng Yuan, Sabuj Laskar, Ariful Azad
url: http://arxiv.org/abs/2608.07954v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KGCache: Amortized Subgraph Retrieval for KG Reasoning with LLMs

## Abstract
Large language models can answer knowledge-intensive questions more reliably when they are grounded with knowledge graphs, but systems such as Think-on-Graph and Reasoning-on-Graph repeatedly query the same graph neighborhoods across different questions. In this work, we study this repeated retrieval in Knowledge Graph Question Answering~(KGQA) workloads and propose KGCache, an in-memory cache for one-hop knowledge graph neighborhoods. KGCache is designed to be compatible with both iterative traversal (ToG) and one shot planning (RoG) KGQA paradigms. KGCache is placed between the KGQA engine and the backend serving the KG, so repeated entity requests can be served from cache instead of issuing new KG queries. We evaluate KGCache on WebQSP and CWQ using LRU, LFU, and a trace-aware Oracle policy. Our analysis shows that both datasets contain substantial entity reuse among starting entities and entities reached during traversal. We also explore semantic caching for similar queries, which shows additional hit-rate gains on WebQSP and needs further accuracy testing on CWQ. Entity caching accelerates KG retrieval by up to $1.91\times$, while semantic-context caching achieves up to $1.06\times$ full-system speedup in the evaluated WebQSP configurations, with each hit being up to $3.73\times$ faster.

## Metadata
- **Published**: 2026-08-08T06:36:24Z
- **Authors**: Uros Stanic, Changcheng Yuan, Sabuj Laskar, Ariful Azad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07954v1)