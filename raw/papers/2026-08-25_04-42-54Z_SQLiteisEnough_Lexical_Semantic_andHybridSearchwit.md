---
title: SQLite is Enough. Lexical, Semantic, and Hybrid Search with scrydb
published: 2026-08-25T04:42:54Z
authors: Timo Breuer
url: http://arxiv.org/abs/2608.24060v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SQLite is Enough. Lexical, Semantic, and Hybrid Search with scrydb

## Abstract
This work introduces scrydb, a Python library that enables lexical, semantic, and hybrid search within SQLite. For lexical search, scrydb leverages SQLite's full-text search extension FTS5. Semantic search builds on sqlite-vec, a SQLite extension for vector search. Furthermore, the library allows users to rerank and fuse retrieval results to combine both lexical and semantic approaches, providing a lightweight solution for downstream tasks in information retrieval (IR) or agentic search. We evaluate scrydb on various IR benchmark datasets and demonstrate its effectiveness in text retrieval based on keyword matching, semantic similarity, and rank fusion. In addition, we provide insights into query latency and the trade-off between efficiency and effectiveness. scrydb is available under the MIT license.

## Metadata
- **Published**: 2026-08-25T04:42:54Z
- **Authors**: Timo Breuer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24060v1)