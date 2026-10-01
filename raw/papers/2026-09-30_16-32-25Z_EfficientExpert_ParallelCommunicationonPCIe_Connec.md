---
title: Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs
published: 2026-09-30T16:32:25Z
authors: Jaehwan Lee, Sangmin Lee, Chaewon Kim, Junsik Shin, Jaejin Lee
url: http://arxiv.org/abs/2609.40093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs

## Abstract
Expert parallelism (EP) enables inference of large Mixture-of-Experts (MoE) models by placing their experts across multiple GPUs, but requires substantial communication between GPUs at every MoE layer. As contemporary MoE models activate more experts per token, this communication accounts for a growing fraction of inference time. The cost becomes particularly pronounced on PCIe-based consumer GPU systems, where all inter-GPU transfers traverse CPU memory. However, existing MoE-specialized EP communication libraries assume that direct GPU-to-GPU access is available, largely overlooking consumer GPUs. Therefore, most LLM frameworks instead rely on NCCL, whose CPU-staged communication incurs redundant PCIe transfers and competes with expert computation for GPU resources, limiting their overlap. We present ThunderEP, a novel communication design for such systems that removes the relay hops of traditional ring algorithm, moves data through DMA engines to avoid compute resource contention, and minimizes synchronization latency by reducing the polling overhead of completion flags in CPU memory. We integrate the proposed design into vLLM and evaluate it on three widely used MoE models. Experiments on two PCIe systems equipped with RTX 4090 and RTX 5090 GPUs show that ThunderEP achieves average speedups of 2.00$\times$ and 1.53$\times$ over NCCL for dispatch and combine, respectively, and up to 1.66$\times$ end-to-end speedup over state-of-the-art MoE inference frameworks.

## Metadata
- **Published**: 2026-09-30T16:32:25Z
- **Authors**: Jaehwan Lee, Sangmin Lee, Chaewon Kim, Junsik Shin, Jaejin Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.40093v1)