---
title: Reservoir of Importance: Learning Semi-Structured Sparsity with Differentiable Subset Sampling
published: 2026-08-24T09:54:24Z
authors: Ha Dinh, Xuan Duy Ta, Khoat Than, Khac-Hoai Nam Bui
url: http://arxiv.org/abs/2608.23048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reservoir of Importance: Learning Semi-Structured Sparsity with Differentiable Subset Sampling

## Abstract
Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs). However, existing learnable-mask approaches incur substantial parameter and memory overhead, limiting their scalability to large models and aggressive sparsity regimes. In this work, we revisit semi-structured pruning from a perspective that reconciles efficiency with scalability. We propose Reservoir of Importance (RoI), a lightweight semi-structured pruning framework that learns sparsity masks through differentiable subset sampling. Unlike prior methods that model full categorical distributions over all feasible $N$:$M$ patterns, RoI introduces a compact-logit parameterization for sparsity mask learning and performs sampling without replacement to select masks, thereby reducing trainable parameters from combinatorial complexity to $\mathcal{O}({M})$. As a result, RoI requires 1.5-8.75$\times$ fewer learnable parameters and significantly lower memory cost, while remaining fully aligned with hardware-friendly sparsity patterns. Extensive evaluations across multiple scales of the Qwen2.5 LLM family (0.5-7B parameters) demonstrate that RoI achieves competitive performance with strong memory efficiency, stability, and scalability to more aggressive $N$:$M$ sparsity patterns, offering a practical path toward efficient LLM deployment.

## Metadata
- **Published**: 2026-08-24T09:54:24Z
- **Authors**: Ha Dinh, Xuan Duy Ta, Khoat Than, Khac-Hoai Nam Bui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23048v1)