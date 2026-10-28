---
title: WAKMan: Workload Aware KVCache Manager
published: 2026-10-26T22:19:37Z
authors: Suhas Kumar Morisetty, Vaibhavi Lokegaonkar, Sachin Mathew Varghese, Wesley Harris
url: http://arxiv.org/abs/2610.36355v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WAKMan: Workload Aware KVCache Manager

## Abstract
Prefix caching enables a Large Language Model (LLM) servers to reuse the Key-Value (KV) states and accelerate prefill computation stage for requests that share a prefix with earlier prompts, thus reducing latency and serving cost. With limited memory resource, the KV cache eviction policy becomes a decisive factor in determining the overall benefits of prefix caching. Production traffic may have single-turn, multi-turn, agentic, or a mixture of any combination of these request types. Our findings indicate that agentic steps return within seconds and favor recency, while popular prompts and long conversations return after many other requests and favor frequency. Across 20 mixes, no single policy is always best: vLLM's default strategy LRU provides 12% higher cache hits as compared to the frequency-oriented S3FIFO on agentic-heavy mixes but trails it by up to 22% elsewhere, and even a single workload parameter can flip the winner even for any particular mix. We present WAKMan, a workload-aware KV cache manager that picks its eviction policy from live traffic without knowing request types or reading prompts. It improves hit rate over LRU by 5 percentage points on average, with the lowest mean and worst-case optimality gap of all policies.

## Metadata
- **Published**: 2026-10-26T22:19:37Z
- **Authors**: Suhas Kumar Morisetty, Vaibhavi Lokegaonkar, Sachin Mathew Varghese, Wesley Harris
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36355v1)