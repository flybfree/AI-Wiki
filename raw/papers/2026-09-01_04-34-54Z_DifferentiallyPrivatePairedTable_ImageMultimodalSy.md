---
title: Differentially Private Paired Table-Image Multimodal Synthesis
published: 2026-09-01T04:34:54Z
authors: Kai Chen, Josephine Lamp, Somesh Jha, Tianhao Wang
url: http://arxiv.org/abs/2609.00708v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Differentially Private Paired Table-Image Multimodal Synthesis

## Abstract
Differentially private (DP) synthesis has been extensively studied for tabular and image data separately, yet many real-world datasets contain images paired with multivariate tabular records. Synthesizing such data is particularly challenging under DP, as the two modalities favor different private learning mechanisms while their dependence must also be preserved. To address this challenge, we propose DP-TabImage, a modality-specialized framework for private paired synthesis. DP-TabImage instantiates the factorization $p(x,y)=p_T(y)p_I(x\;|\;y)$ using a private Probabilistic Graphical Model for the multivariate table distribution and a table-conditioned diffusion model trained with DP-SGD for the conditional image distribution. To facilitate conditional learning under clipped and noisy gradients, we further pretrain the model on private table-image prototypes, pairing privately constructed attribute-conditioned images with tabular vectors derived from the already private tabular model at no additional privacy cost. Experiments on three real-world datasets show that DP-TabImage achieves a strong balance among tabular fidelity, image fidelity, and cross-modal alignment. Our analysis further reveals that visual warm-up primarily improves marginal image fidelity, whereas aligned table-image warm-up is critical for improving cross-modal correspondence. Our source code is available in the GitHub repository, https://github.com/KaiChen9909/TabImage_Syn.

## Metadata
- **Published**: 2026-09-01T04:34:54Z
- **Authors**: Kai Chen, Josephine Lamp, Somesh Jha, Tianhao Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00708v1)