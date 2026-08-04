---
title: Select-And-Extract: A Lightweight Plugin for Retrieval-Augmented Generation
published: 2026-08-01T13:21:55Z
authors: Chenming Tang, Jiawei Han
url: http://arxiv.org/abs/2608.00658v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Select-And-Extract: A Lightweight Plugin for Retrieval-Augmented Generation

## Abstract
Retrieval-augmented generation (RAG) for language model (LM) systems fundamentally has two failure modes: retrieval failure and reading failure. The former fails to recall the right pieces of information from the external corpus, and the latter fails to produce the correct answer although the right information is retrieved. Some methods perform structured indexing for retrieval failure, but may suffer from limited generalization of the fixed structures. Some methods perform query-time structuring for reading failure, but typically require a lot of LM calls and rely heavily on the LM's capability. To this end, we propose Select-ANd-Extract (SANE), a simple yet effective plugin for RAG. For the retrieval failure, we retrieve a wide set of candidates with a semantic retriever, and leverage the LM to select the top candidates based on their synopses, which yields better recall than the original retriever. For the reading failure, we perform blueprint-guided query-time evidence extraction, which allows the generator LM to use only compact and structured key information so that it can perform better reasoning. Empirical results confirm that SANE brings solid improvements, while only introducing modest extra overhead. As a lightweight plugin for RAG, SANE offers a simple alternative to heavier approaches, and suggests a high-performance RAG framework need not be overly complex.

## Metadata
- **Published**: 2026-08-01T13:21:55Z
- **Authors**: Chenming Tang, Jiawei Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00658v1)