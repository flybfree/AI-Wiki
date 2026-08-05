---
title: DS@GT-ARC at eRisk 2026 Task 3: Sparse, Semantic, and LLM Reranking for ADHD Symptom Sentences
published: 2026-08-04T16:19:22Z
authors: David Guecha
url: http://arxiv.org/abs/2608.03883v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DS@GT-ARC at eRisk 2026 Task 3: Sparse, Semantic, and LLM Reranking for ADHD Symptom Sentences

## Abstract
This paper describes our submissions to eRisk 2026 Task 3, ADHD Symptom Sentence Ranking. The task requires systems to rank candidate Reddit sentences according to their relevance to each of the 18 symptoms in the Adult ADHD Self-Report Scale (ASRS-v1.1). Because no annotated training data were released for this first edition of the task, we relied on zero-shot experimentation, manual validation, and unsupervised or weakly guided retrieval pipelines. Our systems combine sparse BM25 retrieval, evidence-aware rescoring for self-referential symptom reports, embedding-based reranking, query-prototype expansion, and LLM-based reranking. All submitted systems follow a staged retrieval design in which BM25 retrieves candidates at scale and semantic or LLM rerankers refine the final rankings. Among our submissions, the LLM reranker achieved the strongest official scores, followed by the prototype query-expansion run. Our manual top-10 analysis aligned with the official expert scoring trend, suggesting that staged reranking is a promising direction for further development.

## Metadata
- **Published**: 2026-08-04T16:19:22Z
- **Authors**: David Guecha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03883v1)