---
title: Dual Inversion for Text-to-Image Diffusion Models: From Both Prompt and Noise Perspectives
published: 2026-07-29T10:29:07Z
authors: Xiaolong Liu, Junjian Li, Yuan Xiao, Jiaqi Deng, Dayong Ye, Tianqing Zhu, Huan Huo
url: http://arxiv.org/abs/2607.26735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dual Inversion for Text-to-Image Diffusion Models: From Both Prompt and Noise Perspectives

## Abstract
Prompt inversion, as a typical reverse engineering technique, enables text-to-image (T2I) diffusion models to generate the desired target images without extensive prompt engineering. However, existing prompt inversion methods suffer from significant limitations: (1) gradient-based methods are unstable and uninterpretable, often resulting in generated images with severe artifacts; (2) gradient-free methods yield human-readable prompts but still fail to preserve visual fidelity due to the lack of fine-grained detail alignment. We contend that the limitations stem from treating prompt inversion as a sufficient condition for reverse engineering, ignoring the critical role of the latent noise that encodes structural information. Consequently, we propose Dualin (Dual inversion), a two-stage method that jointly recovers both the semantic prompt and latent noise of the target image. In the first stage, we integrate vision-language model, CLIP and large language model to invert a faithful, human-interpretable hard prompt. In the second stage, unconditional DDIM inversion reconstructs the exact latent noise of the target image, guaranteeing the consistency at the structural information level. Theoretically, we prove that the inverted noise enables flexible image editing without re-optimization. Extensive experiments on diverse datasets demonstrate that Dualin simultaneously generates high-quality inverted prompts and achieves state-of-the-art image fidelity. Additionally, Dualin can establish a robust foundation for the precise and controllable image editing.

## Metadata
- **Published**: 2026-07-29T10:29:07Z
- **Authors**: Xiaolong Liu, Junjian Li, Yuan Xiao, Jiaqi Deng, Dayong Ye, Tianqing Zhu, Huan Huo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26735v1)