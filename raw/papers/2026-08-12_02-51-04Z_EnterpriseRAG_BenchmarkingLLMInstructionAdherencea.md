---
title: EnterpriseRAG: Benchmarking LLM Instruction Adherence and Robustness under Non-Ideal Enterprise Retrieval
published: 2026-08-12T02:51:04Z
authors: Huiqi Miao, Xinbao Sun, Bo Wang, Fanyu Meng, Lijun Mei, Na Wu, Di Jin, Chao Deng, Junlan Feng
url: http://arxiv.org/abs/2608.11584v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EnterpriseRAG: Benchmarking LLM Instruction Adherence and Robustness under Non-Ideal Enterprise Retrieval

## Abstract
Enterprise RAG deployments face a critical reliability gap: while LLMs satisfy 80% of individual constraints, only 26.8% of responses meet all requirements simultaneously, revealing a 57-point orchestration gap. Existing benchmarks assume clean retrieval with simple queries, failing to capture production conditions where noisy documents and multi-dimensional constraints coexist. We introduce EnterpriseRAG, a benchmark of 983 expert-validated samples across six domains that systematically simulates three failure modes absent from prior work: retrieval noise, knowledge gaps, and factual conflicts, coupled with complex instructions. Evaluation of 13 state-of-the-art LLMs reveals a severe instruction adherence collapse, where high per-constraint satisfaction masks low holistic compliance. Critical findings expose deep barriers under knowledge gaps and factual conflicts, even with reasoning-enhanced inference, indicating production RAG requires explicit context-aware protocols and calibrated judgment. EnterpriseRAG provides a reproducible foundation for measuring and closing these gaps, directly informing deployment decisions for enterprise-scale RAG systems. We will release the benchmark and evaluation framework upon publication.

## Metadata
- **Published**: 2026-08-12T02:51:04Z
- **Authors**: Huiqi Miao, Xinbao Sun, Bo Wang, Fanyu Meng, Lijun Mei, Na Wu, Di Jin, Chao Deng, Junlan Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11584v1)