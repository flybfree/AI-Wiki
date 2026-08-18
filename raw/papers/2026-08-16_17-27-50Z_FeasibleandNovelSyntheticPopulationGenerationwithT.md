---
title: Feasible and Novel Synthetic Population Generation with Tabular and Sequential Travel Attributes
published: 2026-08-16T17:27:50Z
authors: Farbod Abbasi, Zachary Patterson, Bilal Farooq
url: http://arxiv.org/abs/2608.15867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Feasible and Novel Synthetic Population Generation with Tabular and Sequential Travel Attributes

## Abstract
Synthetic populations are critical inputs for activity-based travel demand models, yet generating realistic populations from limited survey data remains challenging. Small samples miss valid attribute combinations, known as sampling zeros, and generative models may also produce infeasible structural zeros. Moreover, realistic synthetic populations must capture both static socio-demographic attributes and sequential travel behaviour, such as trip chains. This paper proposes a regularized two-stage generative framework to address these challenges, where regularization refers to additional loss terms that guide the generator toward broader valid coverage and fewer infeasible samples. In Stage 1, a Wasserstein GAN with gradient penalty is augmented with three regularization terms, IGP, LDR, and CLAP, to improve feasibility, diversity, and novelty in tabular population synthesis. In Stage 2, Transformer and LSTM-Attention models generate sequential travel attributes, including departure time, trip purpose, and travel mode, conditioned on the synthesized tabular profiles. We also introduce novelty and count-aware metrics to evaluate whether valid unseen combinations are recovered and generated in realistic proportions. Results show that regularized models outperform the vanilla WGAN-GP across feasibility, diversity, and novelty. Regularization increases feasibility by 2.1 to 3.7 percentage points and novelty by 6.6 to 10.0 percentage points, improving sampling-zero recovery without sacrificing feasibility. The F1 score improves by 6.3 to 8.6 percentage points. For sequential attributes, LSTM-Attention best matches the trip-length distribution, while Transformer achieves higher overall sequential F1, 90.6\% versus 89.1\%. Cross-stage validation confirms strong consistency between generated mobility status and generated trip chains.

## Metadata
- **Published**: 2026-08-16T17:27:50Z
- **Authors**: Farbod Abbasi, Zachary Patterson, Bilal Farooq
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15867v1)