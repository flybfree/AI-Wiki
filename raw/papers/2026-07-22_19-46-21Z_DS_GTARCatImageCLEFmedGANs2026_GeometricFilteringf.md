---
title: DS@GT ARC at ImageCLEFmed GANs 2026: Geometric Filtering for Privacy-Preserving CT Slice Generation
published: 2026-07-22T19:46:21Z
authors: Eric Regina, Richard Arnaud, Samir Hadi Cisneros
url: http://arxiv.org/abs/2607.20692v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DS@GT ARC at ImageCLEFmed GANs 2026: Geometric Filtering for Privacy-Preserving CT Slice Generation

## Abstract
We present a privacy-preserving framework for synthetic lung CT slice generation developed for the Image-CLEFmed GANs 2026 challenge. The approach combines Optimal Transport Conditional Flow Matching with privacy-oriented training and a post-generation "Supervisor" pipeline that filters generated candidates in learned geometric latent spaces using autoencoder embeddings, Determinantal Point Processes, and Stein Kernel Thinning. Official results show a strong realism-privacy trade-off, with the best-performing model achieving a Privacy Preservation Score of 0.549 and competitive visual fidelity with an FID of 0.3290. While the proposed geometric filtering substantially reduces nearest-neighbor memorization and membership-inference leakage, persistent patient re-identification scores indicate that preventing direct image copying is not sufficient to remove deeper patient-specific anatomical identity, highlighting an important frontier for future privacy-preserving medical image generation.

## Metadata
- **Published**: 2026-07-22T19:46:21Z
- **Authors**: Eric Regina, Richard Arnaud, Samir Hadi Cisneros
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20692v1)