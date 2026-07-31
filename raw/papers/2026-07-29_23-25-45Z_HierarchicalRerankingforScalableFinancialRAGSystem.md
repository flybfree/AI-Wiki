---
title: Hierarchical Reranking for Scalable Financial RAG System
published: 2026-07-29T23:25:45Z
authors: Joohyun Lee, Sungwoo Hong
url: http://arxiv.org/abs/2607.27523v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Reranking for Scalable Financial RAG System

## Abstract
Analyzing financial documents such as 10-K filings, tabular disclosures, and macroeconomic reports demands expert reasoning and extensive time. However, existing Retrieval-Augmented Generation systems often struggle to process hybrid text-table structures or the massive scale of financial documents. To address these challenges, we propose Hierarchical Reranker, a RAG framework designed to improve retrieval performance and generative reliability across large-scale financial datasets. The system integrates three key innovations: Pre-Retrieval Optimization, enhancing query clarity and search efficiency through normalization, keyword expansion, and table transformation; Hierarchical Reranker Architecture, improving retrieval precision through a two-stage ranking mechanism; and Long-Context Management, preserving reasoning accuracy through adaptive input partitioning and fusion under extensive contexts. Across multiple benchmarks, including FinQA, FinanceBench, and ConvFinQA, the proposed system achieved an NDCG@20 score of 0.7918 and demonstrated superior factual consistency. Its robustness was further validated by achieving second place in the ACM-ICAIF '24 FinanceRAG Challenge. This work presents a deployable, domain-optimized RAG pipeline that enhances both the accuracy and scalability of financial reasoning, paving the way for automated audit reporting and quantitative investment analysis. The source code will be made publicly available on GitHub upon acceptance.

## Metadata
- **Published**: 2026-07-29T23:25:45Z
- **Authors**: Joohyun Lee, Sungwoo Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27523v1)