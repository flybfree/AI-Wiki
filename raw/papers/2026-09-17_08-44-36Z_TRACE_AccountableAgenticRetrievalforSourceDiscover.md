---
title: TRACE: Accountable Agentic Retrieval for Source Discovery in Digital Archives
published: 2026-09-17T08:44:36Z
authors: Donghan Bian, Marie Puren, Florian Cafiero
url: http://arxiv.org/abs/2609.19897v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE: Accountable Agentic Retrieval for Source Discovery in Digital Archives

## Abstract
Historical archives pose a difficult retrieval problem for retrievalaugmented generation systems: documents are OCR-degraded, heterogeneous across genres and sources, and require strong source traceability for scholarly and institutional use. We introduce TRACE, a training-free agentic retrieval framework designed for accountable source discovery over historical corpora. The system was developed in the context of DECIDON, an interdisciplinary project on the circulation of political discourse between parliamentary debates and the press during the French Third Republic, involving digitised historical collections and institutional use cases. The prototype is currently deployed internally within the project and accessible to 24 researchers across six partner institutions. We evaluate TRACE on HistoriQA-ThirdRepublic, a benchmark of 1,752 French historical questions over parliamentary debates and newspapers from 1887, with documents derived from Biblioth{è}que nationale de France digitised collections. TRACE achieves R@10 = 0.856 and MRR = 0.653, outperforming sparse, dense, graph-based, and agentic RAG baselines, with the largest gains on multi-hop and cross-corpus questions. At approximately $0.02 per question under the default hosted inference configuration, TRACE also remains economically feasible for heritage institutions, laboratories or companies that cannot rely on costly local GPU infrastructure. These results suggest that, for large digital libraries and archives, retrieval accountability and corpus-aware agent design can provide a practical alternative to heavier training-based or graph-construction approaches.

## Metadata
- **Published**: 2026-09-17T08:44:36Z
- **Authors**: Donghan Bian, Marie Puren, Florian Cafiero
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19897v1)