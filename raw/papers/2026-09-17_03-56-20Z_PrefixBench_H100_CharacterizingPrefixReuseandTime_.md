---
title: PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving
published: 2026-09-17T03:56:20Z
authors: Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav
url: http://arxiv.org/abs/2609.19657v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving

## Abstract
Repeated prompt prefixes are increasingly common in LLM serving workloads, appearing in system prompts, templated retrieval-augmented generation pipelines, agent frameworks, and multi-turn conversations. Modern inference runtimes such as vLLM and TensorRT-LLM provide mechanisms for reusing previously computed KV-cache state across requests, yet it remains unclear when prefix reuse materially improves serving performance on contemporary accelerators and when its benefits are limited by scheduling, cache granularity, concurrency, or memory pressure.   This paper presents PrefixBench-H100, a reproducible benchmark and measurement framework for characterizing prefix reuse on a single NVIDIA H100. PrefixBench-H100 combines controlled synthetic traces with chat-style and retrieval-style workloads, and evaluates two widely used LLM serving runtimes under matched workload conditions. The benchmark varies shared-prefix length, suffix diversity, request arrival pattern, concurrency, output length, and cache configuration, while collecting time-to-first-token, inter-token latency, end-to-end latency, throughput, cache-hit statistics, GPU memory usage, and selected profiling traces.   The goal of PrefixBench-H100 is not to introduce a new caching algorithm, but to expose the practical operating envelope of prefix reuse for H100-class LLM serving. The study identifies the regime where prefix reuse provides substantial first-token latency reductions and the regime where cache pressure erodes them, while showing that cache effectiveness itself is largely insensitive to concurrency and output length; the cross-runtime differences that remain arise above the cache, in the scheduling layer.

## Metadata
- **Published**: 2026-09-17T03:56:20Z
- **Authors**: Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19657v1)