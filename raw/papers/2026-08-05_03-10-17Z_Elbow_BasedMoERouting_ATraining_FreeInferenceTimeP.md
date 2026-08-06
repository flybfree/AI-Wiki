---
title: Elbow-Based MoE Routing: A Training-Free Inference Time Plugin for Expert Selection
published: 2026-08-05T03:10:17Z
authors: Robin Pan, Raymond Liu, Daniel Fang, Adelina Andrei, Rosa Wu
url: http://arxiv.org/abs/2608.04401v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Elbow-Based MoE Routing: A Training-Free Inference Time Plugin for Expert Selection

## Abstract
Mixture-of-Experts (MoE) models enable model scaling while maintaining low inference-time compute by activating only a subset of experts per token. However, conventional routing relies on a fixed top-k selection, forcing the model to spend the same compute regardless of how many experts are relevant. We introduce elbow-based routing, a training-free inference-time modification that dynamically adjusts the number of experts on a per-token basis. Our method examines the sorted router probability distribution and identifies an elbow point that separates high- and low-probability experts. We find that most router distributions exhibit clear inflection points suitable for this strategy, and we show both theoretically and empirically that elbow-based routing preserves expert load balance. Experiments on a state-of-the-art MoE model demonstrate an average latency reduction of 5.3% while maintaining accuracy across six benchmarks.

## Metadata
- **Published**: 2026-08-05T03:10:17Z
- **Authors**: Robin Pan, Raymond Liu, Daniel Fang, Adelina Andrei, Rosa Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04401v1)