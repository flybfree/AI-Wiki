---
title: FluxBin: Flexible LUT-based Ultra-low-bit LLM Inference by Algorithm-Kernel Synergy
published: 2026-08-16T08:01:06Z
authors: Qingyao Yang, Runming Yang, He Xiao, Wendong Xu, Junyu Chen, Haobo Liu, Chenchen Ding, Ruihan Hu, Yik-Chung Wu, Ngai Wong
url: http://arxiv.org/abs/2608.15602v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FluxBin: Flexible LUT-based Ultra-low-bit LLM Inference by Algorithm-Kernel Synergy

## Abstract
While binary quantization theoretically promises extreme compression and acceleration for Large Language Models (LLMs), existing research often overlooks the necessity of specialized hardware kernels, thus failing to unleash the full acceleration potential due to persistent reliance on expensive floating-point arithmetic or runtime dequantization overheads. To bridge this gap, we propose FluxBin (\textbf{F}lexible \textbf{L}UT-based \textbf{U}ltra-low-bit e\textbf{X}ecution with \textbf{Bin}ary bases), an algorithm-kernel co-design that synergizes post-training quantization with a highly optimized CUDA kernel. Algorithmically, we introduce Decoupled Row-Column Binary Decomposition to enhance representational capacity while maintaining hardware efficiency, complemented by a Hessian-guided saliency-aware hybrid bases that preserve critical information. At the kernel level, we implement a Lookup Table Building Approach with Scale Fusion to reduce floating-point arithmetic, featuring a Virtual Columnar Mapping that transforms irregular, sparse, and salient matrices into dense execution. Extensive evaluations demonstrate FluxBin achieves up to $5.92\times$ speedup and $10.19\times$ energy savings across diverse model architectures, delivering comparable accuracy to heavily fine-tuned methods. This effectively enables the deployment of 70B-scale models on one single A100 GPU with a $4\times$ memory reduction. Code is available at https://github.com/nicyyyy/FluxBin.

## Metadata
- **Published**: 2026-08-16T08:01:06Z
- **Authors**: Qingyao Yang, Runming Yang, He Xiao, Wendong Xu, Junyu Chen, Haobo Liu, Chenchen Ding, Ruihan Hu, Yik-Chung Wu, Ngai Wong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15602v1)