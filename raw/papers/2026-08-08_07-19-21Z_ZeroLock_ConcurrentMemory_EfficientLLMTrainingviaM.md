---
title: ZeroLock: Concurrent Memory-Efficient LLM Training via Modular Update Decoupling
published: 2026-08-08T07:19:21Z
authors: Wentao Dai, Xuanran Li, Yuxiang Zhang, Ming Tang, Chao Huang
url: http://arxiv.org/abs/2608.07974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ZeroLock: Concurrent Memory-Efficient LLM Training via Modular Update Decoupling

## Abstract
Large language model (LLM) fine-tuning at the edge adapts the model to scenario-specific data while preserving privacy. Although existing studies proposed pipeline parallelism to address the limited memory and computing resources of edge devices, they commonly rely on backpropagation (BP) training, which has a fundamental limitation of update locking and could experience severe throughput and memory bottlenecks. In this work, we propose a BP-free algorithm, called ZeroLock, that decouples the model updates into independent chunk updates by local objective construction. It breaks the update locking of BP and hence can improve throughput at the algorithm level and lower memory usage by reducing activation storage. To the best of our knowledge, we provide the first theoretical framework for such local objective construction-based approaches under general model chunk division by mapping local objectives to the global objective. We prove that ZeroLock has a convergence rate of $\tilde{\mathcal{O}}(1/\sqrt{T})$, which differs from BP only by polylogarithmic factors. We design a system for ZeroLock and build real-world prototypes, incorporating techniques such as early forwarding and failure recovery for efficient and robust implementation. Experiments on the prototype show that compared to BP-based baselines, ZeroLock reduces the memory by 26.5% and improves throughput by 4.9%.

## Metadata
- **Published**: 2026-08-08T07:19:21Z
- **Authors**: Wentao Dai, Xuanran Li, Yuxiang Zhang, Ming Tang, Chao Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07974v1)