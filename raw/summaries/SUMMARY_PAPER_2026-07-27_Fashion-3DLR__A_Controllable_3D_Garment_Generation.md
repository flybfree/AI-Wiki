---
title: Fashion-3DLR: A Controllable 3D Garment Generation Using Pairwise Fashion Elements for Intelligent Design
url: http://arxiv.org/abs/2607.23189v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_13-10-38Z_Fashion_3DLR_AControllable3DGarmentGenerationUsing.md
generated_at: 2026-07-27 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
Fashion-3DLR is a framework that generates high-quality 3D garments from diverse design elements by fusing 2D sketches and textures into latent space using a Garment Feature Fusion Diffusion Transformer. It then uses rectified flow transformer to produce geometry latents decoded as 3D Gaussians or meshes, enabling physical simulation via 3D Gaussian Splatting and virtual try‑on.

## Key Takeaways
- The GFF-DiT module bridges semantic gaps between 2D fashion elements like sketch and texture by integrating them into a shared latent space.
- A rectified flow transformer converts this fused representation into geometry latents that can be rendered as watertight or non‑watertight 3D garment models such as meshes or Gaussians.
- The method enables downstream tasks including cloth physical simulation with 3D Gaussian Splatting and mesh‑based virtual try‑on, demonstrating versatility beyond simple generation.

## Context
Current AI research focuses on 2D generative models for fashion, yet 3D garment creation remains limited by the complex coupling of design elements in three dimensions. Fashion-3DLR addresses this gap by providing a unified pipeline that respects semantic relationships across elements and produces usable 3D assets.

## Implications
This work opens new possibilities for designers to create realistic 3D garments quickly, supporting virtual fitting rooms and physical prototyping without manual modeling. It also reduces the need for separate pipelines for simulation and rendering, streamlining production workflows in fashion e‑commerce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23189v1)
