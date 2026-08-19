---
title: KernelArc: A Multi-Agent Framework for GPU Kernel Optimization
published: 2026-08-17T19:21:23Z
authors: Joyjit Kundu, Ben Stoffelen, Kaili Wang, Peter Vrancx, Ludovic Denoyer
url: http://arxiv.org/abs/2608.17071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KernelArc: A Multi-Agent Framework for GPU Kernel Optimization

## Abstract
We present KernelArc, a multi-agent framework for autonomous GPU kernel optimization across heterogeneous workloads. Strategy-specialized agents run in parallel and coordinate through conclusions-only shared memory, a deterministic benchmark guard, and read-only cross-agent state with plateau-triggered drafting. We evaluate \kernelarc{} on NVIDIA H100 and B200 GPUs using category-representative SOL-ExecBench workloads. The resulting implementations span custom BF16 GEMM, static cuBLASLt Expert-API configuration tables, fused mixture-of-experts backward, shape-gated decoder-layer fusion, native NVFP4 grouped-query attention, and paged prefill attention. At the public SOL-ExecBench leaderboard snapshot recorded on July~30, 2026, these submissions ranked first on representative L1, L2, Quantization, and FlashInfer tasks. The trajectories support the paper's central motivation: shared multi-agent search can broaden exploration and reach stronger incumbents within a fixed candidate budget, while the value of individual coordination features depends on the kernel and optimization stage.

## Metadata
- **Published**: 2026-08-17T19:21:23Z
- **Authors**: Joyjit Kundu, Ben Stoffelen, Kaili Wang, Peter Vrancx, Ludovic Denoyer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17071v1)