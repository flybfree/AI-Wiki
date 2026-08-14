---
title: CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution
published: 2026-08-12T22:31:32Z
authors: Zihao Ye, Yingyi Huang, Hongyi Jin, Bohan Hou, Junru Shao, Zhongming Yu, Jinqi Chen, Meghan Cowan, Shiyi Cao, Shanli Xing, Hanfeng Chen, Vinod Grover, Tianqi Chen, Luis Ceze
url: http://arxiv.org/abs/2608.12629v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution

## Abstract
GPU kernel agents and GPU programming languages have advanced separately, leaving expert kernels difficult to reproduce. Agents usually treat the compiler as a fixed black box and receive only errors, correctness outcomes, and timing, while existing DSLs either hide critical scheduling decisions or expose them through difficult layout abstractions. We present CAKE, a compiler-agent co-design in which agents author CAKE IR, a typed, hardware-explicit schedule representation. CAKE exposes warp roles, memory movement, synchronization, and pipelines while supporting verification, cost modeling, and localized diagnostics. The harness itself evolves: recurring failures become verifier rules, IR primitives, model calibrations, and reusable optimization tactics. In matched implementation-hidden Flash-KMeans clean starts on B200, the best CAKE IR candidate at an 80-million-token budget runs at 1.144x the tuned FlashML baseline, compared with 0.928x for direct CUDA/PTX. Beyond this benchmark, agent-generated Kimi Delta Attention achieves a 2.05x geometric-mean speedup over official FlashKDA and passes end-to-end serving validation. Dispatcher-backed KNN and KMeans improve performance by 1.42x to 2.12x across more than 400 shapes, and four kernel changes are available as upstream PRs. CAKE targets NVIDIA GPUs from Ampere through Blackwell and separates single-shape evolution from library generalization and dispatch.

## Metadata
- **Published**: 2026-08-12T22:31:32Z
- **Authors**: Zihao Ye, Yingyi Huang, Hongyi Jin, Bohan Hou, Junru Shao, Zhongming Yu, Jinqi Chen, Meghan Cowan, Shiyi Cao, Shanli Xing, Hanfeng Chen, Vinod Grover, Tianqi Chen, Luis Ceze
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12629v1)