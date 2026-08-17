---
title: Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs
published: 2026-08-13T15:32:40Z
authors: Dingzhan Nong, Zhihao Ren, Ziqi Li, Tim Lo
url: http://arxiv.org/abs/2608.13368v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs

## Abstract
This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expert branch in the generator toward a distinct visual region, enabling implicit feature specialization without explicit diversity losses. To stabilize this multi-discriminator system, whose early-phase training otherwise exhibits chaotic dynamics, we introduce a United Loss consensus mechanism that regularizes each discriminator toward the ensemble average at a 10% weight. Each branch further adopts a dual-pathway convolutional-transformer design with learnable AdaptiveFeatureFusion, balancing the stability of convolutions against the detail of windowed self-attention. The generator is trained using an alternating three-mode schedule (discriminator, holistic generation, branch-specialized generation). On a custom 156GB dataset with a filtered test set that removes easy and repetitive samples, our 0.2B-parameter variant achieves 29.8 PSNR and the 1.3B-parameter variant achieves 30.7 PSNR, with inference VRAM footprints of 1.5 GB and 8 GB respectively, enabling deployment on consumer-grade hardware. Full ablation studies remain ongoing due to the 2-3 month training cycle on a single GPU. The system was showcased at the 2025 Hong Kong Frontier Technology Summit.

## Metadata
- **Published**: 2026-08-13T15:32:40Z
- **Authors**: Dingzhan Nong, Zhihao Ren, Ziqi Li, Tim Lo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13368v1)