---
title: NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering
published: 2026-08-06T17:16:28Z
authors: Jonas Gann, Michael Gertz
url: http://arxiv.org/abs/2608.06292v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering

## Abstract
Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence. Moreover, missing user-specific context is rarely detected systematically, often leading to incomplete or incorrect output.   We propose NeSy-RAG, a modular neuro-symbolic RAG framework that synthesizes attributable Prolog modules from retrieved text chunks. For each chunk, the system generates semantically meaningful predicates that encode Boolean claims, which may depend on user facts. Using joint natural language-code embeddings, predicates are retrieved and composed into Prolog queries. To address incomplete user context, we introduce a symbolic knowledge-gap detection mechanism that identifies missing user facts whose truth values affect the query outcome and automatically triggers follow-up interactions.   Executing the resulting Prolog queries yields deterministic answers together with transparent execution traces that link each reasoning step to its originating source. On the ShARC benchmark, without domain-specific training, NeSy-RAG achieves 61.1% accuracy, outperforming a same-model RAG baseline that achieves 42.8% accuracy.

## Metadata
- **Published**: 2026-08-06T17:16:28Z
- **Authors**: Jonas Gann, Michael Gertz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06292v1)