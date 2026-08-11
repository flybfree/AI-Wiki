---
title: Fourier Self-Supervision for Fine-Grained Generalized Category Discovery
published: 2026-08-09T23:54:22Z
authors: Sarah Rastegar, Mina Ghadimi Atigh, Pascal Mettes, Yuki M. Asano, Cees G. M. Snoek
url: http://arxiv.org/abs/2608.08963v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fourier Self-Supervision for Fine-Grained Generalized Category Discovery

## Abstract
Generalized Category Discovery aims to recognize known categories while identifying novel ones within unlabeled data. Existing methods, typically based on self-supervision and contrastive learning, often struggle to capture fine-grained distinctions, relying on superficial visual cues rather than the intrinsic attributes humans use for categorization. We introduce Fourier Self-Supervision, that leverages the Fourier transform of images to enhance the discrimination of subtle differences and support the discovery of new categories. Our method employs a dual frequency filtering strategy: a low-pass filter first extracts broad, abstract attributes that capture high-level category information, while a high-pass filter emphasizes fine details such as edges and textures that are essential for fine-grained recognition. Each operates on a dedicated latent space, and their overlapping representations together yield a richer, more complete feature space. This dual-frequency approach not only refines feature extraction to identify novel categories, but also strengthens the model's discriminative power in fine-grained category discovery. Experiments on multiple fine-grained datasets show that incorporating Fourier Self-Supervision outperforms state-of-the-art methods, even when the number of classes is unknown, demonstrating its effectiveness for Generalized Category Discovery. Our code is available at: https://github.com/SarahRastegar/FourEx.

## Metadata
- **Published**: 2026-08-09T23:54:22Z
- **Authors**: Sarah Rastegar, Mina Ghadimi Atigh, Pascal Mettes, Yuki M. Asano, Cees G. M. Snoek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08963v1)