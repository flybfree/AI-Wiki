---
title: SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware
published: 2026-10-13T10:47:05Z
authors: Jieyun Deng, Keming Hu, Yanghe Liu, Li Feng
url: http://arxiv.org/abs/2610.18140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware

## Abstract
Running large language models (LLMs) on consumer hardware is bottlenecked by the key-value (KV) cache, which grows with every decoded token and quickly exhausts the memory and bandwidth of a single consumer GPU. We present SparPR (Sparse Partial Recomputation), a runtime KV-cache recovery mechanism that does not modify model weights and requires no offline training. SparPR couples three online decisions: Query-Aware key-block selection scores historical blocks against the current query; dynamic budget control estimates per-block copy and recompute costs to decide how many blocks to retain; and on-demand local recomputation with cost-aware fallback merges retained blocks into continuous spans and switches between sparse recomputation and full recovery according to a runtime cost comparison. Implemented on FlexGen/FlexLLMGen, SparPR is evaluated on a single consumer laptop (RTX 3070 Ti 8GB, Ryzen 9 6900HX, 16GB RAM). It cuts end-to-end latency by 31%, 52%, and 63% at 1k, 2k, and 4k prompt tokens respectively, with 1.4x-2.7x higher throughput, and completes an 8k-token workload in 44 minutes where the FlexGen baseline times out. Under a fixed cache budget, SparPR retains a Needle Accuracy that stays well above StreamingLLM and H2O at every keep ratio, and ablation studies confirm that the three mechanisms act jointly.

## Metadata
- **Published**: 2026-10-13T10:47:05Z
- **Authors**: Jieyun Deng, Keming Hu, Yanghe Liu, Li Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18140v1)