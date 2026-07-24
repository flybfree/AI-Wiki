---
title: Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts
published: 2026-07-21T19:40:06Z
authors: Minyu Cui, Anna Wingkvist, Morgan Ericsson
url: http://arxiv.org/abs/2607.19539v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts

## Abstract
Mixture-of-Experts (MoE) architectures increase model capacity without proportionally increasing computation cost and have become a key building block for scaling large language models (LLMs) to trillion-parameter regimes. Efficient deployment of these MoE models relies on distributed execution across multiple GPUs, where each MoE layer involves two all-to-all communications: dispatching tokens to expert ranks and returning the expert outputs to their source ranks. Conventional MoE implementations launch this return all-to-all after expert compute completes, exposing communication latency on the critical path and reducing GPU utilization. We present a fine-grained approach that overlaps expert compute with the second all-to-all via tile-level signaling and scheduling. Our producer-consumer co-design combines: (1) a persistent per-rank computation kernel (producer) that covers all local experts on the rank to eliminate repeated kernel launch overhead and prioritizes remote-critical tiles, and (2) a persistent communication kernel (consumer) on a small dedicated partition of streaming multiprocessors (SMs) that issues segment-granular transfers as tiles become ready. Our co-design avoids intrusive changes to the underlying computation operators or communication primitives, making it practical for improving distributed MoE execution efficiency on multi-GPU systems. On a 4-A100 GPU platform, evaluated on three MoE models against four state-of-the-art MoE systems, our approach achieves up to 2.64x end-to-end speedup and 2.74x MoE-layer speedup. Compared with a conventional non-overlap baseline, our approach consistently improves both operator- and MoE-layer-level performance across varying GEMM shapes, router modes, and a broad range of producer/consumer SM partitions, while preserving correctness.

## Metadata
- **Published**: 2026-07-21T19:40:06Z
- **Authors**: Minyu Cui, Anna Wingkvist, Morgan Ericsson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19539v1)