---
title: GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix
published: 2026-08-16T07:19:49Z
authors: Jinhyun Jeon, Sungjoo Yoo
url: http://arxiv.org/abs/2608.15584v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix

## Abstract
Production paged-serving engines apply uniform paging granularity to the KV cache, even though the two regions of a multi-agent workload have opposite storage requirements: a long shared prefix demands contiguity, while the per-request suffix demands fine-grained allocation.   We present \textbf{GraniKV}, a KV-cache layer that allocates the shared prefix in a contiguous HOT pool and the suffix in a token-level COLD pool, combined with a per-step dispatcher which selects the appropriate backend among dual backends for each regime (compute-, memory-, or communication-bound). To the best of our knowledge, GraniKV is the first system to apply asymmetric paging granularity to the KV cache of a production paged-serving engine.   At $L_p{=}16$\,K shared tokens GraniKV reaches $\mathbf{2.16\times}$, $\mathbf{1.98\times}$, and $\mathbf{1.57\times}$ output-token throughput over the production baseline on Llama-3.1-8B/TP=1, Qwen-2.5-14B/TP=2, and Qwen-2.5-32B/TP=4. The gain decomposes: cascade attention integration contributes the majority at saturation; the asymmetric storage layer adds $1.05$--$1.15\times$ end-to-end while being what makes the batched-GEMM prefix backend possible at all. Under heterogeneous multi-agent serving with \emph{distinct} prompts of different lengths, the attribution inverts: GraniKV sustains $\mathbf{1.95\times}$ while batch-global cascade collapses to parity --- the storage layer alone carries the win in the regime that motivates the paper.

## Metadata
- **Published**: 2026-08-16T07:19:49Z
- **Authors**: Jinhyun Jeon, Sungjoo Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15584v1)