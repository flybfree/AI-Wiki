---
title: BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and Agent-Based Answer Generation
published: 2026-09-04T11:10:07Z
authors: André Ribeiro, Rúben Garrido, Alexander Christiansen, Richard A. A. Jonker, Sérgio Matos
url: http://arxiv.org/abs/2609.04999v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and Agent-Based Answer Generation

## Abstract
This paper describes the participation of the BIT.UA team from the University of Aveiro in the 14th edition of the BioASQ Task B challenge on biomedical question answering. Building on our previous submissions, we introduced a substantially refactored and modular codebase, and made significant changes to both the retrieval and generation components of the pipeline. For Phase~A document retrieval, we replaced the PyTerrier PISA index with PostgreSQL-based pg\_textsearch for BM25 retrieval and adopted Qdrant for dense embedding indexing, enabling more efficient storage and GPU-accelerated similarity search. We explored HyDE-based query expansion alongside a Context-1 retrieval strategy. A new reranker training pipeline was developed, incorporating dense retrieval for negative sampling. For Phases A+ and B answer generation, we introduced an LLM-as-a-judge framework and a novel agent quorum mechanism, where multiple agents with diverse prompts debate and iteratively converge on a consensus answer using adaptive document retention. We also participated in the snippets generation subtask for the first time. Our systems achieved competitive results across all batches, with Phase~A systems achieving MAP ranks of 5 (Batch~1,3). We discuss the impact of these architectural changes, lessons learned, and outline directions for future work including SPLADE and ColBERT integration. All code is openly available: https://github.com/bioinformatics-ua/BioASQ14b.

## Metadata
- **Published**: 2026-09-04T11:10:07Z
- **Authors**: André Ribeiro, Rúben Garrido, Alexander Christiansen, Richard A. A. Jonker, Sérgio Matos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04999v1)