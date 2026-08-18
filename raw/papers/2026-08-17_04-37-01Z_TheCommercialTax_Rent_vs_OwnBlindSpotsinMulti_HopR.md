---
title: The Commercial Tax: Rent-vs-Own Blind Spots in Multi-Hop Retrieval Benchmarks
published: 2026-08-17T04:37:01Z
authors: Luis M. Sanchez, Kosrow Dehnad
url: http://arxiv.org/abs/2608.16096v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Commercial Tax: Rent-vs-Own Blind Spots in Multi-Hop Retrieval Benchmarks

## Abstract
Enterprises connect language models to their own data through retrieval. The benchmarks that rank multi-hop retrieval systems leave out two facts a buyer needs before a published number can be used: whether the retrieval backbone may be deployed commercially, and what it costs to build. On licensing: the field's dense-retrieval anchor, NV-Embed-v2, is licensed cc-by-nc-4.0. Of the four leading MuSiQue systems we audit (HippoRAG-2, PropRAG, SAG, KET-RAG), three depend on it for their best numbers and none says so. On performance: we measure thirteen embedders from eight makers on one identical MuSiQue harness with bootstrap confidence intervals throughout. Until mid-2026 there was a real commercial tax: the best commercially-licensed embedder trailed the anchor by 2.31 Recall@5 points (95% CI [0.91, 3.71], p=0.001). NVIDIA's Nemotron-3-Embed-8B, released 2026-07-16, has closed it: +0.24 at Recall@5 (95% CI [-0.94, +1.43], p=0.69), -0.58 at Recall@10 (p=0.28). It matches the anchor, does not beat it, and is the only entrant that is commercially licensed, free to self-host, and indistinguishable from the anchor; every other entrant meeting the first two conditions sits 5.2 to 14.6 points below. The durable finding is the paid-versus-free divide: API embedders charge per token on every re-index, self-hosted ones charge nothing. On cost: three of five audited systems (adding Microsoft's GraphRAG) do not disclose indexing cost, and the only published GraphRAG dollar figures span 11x inside one third-party paper (USD 2.30 vs USD 24.94 to index a 5.64 MB corpus once); extrapolated to 1 TB that undisclosed choice separates roughly USD 428K from $4.6M. Our cost model keeps one-time embedding apart from recurring answering: at 1 TB, embedding sits 7.5x-900x below graph construction, and a year of answering at 10,000 queries/day sits 350x or more below it.

## Metadata
- **Published**: 2026-08-17T04:37:01Z
- **Authors**: Luis M. Sanchez, Kosrow Dehnad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16096v1)