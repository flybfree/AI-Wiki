---
title: NSMA: Neuro-Symbolic Manifold Alignment for Generalizable Adaptive Bitrate Streaming under Texture Shift
published: 2026-07-21T08:30:54Z
authors: Zhiqiang He, Zhi Liu
url: http://arxiv.org/abs/2607.18845v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NSMA: Neuro-Symbolic Manifold Alignment for Generalizable Adaptive Bitrate Streaming under Texture Shift

## Abstract
For decades, ABR has kept two kinds of intelligence apart. Neural policies learn rich behaviors yet forget them the moment the environment changes; rules never learn, and never forget. Every prior attempt to combine them has kept this separation, letting rules supervise, constrain, or override the network from outside. We dissolve the boundary itself. But no union can be trusted before it can be tested, and ABR has never known how to measure what its policies learn or forget. The field's yardstick is bandwidth statistics, and we show it misleads. Identical statistics can hide entirely different outcomes, while wildly different statistics can hide similar ones. We replace the yardstick before building the bridge, with Texture-Aware Generalization Evaluation, a protocol that judges a policy by its whole training journey across traces whose temporal nature is laid bare. What truly breaks a policy is invisible. No statistic reveals it, no feature extracts it, yet rules walk through it untouched, for they reason from physics and owe the data nothing. So we build the bridge. Neuro-Symbolic Manifold Alignment (NSMA) embeds rule decisions as anchors inside the latent space of the neural policy, so that it keeps learning where learning pays, and can no longer forget what rules have always known. Generalization cannot be argued, only survived. We raise NSMA on 3G traces alone and release it, without fine-tuning, into eight unseen datasets spanning 4G, 5G, and WiFi, and onto a real-world player. It outperforms every state-of-the-art baseline. And when we open its latent space to ask why, probing and visualization return the same answer the design promised. https://tinyzqh.github.io/NSMA/

## Metadata
- **Published**: 2026-07-21T08:30:54Z
- **Authors**: Zhiqiang He, Zhi Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18845v1)