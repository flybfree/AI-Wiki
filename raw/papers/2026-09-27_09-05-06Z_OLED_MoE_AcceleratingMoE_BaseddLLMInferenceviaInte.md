---
title: OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading
published: 2026-09-27T09:05:06Z
authors: Jingyuan Xiao, Jiayue Wang, Yitao Hu, Xinning Wang, Shi Chen, Ziqi Gong, Zhengchao Wang, Guotao Yang, Sheng Chen, Keqiu Li
url: http://arxiv.org/abs/2609.33385v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading

## Abstract
Semi-autoregressive diffusion large language models (dLLMs) improve decoding parallelism through iterative block-wise denoising, but scaling them with mixture-of-experts (MoE) layers introduces a large expert parameter footprint that exceeds memory-constrained GPU capacity. Expert offloading is a natural remedy, yet existing MoE serving systems target autoregressive decoding and rely on intra-iteration layer-wise prefetching: while computing one layer, they predict and load experts for subsequent layers. Under dLLM inference, block-wise routing expands the active expert working set within each iteration, making such prefetches difficult to complete in time and costly when mispredicted. Consequently, existing prefetch-based solutions often degenerate into on-demand expert loading with high decoding latency.   We propose OLED-MoE, an expert offloading system that shifts the optimization target from intra-iteration prefetching to inter-iteration expert retention. Its key insight is that adjacent denoising iterations exhibit strong expert routing overlap, and token confidence indicates which experts are likely to be reused. OLED-MoE uses confidence-guided inter-iteration prediction to retain high-value experts in GPU memory without introducing extra prefetch traffic. It further compensates unavoidable cache misses through CPU-GPU cooperative execution, jointly considering dynamic expert computation load and predicted future reuse. Across diverse dLLM workloads, OLED-MoE reduces time per output token (TPOT) by 1.23x-7.93x and improves expert cache utilization by 1.44x-4.23x over state-of-the-art offloading systems. Notably, OLED-MoE approaches full-residency performance while using only 40% of the expert GPU memory, incurring merely 23% higher TPOT despite a 60% reduction in expert memory footprint. OLED-MoE's source code is publicly available at https://github.com/flashserve/OLED-MoE.

## Metadata
- **Published**: 2026-09-27T09:05:06Z
- **Authors**: Jingyuan Xiao, Jiayue Wang, Yitao Hu, Xinning Wang, Shi Chen, Ziqi Gong, Zhengchao Wang, Guotao Yang, Sheng Chen, Keqiu Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33385v1)