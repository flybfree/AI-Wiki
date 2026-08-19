---
title: A Constant-Competitive Algorithm for Dynamic Mixture-of-Experts Serving
published: 2026-08-15T03:51:27Z
authors: Ian D'Ambrosio
url: http://arxiv.org/abs/2608.16947v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Constant-Competitive Algorithm for Dynamic Mixture-of-Experts Serving

## Abstract
Huang, Lou, and Xiao introduced Dynamic Mixture-of-Experts Serving and gave an O(sqrt(log k))-competitive randomized algorithm for its integral primal problem, where k is the number of replica GPUs beyond the mandatory copy of each expert. Their matching lower barrier applies to an auxiliary dual and leaves the primal order open. We prove that the randomized primal competitive ratio is in fact Theta(1) for arbitrary numbers of experts. The upper bound reduces reciprocal-max service costs to chasing positive bodies with covering row sparsity two. A finite tangent envelope approximates each reciprocal epigraph within a constant factor, summable positive resets convert accumulated service into movement, and a nonexpansive balanced projection removes the positive-body algorithm's resource augmentation. Combining the resulting fractional path with Lazy Threshold Rounding gives   E[ALG] <= 10 C_PB OPT + (5 C_PB + 2) k + 16,   where C_PB is the absolute constant from Chasing Positive Bodies at resource augmentation one and covering sparsity two. The full reduction, rounding composition, and quantified main theorem are machine-checked in Lean 4 relative to exact formal interfaces for the two cited source theorems. Deterministic rational controls and a fresh independent replay accompany the formal proof.

## Metadata
- **Published**: 2026-08-15T03:51:27Z
- **Authors**: Ian D'Ambrosio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16947v1)