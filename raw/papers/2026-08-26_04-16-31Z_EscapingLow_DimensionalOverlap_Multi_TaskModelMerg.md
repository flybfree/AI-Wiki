---
title: Escaping Low-Dimensional Overlap: Multi-Task Model Merging via High-Dimensional Sparse Disentanglement
published: 2026-08-26T04:16:31Z
authors: Yihang Zhang, Shengke Sun, Junjie Wen, Feng Zeng
url: http://arxiv.org/abs/2608.25354v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Escaping Low-Dimensional Overlap: Multi-Task Model Merging via High-Dimensional Sparse Disentanglement

## Abstract
Model merging provides an efficient way to construct multi-task generalist models without additional training, but its performance often degrades under severe task interference. Task interference in model merging primarily stems from \textit{superposition}, where task-specific features become entangled within the parameter space. This entanglement renders conventional decomposition methods insufficient for effectively isolating useful task directions from interfering components. In this paper, we propose a sparse-representation-based merging framework that uses Sparse Autoencoders (SAEs) to project task vectors into a high-dimensional sparse feature space, enabling feature-level disentanglement before fusion. To reduce computational overhead, we further introduce a lightweight Group-Ranked Zeroth-Order Optimizer (GR-ZOO) to identify task-critical layers for selective merging. Experiments on both Qwen2.5-1.5B and Qwen2.5-7B demonstrate that our method consistently outperforms representative baselines, including Task Arithmetic, TIES-Merge, DARE, Fisher-Merge,and several recent training-free merging methods, across mathematical reasoning, code generation, instruction following, and general knowledge tasks. In a highly conflicting four-task setting on Qwen2.5-1.5B, our method further achieves a 2.78\% improvement over the strongest baseline.

## Metadata
- **Published**: 2026-08-26T04:16:31Z
- **Authors**: Yihang Zhang, Shengke Sun, Junjie Wen, Feng Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25354v1)