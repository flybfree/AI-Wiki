---
title: UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction
published: 2026-08-03T12:31:12Z
authors: Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan
url: http://arxiv.org/abs/2608.02145v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UniqueSplat: View-conditioned 3D Gaussian Splatting for Generalizable 3D Reconstruction

## Abstract
In this paper, we propose UniqueSplat, a view-conditioned feed-forward 3D Gaussian Splatting model to reconstruct customized 3D radiance fields for each view query. Existing feed-forward methods such as pixelSplat and MVSplat aim to generate fixed Gaussians across all views of each scene by minimizing the error between rendered views and ground-truth images. However, such fixed Gaussians generally render images from all views and lack the ability to adapt to specific viewpoints, as they do not incorporate target view information when predicting Gaussians. To address this, our UniqueSplat learns the view-conditioned information as a prior and incorporates this knowledge into network parameters, so that Gaussians are dynamically adjusted in accordance with different views. Specifically, we propose a two-branch view-conditioned hyperNetwork to simultaneously learn view-agnostic embeddings and view-specific knowledge, which not only explores the shareable knowledge from various views, but also adapts the model to specific views at test time. Extensive experiments on widely-used datasets including RealEstate10K, ACID and DTU demonstrate the superiority of UniqueSplat over the state-of-the-art methods. Moreover, UniqueSplat encouragingly outperforms existing methods in cross-dataset evaluation, showing its notable generalization ability.

## Metadata
- **Published**: 2026-08-03T12:31:12Z
- **Authors**: Haixu Song, Xiaoke Yang, Shengjun Zhang, Jiwen Lu, Yueqi Duan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02145v1)