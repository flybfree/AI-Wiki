---
title: PIXLRelight: Controllable Relighting via Intrinsic Conditioning
url: http://arxiv.org/abs/2605.18735v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-18_17-55-03Z_PIXLRelight_ControllableRelightingviaIntrinsicCond.md
generated_at: 2026-06-11 10:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
PIXLRelight introduces a feed‑forward method for controllable single‑image relighting that uses intrinsic conditioning derived from either real photos or PBR renders. The approach avoids chaining errors and costly per‑image optimization, achieving high quality under sub‑tenth‑second inference.

## Key Takeaways
- The model decomposes paired multi‑illumination photographs into albedo, diffuse shading, and non‑diffuse residuals to condition the network.  
- At inference, a coarse 3D reconstruction is rendered with user‑specified PBR lights, producing conditioning that matches the target illumination.  
- A transformer‑based renderer applies the lighting via per‑pixel affine modulation, preserving fine image detail.

## Context
Controllable relighting remains challenging due to the need for accurate scene understanding and efficient inference. This work advances AI rendering by integrating physics‑based PBR with learned synthesis in a unified conditioning framework.

## Implications
Practitioners can now generate realistic lighting variations from photographs without complex 3D pipelines, opening possibilities for real‑time applications such as virtual production and augmented reality. The sub‑tenth‑second runtime makes the method suitable for interactive use cases across industry and research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.18735v1)
