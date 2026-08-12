---
title: Iterative Erasure Count Is Not an Affine-Invariant Concept Dimension
url: http://arxiv.org/abs/2608.10566v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_06-53-50Z_IterativeErasureCountIsNotanAffine_InvariantConcep.md
generated_at: 2026-08-11 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the number of directions a neural representation uses to encode a concept is an intrinsic property or depends on how we measure it. The authors show that both the stopping count and cumulative Euclidean erasure rank can change under invertible reparameterizations, indicating they are not affine‑invariant concepts. They differentiate model‑defined population dimensions from procedure‑dependent counts and demonstrate this separation with Gaussian constructions and various optimization procedures.

## Key Takeaways
- The stopping count of erased probe directions is a procedure‑relative quantity that varies with the chosen reparameterization rather than reflecting an intrinsic concept dimension.
- Cumulative Euclidean erasure rank can shift from one to two under invertible shears, showing it is not a stable semantic metric across model geometries.
- Affine‑equivariant cumulative metrics exist only when probe, regularizer, and tie‑breaking are transported together; exact covariance is a corollary, not the canonical measure.

## Context
Understanding concept dimensions in neural representations is crucial for interpretability and alignment with human perception. This work clarifies that many reported dimensions are artifacts of measurement procedures, influencing both research and practical applications.

## Implications
For practitioners relying on iterative erasure counts to gauge model complexity, this paper warns against treating them as reliable proxies for true dimensionality. Instead, they should consider the full measurement pipeline and its effect on results.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10566v1)
