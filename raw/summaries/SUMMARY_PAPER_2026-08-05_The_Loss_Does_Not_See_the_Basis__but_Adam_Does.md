---
title: The Loss Does Not See the Basis, but Adam Does
url: http://arxiv.org/abs/2608.05136v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-56-26Z_TheLossDoesNotSeetheBasis_butAdamDoes.md
generated_at: 2026-08-05 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why gradient descent on a factored model $W = UV^\top$ is biased toward low‑rank solutions while Adam, starting from the same small initialization, does not recover the true basis. It attributes this difference to the gauge symmetry of the loss and shows that only optimizers satisfying certain equivariance conditions can benefit from gradient flow’s low‑rank mechanism.

## Key Takeaways
- Gradient descent’s low‑rank bias stems from its gauge‑equivariance, allowing it to follow the manifold of solutions when starting from a small initialization.  
- Adam lacks this equivariance because it updates each column independently, breaking the symmetry and thus cannot recover the exact basis even after training.  
- The paper demonstrates that a one‑parameter family of shared‑scalar preconditioners restores monotonic low‑rank recovery, isolating anisotropy as the root cause.

## Context
In modern deep learning, optimizers such as Adam are widely used for their adaptive behavior, yet they often deviate from theoretically optimal solutions. Understanding the underlying mathematical properties of these methods can guide better model design and training strategies.

## Implications
For practitioners, choosing an optimizer that preserves gauge symmetry may improve low‑rank parameter recovery in factorized models like transformers. This insight could lead to more robust architectures and potentially reduce overfitting on underdetermined problems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05136v1)
