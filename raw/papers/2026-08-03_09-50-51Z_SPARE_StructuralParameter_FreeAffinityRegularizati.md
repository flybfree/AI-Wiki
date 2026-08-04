---
title: SPARE: Structural Parameter-Free Affinity Regularization for Flow Matching
published: 2026-08-03T09:50:51Z
authors: Zong-Wei Hong, Jinglun Li, Shen Zhang, Yuhan Liu, Linze Li, Yao Tang
url: http://arxiv.org/abs/2608.01990v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPARE: Structural Parameter-Free Affinity Regularization for Flow Matching

## Abstract
Denoising diffusion transformers achieve strong generation quality but converge slowly during training. Regularizing their internal representations has emerged as an effective accelerator, yet existing methods split into two families with complementary costs. Target-based methods strengthen representations by aligning them to external features, which requires an external encoder and a learnable projection head to bridge feature spaces. Target-free methods hold no reference at all, and can only repel the model's own features across samples or layers, discarding whatever structure the data contains. Prior work suggests that spatial structure, rather than global semantics, drives the gains of alignment. We therefore ask whether such structure can serve as a target directly, and whether it exists not only within an image but across images. Our key insight is that the clean data latent already carries this structure in the relations among its tokens, where a relation is the similarity between two tokens, a single scalar comparable across feature spaces without a projection head. We propose Structural Parameter-free Affinity Regularization (SPARE), a regularizer that matches the pairwise affinities of intermediate tokens to those of the clean latents. To exploit this structure fully, SPARE extends the matching to token pairs across images, precisely the pairs that prior target-free methods repel by default, and calibrates both relation types with a single learning objective. On ImageNet $256 \times 256$ with SiT backbones under matched 400K-iteration budgets, SPARE adds no encoder, head, or parameters and only 0.08 GB of training memory, yet attains the lowest FID among parameter-free regularizers in every tested setting, recovers 37 to 54\% of REPA's FID reduction, and improves over REPA when combined with it, reaching FID 1.90 under classifier-free guidance at 1M iterations.

## Metadata
- **Published**: 2026-08-03T09:50:51Z
- **Authors**: Zong-Wei Hong, Jinglun Li, Shen Zhang, Yuhan Liu, Linze Li, Yao Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01990v1)