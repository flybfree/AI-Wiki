---
title: Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models via Representation-Space Bridging
published: 2026-08-04T08:23:57Z
authors: Siming Fu, Zheming Fu, Ruizhe He, Hualiang Wang, Jie Huang, Xiaoxiao Ma, Mingchen Zhong, Weihu Huang, Xiaoxuan He, Haojun Xu
url: http://arxiv.org/abs/2608.03316v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models via Representation-Space Bridging

## Abstract
On-policy distillation, in which a teacher corrects samples that the student itself generates, presupposes that the two models speak the same language: identical VAE latents, matching architectures, and a common timestep grid. We ask what happens when none of this holds, as when the strongest teacher available and the student one wishes to deploy come from different model families, and find that the standard recipes have no answer: teacher latents cannot serve as targets in a foreign coordinate system, per-pixel losses against a teacher that stochastically re-draws local detail degenerate into blur or divergence, and timestep indices lose their meaning across mismatched schedules. We present Any-OPD, to our knowledge the first framework for on-policy distillation between arbitrary pairs of latent flow-matching generators. Any-OPD treats the teacher purely as a black-box sampler and connects the two models at exactly one point: a frozen, model-agnostic vision representation in which their independently decoded outputs are compared, sidestepping every assumption about latents, features, or architecture. Trajectory correspondence is recovered by matching continuous noise levels instead of step indices, and a brief anchoring phase, in which teacher samples are re-encoded through the student's own VAE, ensures the on-policy gradient measures sample quality rather than domain mismatch. Distilling the 12B FLUX.1-dev into the 2.5B SD3.5-Medium, Any-OPD lifts the student's PickScore from 0.846 to 0.884 and HPSv3 from 9.12 to 10.97, rivaling the teacher at a fifth of its size, where direct latent regression fails to train at all.

## Metadata
- **Published**: 2026-08-04T08:23:57Z
- **Authors**: Siming Fu, Zheming Fu, Ruizhe He, Hualiang Wang, Jie Huang, Xiaoxiao Ma, Mingchen Zhong, Weihu Huang, Xiaoxuan He, Haojun Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03316v1)