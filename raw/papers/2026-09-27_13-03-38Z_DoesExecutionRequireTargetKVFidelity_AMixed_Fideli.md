---
title: Does Execution Require Target KV Fidelity? A Mixed-Fidelity KV Runtime for LLM Serving
published: 2026-09-27T13:03:38Z
authors: Jiantong Jiang, Yue Yang, Peiyu Yang, Feng Liu
url: http://arxiv.org/abs/2609.33536v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does Execution Require Target KV Fidelity? A Mixed-Fidelity KV Runtime for LLM Serving

## Abstract
Large language model (LLM) serving is increasingly constrained by the GPU memory consumed by key-value (KV) caches. Existing compression, eviction, and offloading techniques alleviate this pressure, but serving runtimes typically treat only the configured target KV representation as execution-ready. Under memory pressure, this target-only contract can turn KV shortage into request stalls and preemptions. We present ElasticKV, a mixed-fidelity KV runtime built on the observation that target fidelity need not gate execution. ElasticKV introduces a compact intermediate KV state, making fidelity a runtime-managed execution property. To realize this state in a paged serving runtime, ElasticKV combines (i) a pair-structured layout that turns fidelity reduction into reusable GPU capacity, (ii) a dual-mode attention backend that directly consumes the compact state while preserving the native target-only path, and (iii) pressure-aware fidelity management that adapts KV fidelity to memory pressure. Our extensive evaluation across diverse workloads, model families and scales, and GPU platforms demonstrates the effectiveness and generality of ElasticKV. Under high concurrency, ElasticKV achieves 3.8-4.0$\times$ lower time-to-first-token (TTFT) and 9.1$\times$ lower P90 TTFT than vLLM while preserving generation quality.

## Metadata
- **Published**: 2026-09-27T13:03:38Z
- **Authors**: Jiantong Jiang, Yue Yang, Peiyu Yang, Feng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33536v1)