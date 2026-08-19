---
title: CORAM: Coherent Orthogonal Rotation for Model Merging
url: http://arxiv.org/abs/2608.17366v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_04-44-24Z_CORAM_CoherentOrthogonalRotationforModelMerging.md
generated_at: 2026-08-18 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CORAM, a method for merging finetuned models using orthogonal transformations that preserve singular values while allowing manifold averaging to contract updates. It improves over OrthoMerge by up to 1.35 points across diverse suites and scales from 3B to 9B parameters in language and vision-language tasks.

## Key Takeaways
- CORAM partitions each target matrix into row slices, representing expert slices with their singular value decompositions aligned to the base-model SVD frame.
- The merging update is amplified by a coefficient λ = κ \hat{c}, where c_hat ≈ √N for N experts and kappa is chosen from the dispersion of expert updates without evaluating merged models.
- Spread slicing distributes highly updated rows across slices, and a residual pathway handles non-target layers.

## Context
Model merging is essential for combining specialized capabilities in large language and vision-language systems without retraining on original data. Existing Euclidean-based approaches ignore geometric constraints, limiting performance.

## Implications
CORAM’s manifold-aware merging can be integrated into production pipelines to enhance model fusion efficiency across diverse architectures. Practitioners benefit from higher accuracy gains with minimal computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17366v1)
