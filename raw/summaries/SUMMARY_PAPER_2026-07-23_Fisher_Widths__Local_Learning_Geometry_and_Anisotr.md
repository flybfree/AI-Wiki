---
title: Fisher Widths: Local Learning Geometry and Anisotropic Recovery
url: http://arxiv.org/abs/2607.20578v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_10-07-03Z_FisherWidths_LocalLearningGeometryandAnisotropicRe.md
generated_at: 2026-07-23 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates Gaussian-width complexity on statistical manifolds using Fisher width and its inverse counterpart, showing how these functionals capture local geometry in learning and recovery. It proves that the Fisher width scales as w_G(H_r)/√n for small balls and derives a two-sided estimate linking it to sparse recovery geometry. A sharp inequality w_G(T)w_{G^{-1}}(T)≥w(T)^2 is established, showing anisotropy cannot reduce both widths simultaneously.

## Key Takeaways
- The Fisher width measures local parameter fluctuations in the Fisher metric and attains its asymptotic scale on sufficiently small balls.
- Inverse-Fisher width reveals anisotropic Gaussian measurements, with statistical dimension depending on sparsity and active coordinate positions within the Fisher spectrum.
- A universal inequality relates both widths to Euclidean width, indicating anisotropy transfers complexity but cannot reduce both.

## Context
Statistical manifold learning is central to deep generative models where data lie on curved spaces. Understanding intrinsic dimensions via width functions guides model capacity and inference efficiency. This work bridges geometry theory with practical recovery tasks in compressed sensing.

## Implications
For practitioners, the results provide precise scaling laws for training stability and support-sensitive reconstruction. They inform algorithm design that respects curvature to avoid overfitting or underrecovery, especially in high-dimensional data where Fisher information dominates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20578v1)
