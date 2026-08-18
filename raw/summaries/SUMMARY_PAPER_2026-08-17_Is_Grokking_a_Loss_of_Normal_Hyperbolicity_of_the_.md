---
title: Is Grokking a Loss of Normal Hyperbolicity of the Interpolation Manifold?
url: http://arxiv.org/abs/2608.14803v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_18-16-47Z_IsGrokkingaLossofNormalHyperbolicityoftheInterpola.md
generated_at: 2026-08-17 21:43
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the sharp generalization transition observed in grokking is caused by a loss of normal hyperbolicity on the interpolation manifold or remains smooth. By analyzing the smallest nonzero singular value of the residual Jacobian, it finds that this value stays near zero only before memorization and reaches its largest values during the transition, indicating no collapse.

## Key Takeaways
- σ_min+ does not collapse at the transition; it is near zero only before memorization and attains its largest values during the transition.  
- The six smallest singular values behave identically across five seeds, showing consistent dynamics.  
- No subspace‑local collapse is observed, supporting a smooth contraction picture rather than a bifurcation event.

## Context
Understanding grokking involves studying how neural networks move from exact memorization to generalization. This work provides an optimizer‑agnostic diagnostic that clarifies the nature of this transition, contributing to broader theories of manifold dynamics in deep learning.

## Implications
For practitioners, the findings suggest that training dynamics are generally smooth and not driven by pathological bifurcations, which can inform regularization strategies and optimizer choices for robust generalization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14803v1)
