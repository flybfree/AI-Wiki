---
title: UDT: Reconciling U-Nets and Diffusion Transformers with Data-Adaptive Token Reduction
url: http://arxiv.org/abs/2608.01298v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_15-07-21Z_UDT_ReconcilingU_NetsandDiffusionTransformerswithD.md
generated_at: 2026-08-03 23:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces UDT, a unified architecture that merges the representation depth of diffusion Transformers with the encoder‑decoder flexibility of U‑Nets through data‑adaptive token merging. Experiments show that UDT surpasses existing U‑Net DiT models and matches REPA’s performance across all sizes while achieving up to 40× faster convergence on large models, delivering FID scores as low as 1.35 with VA‑VAE.

## Key Takeaways
- UDT replaces standard spatial downsampling operators with token merging that adapts to image content, preserving the DiT token dimension and improving representation balance.
- The architecture outperforms both REPA and SiT on ImageNet‑256 tasks, achieving FID 1.38 with SD‑VAE in 320 epochs and 1.35 with VA‑VAE in 500 epochs.
- UDT’s data‑adaptive merging enables faster convergence to high‑quality generations without sacrificing the transformer’s progressive depth.

## Context
Diffusion Transformers dominate generative modeling due to their scalability, yet their encoder‑decoder imbalance hampers efficiency and performance. Existing solutions either rely on fixed token reduction or introduce U‑Net‑style bottlenecks that clash with transformer components, limiting both speed and quality.

## Implications
UDT provides a practical backbone for diffusion Transformers, offering practitioners a path to faster training and higher fidelity images without sacrificing the model’s representational power. This opens new avenues for real‑time generation and large‑scale deployment in industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01298v1)
