---
title: Rectify Then Diffuse: Disentangling Concepts Before Denoising Trajectory Unfolds
url: http://arxiv.org/abs/2608.03135v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_05-03-17Z_RectifyThenDiffuse_DisentanglingConceptsBeforeDeno.md
generated_at: 2026-08-05 01:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Rectify‑then‑Diffuse (RTD), a training‑free method that improves compositional generation in diffusion models by fixing concept allocation before denoising begins. The authors show that RTD boosts factual consistency and speed on benchmark tasks, outperforming previous approaches.

## Key Takeaways
- Soft‑Overlap Disentanglement converts normalized overlap between pilot concept maps into a differentiable separation objective, allowing the model to split concepts even when their spatial supports overlap.
- Isotropic Gradient Rectification normalizes this gradient and applies a bounded latent displacement with a consistent scale across all prompts, preventing unwanted drift during diffusion.
- Extensive experiments demonstrate that RTD achieves state‑of‑the‑art compositional fidelity on AE‑Bench object pairs while running 2.3 times faster than baseline models.

## Context
Diffusion models excel at generating individual concepts but struggle when multiple concepts must coexist in a single image, leading to merged or omitted elements. This paper addresses the early coordination bottleneck that arises from prompt‑conditioned attention allocating overlapping spatial support, highlighting a need for explicit boundary conditions rather than continuous control.

## Implications
The RTD framework offers practitioners a simple, training‑free way to enhance compositional quality without sacrificing speed, which is crucial for real‑world applications where both fidelity and efficiency matter. By decoupling concept separation from the diffusion process, it paves the way for more reliable and scalable generative systems in image synthesis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03135v1)
