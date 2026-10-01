---
title: Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs
url: http://arxiv.org/abs/2609.40093v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_16-32-25Z_EfficientExpert_ParallelCommunicationonPCIe_Connec.md
generated_at: 2026-09-30 22:43
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces ThunderEP, a specialized communication framework designed to optimize expert parallelism for large Mixture-of-Experts models on PCIe-connected consumer GPU systems where direct GPU-to-GPU access is unavailable. By eliminating CPU relay hops, leveraging DMA engines to prevent compute resource contention, and reducing synchronization polling overhead, ThunderEP significantly accelerates MoE inference compared to standard libraries like NCCL. Evaluations on RTX 4090 and RTX 5090 systems demonstrate average speedups of up to 2.00x for dispatch operations and 1.66x end-to-end over state-of-the-art frameworks when integrated into vLLM.

## Key Takeaways
- Existing expert parallelism libraries largely overlook consumer GPUs by assuming direct GPU-to-GPU access, forcing PCIe-based systems to route data through CPU memory; standard solutions like NCCL exacerbate this by incurring redundant transfers and

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.40093v1)
