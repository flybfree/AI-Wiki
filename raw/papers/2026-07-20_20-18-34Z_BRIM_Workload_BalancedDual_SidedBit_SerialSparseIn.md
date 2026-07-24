---
title: BRIM: Workload-Balanced Dual-Sided Bit-Serial Sparse Inference Accelerator
published: 2026-07-20T20:18:34Z
authors: Varun Manjunath, Ruokai Yin, Donghyun Lee, Arkapravo Ghosh, Priyadarshini Panda
url: http://arxiv.org/abs/2607.19431v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BRIM: Workload-Balanced Dual-Sided Bit-Serial Sparse Inference Accelerator

## Abstract
Bit-serial accelerators exploit bit-level sparsity to reduce DNN inference cost, but existing designs exploit sparsity on only one operand, bounding the speedup. Extending sparsity exploitation to both operands simultaneously yields compounding reductions in partial products but introduces a critical new bottleneck: workload imbalance. Because each concurrent weight - activation pair's execution cost depends on the product of two independently varying operand non-zero bit counts, pairs that must complete together finish at vastly different times, leaving faster computations idle. We show this limits PE utilization to 56 - 64% in existing dual-sided designs. We present BRIM, a hardware - software co-designed dual-sided bit-serial sparse accelerator that directly targets this bottleneck. BRIM combines two integrated mechanisms: 1) Cyclic-Balanced Pruning (CBP), a post-training weight optimization that reshapes weight representations based on profiled activation statistics to equalize expected workloads across concurrently processed pairs offline; and 2) Pairwise Slot Donation, a lightweight hardware mechanism that absorbs residual runtime imbalance with negligible area overhead. Evaluated across CNNs, ViTs, and LLMs under iso-area constraints, BRIM achieves over 90% PE utilization, up to 2.37x speedup, and up to 1.63x energy efficiency improvement over prior dual-sided designs.

## Metadata
- **Published**: 2026-07-20T20:18:34Z
- **Authors**: Varun Manjunath, Ruokai Yin, Donghyun Lee, Arkapravo Ghosh, Priyadarshini Panda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19431v1)