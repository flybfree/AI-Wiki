---
title: When Latents Forget Pixels: Restoring Fidelity in Diffusion Transformer Super-Resolution
published: 2026-08-10T05:24:39Z
authors: Yu Shi, Yuyao Zhang, Yu-wing Tai
url: http://arxiv.org/abs/2608.09133v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Latents Forget Pixels: Restoring Fidelity in Diffusion Transformer Super-Resolution

## Abstract
Image super-resolution (SR) with large generative models has recently achieved remarkable perceptual quality, yet maintaining fidelity to the LR observation remains challenging. In particular, we observe that diffusion transformers (DiTs) built on latent representations suffer from a critical limitation: the compression bottleneck of the VAE weakens fine-grained spatial information, leading to hallucinated details that are weakly grounded in the input image. In this work, we revisit generative SR from a representation perspective and propose a pixel-grounded super-resolution (PGSR) framework that preserves LR-observed pixel evidence before VAE compression and reuses it throughout restoration. Instead of relying solely on the compressed latent condition, PGSR extracts pre-VAE pixel evidence from the upsampled LR image and reuses it at two stages. First, Condition-Side Trajectory Guidance fuses LR-derived pixel evidence with the latent LR condition to guide the latent restoration trajectory. Second, Decoder-Side Pixel Grounding injects multi-scale pixel features into the frozen VAE decoder to ground the final rendering with LR-observed cues. To efficiently adapt large pretrained DiT models, we keep the latent autoencoder and main flow-matching backbone frozen, and train only lightweight restoration modules. We further study an efficient local-window attention variant for improved high-resolution efficiency and scalability. Extensive experiments demonstrate that PGSR improves the realism--fidelity trade-off and produces more faithful, visually convincing results than existing latent generative SR approaches.

## Metadata
- **Published**: 2026-08-10T05:24:39Z
- **Authors**: Yu Shi, Yuyao Zhang, Yu-wing Tai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09133v1)