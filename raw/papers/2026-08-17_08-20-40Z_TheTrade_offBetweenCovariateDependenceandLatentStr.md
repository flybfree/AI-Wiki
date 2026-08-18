---
title: The Trade-off Between Covariate Dependence and Latent Structure in Representation Learning
published: 2026-08-17T08:20:40Z
authors: Małgorzata Łazęcka, Ewa Szczurek
url: http://arxiv.org/abs/2608.16245v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Trade-off Between Covariate Dependence and Latent Structure in Representation Learning

## Abstract
Disentangled representation learning seeks latent representations whose indicidual dimensions each align with a distinct covariate. Unsupervised approaches typically target latent dimension independence, yet this gives no guarantee that the resulting dimensions align with semantically meaningful covariates. Supervised approaches structure the latent space using observed covariates, but under correlated covariates they cannot simultaneously control one-to-one latent-covariate alignment and latent independence. We introduce a unified, supervised framework that couples latent dimension-covariate dependence with constraints on the latent structure. Within this framework, we show an inherent trade-off, where enforcing latent independence or exclusive one-to-one latent-covariate dependence comes at a provable cost in latent-covariate alignment. We prove that the resulting disentanglement regimes are ordered by the strength of that alignment. Each regime admits a closed-form transformation of the latent space. We apply these transformations post-hoc to realign the representations of pretrained models such as CLIP, DINOv2, and ViT, and we fold them into the inference of informed factor analysis (iFA), a probabilistic model with covariate-informed factors. On simulated and real multi-omics data, we show that both post-hoc alignment and iFA enable controllability of structured latent representations.

## Metadata
- **Published**: 2026-08-17T08:20:40Z
- **Authors**: Małgorzata Łazęcka, Ewa Szczurek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16245v1)