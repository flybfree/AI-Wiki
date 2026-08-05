---
title: Tight Worst-Case Bounds for the Smallest Eigenvalue of ReLU NTK Gram Matrices
url: http://arxiv.org/abs/2608.03368v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_09-19-53Z_TightWorst_CaseBoundsfortheSmallestEigenvalueofReL.md
generated_at: 2026-08-05 01:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper establishes a tight worst‑case bound for the smallest eigenvalue of a continuous ReLU NTK Gram matrix built from n unit vectors in R^d. It shows that the minimum eigenvalue scales with the projective separation Δ_± divided by sqrt(log n) and that this rate cannot be improved.

## Key Takeaways
- The lower bound λ_min(H)=Ω(Δ_±/√log n) holds for any configuration of unit vectors, independent of dimension d.
- A matching upper bound λ_min(H)=O(Δ_±/√log n) is achieved by specific worst‑case families of vectors.
- Together these results prove that the √log n factor in the denominator is optimal up to universal constants.

## Context
In deep learning, NTK Gram matrices appear as second‑order approximations for training dynamics and are crucial for understanding optimization stability. This work provides a dimension‑free analysis that bridges geometry of data points with algorithmic behavior without relying on d.

## Implications
The tight bound informs practitioners about the limits of eigenvalue shrinkage in ReLU networks, guiding regularization strategies and model design to avoid pathological configurations. It also offers theoretical justification for using projection metrics like Δ_± when assessing network robustness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03368v1)
