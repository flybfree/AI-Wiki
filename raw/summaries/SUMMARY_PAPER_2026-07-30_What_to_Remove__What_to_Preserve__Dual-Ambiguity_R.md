---
title: What to Remove, What to Preserve: Dual-Ambiguity Rectification for All-in-One Image Restoration
url: http://arxiv.org/abs/2607.28526v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-01-24Z_WhattoRemove_WhattoPreserve_Dual_AmbiguityRectific.md
generated_at: 2026-07-30 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes DAR‑Net, a Dual‑Ambiguity Rectification Network that tackles the intertwined semantic and spatial ambiguities in all‑in‑one image restoration. Experiments on three‑degradation and five‑degradation benchmarks show DAR‑Net outperforms existing methods by 0.14 dB and 0.34 dB PSNR respectively, achieving the best overall performance.

## Key Takeaways  
- The Degradation Archetype Representation (DAR) module constructs a structured degradation state using simplex‑constrained archetype mixture modeling to separate channel‑wise modulation from scene content.  
- The Semantic Ambiguity Rectification (SeAR) module generates degradation‑aware prompts that guide the decoder, enhancing conditioning for accurate restoration.  
- The Spatial Ambiguity Rectification (SpAR) module regularizes features toward orthogonal response subspaces, minimizing spatial interference between removal and preservation cues.

## Context  
All‑in‑one image restoration seeks a unified framework to handle diverse degradations, but existing approaches often let degradation cues and scene content entangle. This dual ambiguity can cause artifacts and degrade quality, limiting the practical utility of such methods in real‑world applications.

## Implications  
Robust restoration across multiple degradations is crucial for industries ranging from medical imaging to satellite data processing. DAR‑Net’s structured decomposition and orthogonal regularization offer a scalable solution that reduces residual artifacts, encouraging broader adoption of unified restoration pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28526v1)
