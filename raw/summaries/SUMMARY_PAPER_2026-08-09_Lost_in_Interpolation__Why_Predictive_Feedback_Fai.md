---
title: Lost in Interpolation: Why Predictive Feedback Fails in Diffusion Language Models
url: http://arxiv.org/abs/2608.06529v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_19-23-32Z_LostinInterpolation_WhyPredictiveFeedbackFailsinDi.md
generated_at: 2026-08-09 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why linear interpolation (LERP) fails in Masked Diffusion Language Models and proposes Spherical Soft‑Masking using spherical linear interpolation. It shows that embeddings lie on a hypersphere with constant angle, causing LERP to degrade performance. S-SM improves generation quality and perplexity.

## Key Takeaways
- The embedding space of MDLMs exhibits a near‑constant angle (~73°) between mask and predicted tokens, indicating a hyperspherical geometry where Euclidean LERP is inappropriate.
- Norms stay flat across vocabulary‑frequency rank, reinforcing the spherical nature and making linear blending ineffective.
- Spherical Soft‑Masking replaces LERP with SLERP on the Fr'echet mean of top‑k predictions, preserving native mask norm and delivering up to 2× MAUVE gains.

## Context
Diffusion language models rely on soft‑masking to accelerate training, but current implementations assume Euclidean interpolation. This assumption can mislead convergence when embeddings adopt non‑Euclidean structures, limiting the effectiveness of popular training tricks.

## Implications
Practitioners should adopt spherical interpolation techniques for any model whose embeddings exhibit hyperspherical properties. Adopting S-SM could unlock higher quality generation and faster convergence without sacrificing entropy or speed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06529v1)
