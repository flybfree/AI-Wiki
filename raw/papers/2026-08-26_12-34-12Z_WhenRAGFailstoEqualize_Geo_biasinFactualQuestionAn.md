---
title: When RAG Fails to Equalize: Geo-bias in Factual Question Answering over Public Companies
published: 2026-08-26T12:34:12Z
authors: Abhinav Havaldar, Enrico Santus
url: http://arxiv.org/abs/2608.25717v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When RAG Fails to Equalize: Geo-bias in Factual Question Answering over Public Companies

## Abstract
Retrieval-augmented generation (RAG) is widely assumed to mitigate factual errors in large language models (LLMs), but it remains unclear whether retrieval uniformly compensates for missing knowledge. We study this question in a controlled factual QA setting over public companies, constructing a benchmark of approximately 2,000 firms across global equity indices. We evaluate six LLMs on four atomic attributes under four conditions: no-context, perfect context, misleading context, and distraction context. We find strong geographic disparities in no-context accuracy, indicating uneven parametric knowledge. While perfect context improves performance, it does not eliminate these gaps: gains are correlated with baseline accuracy, suggesting retrieval effectiveness is coupled to internal representations. Under misleading context, models frequently copy incorrect information. Larger models improve overall performance but do not remove these structural effects. These results challenge the view of RAG as a universal corrective and highlight the interaction between model knowledge, context quality, and entity representation.

## Metadata
- **Published**: 2026-08-26T12:34:12Z
- **Authors**: Abhinav Havaldar, Enrico Santus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25717v1)