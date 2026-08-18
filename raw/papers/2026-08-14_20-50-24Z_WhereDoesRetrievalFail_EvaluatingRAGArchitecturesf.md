---
title: Where Does Retrieval Fail? Evaluating RAG Architectures for Agricultural Advisory
published: 2026-08-14T20:50:24Z
authors: Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Sumaiya Tabassum Nimi
url: http://arxiv.org/abs/2608.14886v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Does Retrieval Fail? Evaluating RAG Architectures for Agricultural Advisory

## Abstract
Retrieval quality in RAG systems is commonly reported as a single aggregate score, which can hide large differences across query types and language conditions. We study this problem in Bengali agricultural advisory, where farmer queries are often colloquial while official advisory documents use formal scientific terminology. We construct a test collection of 1,000 queries and 2,882 knowledge nodes extracted from 284 official Bangladeshi agricultural publications, and use it to evaluate five retrieval architectures and six embedding models under three controlled language conditions.   The results show that no single retrieval method is consistently best. For native Bengali queries, BM25 is the strongest single retriever (R@10 = 0.506) while Hybrid RRF reaches the highest overall R@10 of 0.539. However, dense retrieval performance varies sharply by query type: R@10 is 0.093 on colloquial farmer queries and 0.970 on formal safety queries. Across language conditions, BM25 R@10 drops from 0.506 on Bengali queries to 0.004 when English queries are matched against the Bengali corpus, while dense retrieval falls only from 0.464 to 0.425. We also find that embedding task configuration and passage length can each change reported R@10 by a factor of seven, independent of architecture. These results show why low-resource RAG evaluation should report performance by language condition and query type rather than relying on aggregate scores alone. The dataset and evaluation scripts are available at https://huggingface.co/datasets/RaiyanKhaan/AgriTrust-RAG.

## Metadata
- **Published**: 2026-08-14T20:50:24Z
- **Authors**: Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Sumaiya Tabassum Nimi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14886v1)