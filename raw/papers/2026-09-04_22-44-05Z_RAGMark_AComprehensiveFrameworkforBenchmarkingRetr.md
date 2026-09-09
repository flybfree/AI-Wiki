---
title: RAGMark: A Comprehensive Framework for Benchmarking Retrieval-Augmented Generation Systems
published: 2026-09-04T22:44:05Z
authors: Zlatan Feric, Amir Taherin, Bin Ren, Yanzhi Wang, Jennifer Dy, David Kaeli
url: http://arxiv.org/abs/2609.05760v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RAGMark: A Comprehensive Framework for Benchmarking Retrieval-Augmented Generation Systems

## Abstract
We present RAGMark, a modular benchmarking framework for advanced Retrieval-Augmented Generation (RAG) systems targeting small-scale multi-GPU environments. RAGMark evaluates diverse RAG components, including retrievers, vector databases, prompt-processing methods, and generator models, while collecting detailed per-stage metrics such as latency, GPU utilization, memory consumption, power usage, time to first token (TTFT), throughput, and answer quality. The framework is highly extensible, separating RAG stages, timing, and resource monitoring into modular components, and is designed to efficiently sweep large configuration spaces while minimizing repeated model and database initialization overhead. Using RAGMark, we characterize five RAG workloads on open-domain QA datasets across varying retrieval depths, model scales, reranking, compression methods, and vector database configurations. We show that while autoregressive generation dominates latency in naive pipelines, context-reduction techniques shift bottlenecks across compute, memory bandwidth, and preprocessing stages. Reranking and compression produce compounding benefits: reranking reduces compression workload itself, while both jointly reduce prefill and KV-cache traversal costs, lowering energy consumption by up to 66%. We further observe strong cross-stage interactions, where small upstream context reductions cascade through downstream latency, memory traffic, and energy consumption. The RAGMark source code is publicly available at: https://github.com/zferic/RAGMark.

## Metadata
- **Published**: 2026-09-04T22:44:05Z
- **Authors**: Zlatan Feric, Amir Taherin, Bin Ren, Yanzhi Wang, Jennifer Dy, David Kaeli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05760v1)