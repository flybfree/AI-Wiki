---
title: A Statistical Difference between Single-Layer Learning and Hierarchical Learning in Wide Neural Networks
url: http://arxiv.org/abs/2607.23397v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_00-11-54Z_AStatisticalDifferencebetweenSingle_LayerLearninga.md
generated_at: 2026-07-27 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper examines a three‑layer neural network with many hidden units to compare two training regimes: one that learns the input‑to‑hidden weights while keeping them fixed, and another where only the output layer is trained. The results show that learning the intermediate weights reduces generalization error and eliminates singularities in the parameter space.

## Key Takeaways
- Learning the input‑to‑hidden weights yields a lower generalization error than fixing those weights.  
- Fixed parameters lead to singularities within the network’s training region, which do not occur when the hidden layer is trained.  
- These singularities are absent in the regime where intermediate weights can move away from initialization.

## Context
Hierarchical neural networks remain popular for deep learning tasks, yet their behavior under infinite width limits is still debated. Understanding how parameter dynamics affect generalization provides insight into robust model design.

## Implications
For practitioners, training deeper layers can improve performance and avoid pathological singularities that degrade results. This knowledge may guide regularization strategies and architecture choices in large‑scale AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23397v1)
