---
title: Do Static Embeddings Add Value to Hybrid Dutch Retrieval?
published: 2026-08-03T12:10:51Z
authors: António Pereira Barata
url: http://arxiv.org/abs/2608.02112v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Static Embeddings Add Value to Hybrid Dutch Retrieval?

## Abstract
Embedding benchmarks measure standalone model quality, but they do not establish whether a low-cost retriever contributes complementary ranking information once lexical and transformer-based retrieval are already combined. We present a controlled evaluation of this question across Dutch retrieval tasks from the Massive Text Embedding Benchmark for Dutch (MTEB-NL). Weighted reciprocal rank fusion (RRF) combines Best Matching 25 (BM25), Qwen/Qwen3-Embedding-0.6B (Qwen), and two multilingual static embedding models. Five datasets comprising 14,500 queries and 786,573 documents are scored exhaustively, and fusion weights are searched on a simplex in increments of 0.1. Ten-fold query-level cross-validation selects weights on nine folds and evaluates them on the held-out fold; paired bootstrap confidence intervals and sign-randomisation tests quantify the resulting differences. Fusion improves over the training-selected individual retriever by 0.061 mean reciprocal rank (MRR) on Dutch News, 0.029 on VABB, 0.004 on WebFAQ NL, and 0.025 on Wikipedia NL, while matching BM25 on Open Tender. All four positive differences remain distinguishable from zero after Holm correction. No unrestricted fold assigns positive weight to either static retriever: all 50 selections lie on the BM25-Qwen edge, and forcing a static contribution reduces effectiveness. Leave-one-dataset-out selection chooses equal BM25-Qwen weighting in every iteration and outperforms the cross-domain-selected individual retriever on every held-out task. The results support a two-retriever lexical-transformer architecture as a robust tested default across the evaluated Dutch tasks and show that standalone benchmark performance is insufficient to establish marginal value in hybrid retrieval.

## Metadata
- **Published**: 2026-08-03T12:10:51Z
- **Authors**: António Pereira Barata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02112v1)