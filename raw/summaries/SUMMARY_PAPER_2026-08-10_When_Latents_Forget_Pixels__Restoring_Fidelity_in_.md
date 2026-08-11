---
title: When Latents Forget Pixels: Restoring Fidelity in Diffusion Transformer Super-Resolution
url: http://arxiv.org/abs/2608.09133v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_05-24-39Z_WhenLatentsForgetPixels_RestoringFidelityinDiffusi.md
generated_at: 2026-08-10 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of maintaining pixel fidelity in diffusion transformer super-resolution by revisiting how latent representations affect image quality. The authors introduce a pixel-grounded framework that preserves low‑resolution evidence before VAE compression and reuses it to guide both the restoration trajectory and the final decoder output, resulting in more faithful images than prior methods.

## Key Takeaways
- The VAE bottleneck compresses fine‑grained spatial information, causing hallucinated details that are not anchored to the original low‑resolution image.  
- PGSR extracts pre‑VAE pixel evidence from the upsampled LR image and fuses it with the latent condition on both the conditioning side and the decoding side to retain observed pixels.  
- Only lightweight restoration modules are trained while the frozen VAE autoencoder and main DiT backbone remain unchanged, enabling efficient adaptation of large pretrained models.

## Context
Latent generative super‑resolution has become a standard technique for enhancing image detail, but its reliance on compressed latent spaces often sacrifices fidelity. This work highlights how representation‑level design choices can degrade the alignment between generated content and observed pixels, a concern that resonates across vision generation research.

## Implications
For practitioners developing large diffusion models, PGSR offers a practical way to preserve visual consistency without retraining massive architectures, reducing computational cost while improving output realism. The approach may inspire future work on hybrid encoder‑decoder pipelines where observation evidence is explicitly integrated throughout the generative process.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09133v1)
