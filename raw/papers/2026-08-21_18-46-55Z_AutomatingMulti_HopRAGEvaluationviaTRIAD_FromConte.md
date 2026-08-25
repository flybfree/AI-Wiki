---
title: Automating Multi-Hop RAG Evaluation via TRIAD: From Context Extraction to Validated Dataset Generation
published: 2026-08-21T18:46:55Z
authors: Lorenz Brehme, Adam Jatowt
url: http://arxiv.org/abs/2608.21558v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automating Multi-Hop RAG Evaluation via TRIAD: From Context Extraction to Validated Dataset Generation

## Abstract
Recent advances in LLMs and the adoption of RAG systems in industry have created a need for domain-specific question-answer datasets that can assess RAG performance on proprietary data. Existing datasets, such as HotpotQA, challenge current RAG systems on Wikipedia-based knowledge, but they cannot be transferred directly to domain-specific settings. A comprehensive evaluation of RAG system quality requires both multi-hop queries and unanswerable questions. This paper introduces TRIAD, a three-stage automated dataset generation approach. First, it generates question--answer (QA) pairs for the domain-specific knowledge base of a RAG system. Second, a validator checks each QA-pair in a feedback loop. Third, the QA pairs are extended with relevance-labeled context documents for downstream evaluation. We evaluate this approach against the established MuSiQue and HotpotQA datasets. The results show that the generated dataset exhibits similar performance trends across different RAG setups, while human validation indicates that the questions are suitable for evaluating a domain-specific RAG system. The code used to generate the dataset and all validation results are available in our GitHub repository(https://github.com/lorenzbrehme/triad).

## Metadata
- **Published**: 2026-08-21T18:46:55Z
- **Authors**: Lorenz Brehme, Adam Jatowt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21558v1)