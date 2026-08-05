---
title: Should the Boundary Term Be Learned in Reflected Diffusion? Conormal Trace and Reflection Masking
url: http://arxiv.org/abs/2608.03469v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_11-05-02Z_ShouldtheBoundaryTermBeLearnedinReflectedDiffusion.md
generated_at: 2026-08-05 01:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether the boundary term in reflected diffusion should be learned or fixed, focusing on the conormal trace and reflection masking. It shows that implicit score matching leaves a scalar boundary term that depends on the diffusion-weighted normal component of the score. The authors demonstrate that enforcing this trace correctly is crucial for accurate score representation.

## Key Takeaways
- The conormal trace, a scalar at each boundary point representing the diffusion-weighted normal part of the learned score, must be fixed to satisfy no-flux conditions; leaving other components free leads to errors that cannot be removed by more data.
- On hyperrectangles the parametrization automatically enforces the required trace without extra trainable parameters or stochastic estimators, preserving true scores under regularity assumptions.
- Hard reflection can mask boundary-score mismatches, causing post-reflection metrics to hide errors and decoupling score accuracy from downstream generation quality.

## Context
Score learning for diffusion models on bounded domains is essential because forward processes generate samples that must respect domain constraints. Implicit score matching introduces boundary terms via integration by parts, which are often overlooked in standard implementations. This work addresses the theoretical gap between learned scores and physical boundary behavior.

## Implications
For practitioners developing diffusion samplers with reflection, correctly handling conormal traces ensures sample placement respects domain boundaries, improving realism. Ignoring these terms can lead to artifacts that are invisible until they affect generation quality, highlighting a need for careful model design in AI research and industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03469v1)
