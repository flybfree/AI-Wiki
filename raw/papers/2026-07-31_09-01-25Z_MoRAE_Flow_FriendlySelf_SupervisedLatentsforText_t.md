---
title: MoRAE: Flow-Friendly Self-Supervised Latents for Text-to-Motion Generation
published: 2026-07-31T09:01:25Z
authors: Yifei Zhu, Mingyi Shi, Yangyang Cai, Miao Cheng, Yoshifumi Kitamura, Taku Komura
url: http://arxiv.org/abs/2607.29180v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoRAE: Flow-Friendly Self-Supervised Latents for Text-to-Motion Generation

## Abstract
Text-to-motion generation must produce motions that are semantically correct, temporally coherent, and physically plausible. A natural approach is to first project motion data into a structured semantic space and then train a generative model within that space. Such a paradigm has been highly successful in image generation through Representation Autoencoders (RAEs), where a frozen self-supervised encoder provides semantic features for diffusion or flow models to learn from. However, direct transfer of such a paradigm to motion space using Motion-JEPA as the frozen encoder fails dramatically. We diagnose this failure geometrically and identify two motion-specific bottlenecks: (1) the JEPA feature space is spectrally ill-conditioned, making the Gaussian-to-data transport unstable; and (2) even with a well-conditioned spectrum, flow residuals tend to align with decoder-sensitive directions, where small latent errors are amplified into large motion artifacts after decoding. Based on these insights, we propose MoRAE. MoRAE addresses the two bottlenecks separately. A compact bottleneck distills the structured JEPA representation while removing weak and redundant directions, bringing the latent spectrum into a transport-stable regime. Motion-coupled training then aligns the retained latent geometry with the decoder, making characteristic flow errors less costly after decoding. With this flow-friendly latent, a standard non-autoregressive Flow-Matching DiT achieves state-of-the-art performance.

## Metadata
- **Published**: 2026-07-31T09:01:25Z
- **Authors**: Yifei Zhu, Mingyi Shi, Yangyang Cai, Miao Cheng, Yoshifumi Kitamura, Taku Komura
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29180v1)