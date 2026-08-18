---
title: GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix
url: http://arxiv.org/abs/2608.15584v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_07-19-49Z_GraniKV_AsymmetricGranularityKV_CachePagingforMult.md
generated_at: 2026-08-17 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GraniKV, a KV-cache paging system that uses asymmetric granularity: a contiguous HOT pool for the long shared prefix and a token-level COLD pool for the per-request suffix. It combines this storage strategy with a dispatcher that selects among compute-, memory-, or communication-bound backends depending on the regime. Experiments show up to 2.16× output-token throughput over baseline models like Llama-3.1-8B, Qwen-2.5-14B, and Qwen-2.5-32B.

## Key Takeaways
- GraniKV achieves a 2.16× increase in output-token throughput on production systems by separating the shared prefix storage into a contiguous HOT pool while placing suffix tokens in a token-level COLD pool.
- The asymmetric storage layer adds roughly 1.05–1.15× end-to-end gain and enables batched-GEMM prefix backend usage, which is critical for handling long shared prefixes efficiently.
- In heterogeneous multi-agent serving with distinct prompt lengths, GraniKV sustains a 1.95× throughput whereas the batch‑global cascade approach collapses to parity, indicating that the storage layer alone drives the performance win.

## Context
Current AI inference systems treat all KV cache entries uniformly, leading to suboptimal memory usage and latency when workloads contain long shared prefixes followed by short per-request suffixes. This uniform paging granularity can cause unnecessary memory fragmentation and degrade throughput in multi‑agent serving environments where agents have heterogeneous prompt lengths.

## Implications
The findings suggest that production paged‑serving engines should adopt region‑specific caching strategies to match storage demands, improving both efficiency and scalability. Practitioners can implement GraniKV‑inspired designs to reduce memory overhead and boost throughput in large language model serving at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15584v1)
