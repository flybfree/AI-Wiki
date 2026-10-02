---
title: MemFit: Efficient Long-Term Agentic Memory
published: 2026-10-01T00:44:33Z
authors: Mitchell Piehl, Muchao Ye
url: http://arxiv.org/abs/2610.00872v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemFit: Efficient Long-Term Agentic Memory

## Abstract
Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications. Current memory systems rely on LLM agents to organize and consolidate memory, resulting in costly, inefficient write operations. To address this limitation, we propose MemFit, a long-term memory system for conversational agents that reduces the cost and latency of memory operations. Unlike existing systems that rely on expensive LLM calls for memory construction or discard surface-level details through compression, MemFit stores each turn verbatim in an append-only store with near-instantaneous, LLM-free insertion, indexing turns with segment summaries rather than replacing them. Additionally, MemFit uses an LLM-free, multi-path retrieval strategy that combines lexical and semantic signals with cross-encoder reranking over caption- augmented episodes in both textual and multimodal settings. Empirical results on three widely used benchmarks, LoCoMo, MemGallery, and LongMemEval-S, show that MemFit achieves state-of-the-art performance while reducing memory construction time and cost several-fold, providing a scalable and efficient solution for persistent agentic memory.

## Metadata
- **Published**: 2026-10-01T00:44:33Z
- **Authors**: Mitchell Piehl, Muchao Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00872v1)