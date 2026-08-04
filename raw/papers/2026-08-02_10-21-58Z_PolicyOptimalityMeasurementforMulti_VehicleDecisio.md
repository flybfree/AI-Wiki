---
title: Policy Optimality Measurement for Multi-Vehicle Decision-Making: From Extrinsic Indicators to Intrinsic Quality
published: 2026-08-02T10:21:58Z
authors: Ye Han, Lijun Zhang, Dejian Meng
url: http://arxiv.org/abs/2608.01133v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Policy Optimality Measurement for Multi-Vehicle Decision-Making: From Extrinsic Indicators to Intrinsic Quality

## Abstract
Evaluating Multi-Agent Reinforcement Learning (MARL) policies in autonomous driving fundamentally relies on extrinsic statistical indicators (e.g., reward curves and success rates), which often mask intrinsic policy degradation and algorithmic blind spots. To break this black-box evaluation, this letter proposes a novel information-theoretic diagnostic framework. By leveraging a fully converged Monte Carlo Tree Search (MCTS) as an asymptotic oracle, we establish a theoretical ground-truth baseline distribution. We formulate a bounded policy optimality score ($\mathcal{M}_{opt}$) using the forward KL divergence to rigorously penalize fatal collaborative omissions. Crucially, we semantically decouple this metric into lateral and longitudinal dimensions, creating a granular "semantic microscope". Extensive spatial and temporal diagnostics on state-of-the-art MARL architectures and exploration mechanisms demonstrate that our framework conclusively exposes hidden directional biases, identifies temporal average-policy traps, and transforms heuristic hyperparameter tuning into a visually trackable trajectory optimization. This framework establishes a rigorous, model-agnostic standard for benchmarking intrinsic multi-agent policy quality.

## Metadata
- **Published**: 2026-08-02T10:21:58Z
- **Authors**: Ye Han, Lijun Zhang, Dejian Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01133v1)