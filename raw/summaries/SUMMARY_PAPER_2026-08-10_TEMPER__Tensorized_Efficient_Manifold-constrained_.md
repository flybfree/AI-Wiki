---
title: TEMPER: Tensorized Efficient Manifold-constrained Parameterization for Expressive Residual Routing
url: http://arxiv.org/abs/2608.07851v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_01-45-27Z_TEMPER_TensorizedEfficientManifold_constrainedPara.md
generated_at: 2026-08-10 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TEMPER, a tensorized efficient manifold‑constrained parameterization for expressive residual routing that reduces generator bottleneck issues. It replaces dense generators with multi‑way tensors and tensor networks to keep parameters low while preserving token‑dependent routing. Experiments show TEMPER matches or exceeds mHC on language modeling and commonsense tasks.

## Key Takeaways
- Tensor ranks control the dimensionality of the learned routing subspace, allowing full ranks to recover dense routing when needed.
- The generator approximation errors bound differences in routing logits and consequently in the routed‑block outputs.
- At eight residual streams TEMPER achieves the best CORE score while using about 84% fewer additional parameters than mHC.

## Context
Deep neural networks rely on residual connections to maintain gradient flow, yet existing methods suffer from exploding parameter counts as stream count grows. This work addresses a structural bottleneck that limits scalability and interpretability of high‑stream routing architectures.

## Implications
TEMPER offers a more efficient way to scale deep models without sacrificing performance, encouraging researchers to adopt tensor‑based representations for routing components. Practitioners can reduce memory usage and training time while maintaining or improving model quality on large language tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07851v1)
