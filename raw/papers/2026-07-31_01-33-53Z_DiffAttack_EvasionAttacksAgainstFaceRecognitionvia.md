---
title: DiffAttack: Evasion Attacks Against Face Recognition via Latent Diffusion Models
published: 2026-07-31T01:33:53Z
authors: Omid Ahmadieh, Nima Karimian
url: http://arxiv.org/abs/2607.28936v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DiffAttack: Evasion Attacks Against Face Recognition via Latent Diffusion Models

## Abstract
Facial biometric identification relies on the distinctiveness of user attributes within a high-dimensional embedding space. However, the decision boundaries of deep face recognition (FR) systems are often sufficiently narrow that they can be conflated, rendering the models vulnerable to adversarial attacks. In such scenarios, the FR system fails to distinguish between an authentic source and a meticulously crafted adversarial face. Existing adversarial methods targeting facial biometrics are limited in both performance and their ability to generate high-quality images that are imperceptible to humans. Moreover, these methods often fail when the source and target images belong to different demographic groups or genders. To address these limitations, we present a novel approach for adversarial face generation via latent-space optimization. We leverage latent diffusion models directly to guide generation toward target identity embeddings, as measured by a face recognition model. Our proposed \textbf{DiffAttack} framework has been evaluated on standard benchmarks, such as the FFHQ and CelebA-HQ datasets. DiffAttack significantly outperforms existing adversarial techniques, achieving a high average attack success rate of 84.86% across multiple face recognition models (e.g., FaceNet). Notably, DiffAttack demonstrates superior transferability, surpassing traditional noise-based methods by over 15.28% and semantic-based approaches by approximately 5.21% on benchmark datasets like FFHQ and CelebA-HQ.

## Metadata
- **Published**: 2026-07-31T01:33:53Z
- **Authors**: Omid Ahmadieh, Nima Karimian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28936v1)