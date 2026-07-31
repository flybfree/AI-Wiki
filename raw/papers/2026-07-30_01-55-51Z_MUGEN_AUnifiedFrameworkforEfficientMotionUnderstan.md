---
title: MUGEN: A Unified Framework for Efficient Motion Understanding and Generation
published: 2026-07-30T01:55:51Z
authors: Zhankai Ye, Yukai Jin, Bingyang Wei, Bofan Li, Yusen Wu, Fangyi Li, Shangqian Gao, Xin Liu
url: http://arxiv.org/abs/2607.27581v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MUGEN: A Unified Framework for Efficient Motion Understanding and Generation

## Abstract
Grounding human motion in language, and language in motion, is a central step toward physical AI systems that can understand, generate, and communicate human behavior. Unified motion--language systems first coupled the two directions through a shared discrete motion codebook, but quantization limits generation quality. The strongest generators buy quality back at growing cost: stacked residual codebooks enlarge the representation; masked decoding stages, long autoregressive rollouts, and denoising chains of tens to hundreds of steps stretch inference; even the continuous-latent designs among them reach their latent only through an iterative diffusion head; and none of this decoding machinery serves understanding. We therefore propose MUGEN, a unified motion--language framework that pays neither cost: no codebook, one draw. A single adaptive-length autoencoder compresses any-length motion into a few continuous latent slots, the system's only motion representation: the language model generates them for text-to-motion and reads them back for motion understanding. Depth-routed hidden states let each slot read from the transformer depth it needs, and a calibrated head predicts a joint distribution over the full latent set, so a single draw carries the text-conditional, cross-slot variation a description permits. At a decoding cost of K language-model steps, one draw, and one decoder pass, MUGEN leads language-model baselines on FID on HumanML3D while raising retrieval precision above the real-motion reference under the standard evaluator, achieves the best CIDEr and BLEU@4 scores, and surpasses the discrete-token state of the art on every retrieval and alignment metric on SnapMoGen.

## Metadata
- **Published**: 2026-07-30T01:55:51Z
- **Authors**: Zhankai Ye, Yukai Jin, Bingyang Wei, Bofan Li, Yusen Wu, Fangyi Li, Shangqian Gao, Xin Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27581v1)