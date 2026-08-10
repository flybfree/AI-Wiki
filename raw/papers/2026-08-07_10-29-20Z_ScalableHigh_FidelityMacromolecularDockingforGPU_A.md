---
title: Scalable High-Fidelity Macromolecular Docking for GPU-Accelerated Supercomputers
published: 2026-08-07T10:29:20Z
authors: Xiangyu Meng, Peng Chen, Mingzhen Li, Jianmin Wang, Sen Wang, Guangming Tan, Weile Jia, Mohamed Wahib, Tao Luo, Xun Wang
url: http://arxiv.org/abs/2608.07078v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scalable High-Fidelity Macromolecular Docking for GPU-Accelerated Supercomputers

## Abstract
Flexible macromolecular docking offers high-fidelity predictions of biomolecular interactions, but remains prohibitively expensive at scale. Among existing approaches, LightDock leverages Glowworm Swarm Optimization (GSO) for accuracy, yet suffers from limited parallelism, irregular computation, and severe load imbalance, preventing efficient execution on GPU supercomputers. We present SparkleDock, a scalable GSO-based docking framework enabling near-real-time flexible docking. We redesign GSO to expose massive fine-grained parallelism at the glowworm-agent level, and restructure the dominant energy scoring computation into a Tensor Core-compatible formulation, enabling efficient execution of irregular pairwise interactions through structured matrix operations. We further introduce a performance-model-driven scheduling for load balancing and out-of-core scaling across GPUs. SparkleDock achieves 9.7 $\times$ and 18.9 $\times$ speedups over LightDock on single A100 and H100 GPU, and delivers over two orders of magnitude acceleration at scale. On 512 GPUs, it reduces docking time from hours to seconds, enabling large-scale, high-fidelity virtual screening previously impractical with flexible docking.

## Metadata
- **Published**: 2026-08-07T10:29:20Z
- **Authors**: Xiangyu Meng, Peng Chen, Mingzhen Li, Jianmin Wang, Sen Wang, Guangming Tan, Weile Jia, Mohamed Wahib, Tao Luo, Xun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07078v1)