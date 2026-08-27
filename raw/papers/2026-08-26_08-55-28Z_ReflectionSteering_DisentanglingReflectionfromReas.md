---
title: Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference
published: 2026-08-26T08:55:28Z
authors: Jiarui Hu, Zhiyuan Wen, Xiaoyun Liu, Jiaxing Shen, Yu Yang
url: http://arxiv.org/abs/2608.25542v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reflection Steering: Disentangling Reflection from Reasoning in Activation Space for Token-Efficient Inference

## Abstract
Large reasoning models often produce reasoning traces with verification, revision, and backtracking. When reflection merely re-checks established results, it wastes reasoning tokens and increases latency. Most existing reflection steering methods add a label-derived mean-difference direction across preset layers, but its entanglement with reasoning and length signals destabilizes the accuracy-efficiency trade-off. In this paper, we propose Reflection Steering, a training-free framework for controlling reflection-associated computation within LLMs by disentangling reflection-related activations from general reasoning. Specifically, we contrast reflective and non-reflective hidden states at each LLM layer, denoise the resulting reflection directions with PCA, and orthogonalize them against general-reasoning directions. To limit downstream amplification from early-layer interventions, we calibrate each layer across multiple intervention strengths on a small set, retain only stable layers, and apply bounded projection removal to their residual-stream activations. We conduct extensive experiments across two public benchmarks and three open-weight LLMs against state-of-the-art activation-steering baselines. Results show that Reflection Steering reduces reasoning tokens by 16.9% on average across six matched settings. Besides, our method further introduces a bounded reflection intervention-strength parameter $α$, enabling deployment-time adjustment to balance token savings, accuracy, and generation stability.

## Metadata
- **Published**: 2026-08-26T08:55:28Z
- **Authors**: Jiarui Hu, Zhiyuan Wen, Xiaoyun Liu, Jiaxing Shen, Yu Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25542v1)