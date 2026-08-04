---
title: Feed-Forward Steering in Transformer Residual Dynamics
published: 2026-08-03T11:15:31Z
authors: Timur Mudarisov, Mikhail Burtsev, Radu State
url: http://arxiv.org/abs/2608.02071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Feed-Forward Steering in Transformer Residual Dynamics

## Abstract
Attention-only dynamical theories model Transformer residual directions as particles aggregating on a sphere. We extend this framework by incorporating the feed-forward network (FFN) term as a local steering field acting on each token state. The resulting theory predicts that the tangential component of the FFN field is necessary for motion in residual-direction space, that critical residual directions correspond to nonlinear projective equilibria, and that a commutator defect determines when a finite attention--FFN block can be accurately approximated by a parallel, additive flow. Across GPT-2, Pythia, Mistral, and Llama models, the extended theory improves one-step angular prediction relative to an attention-only baseline, with the contribution of the FFN increasing from GPT-2 to Llama-3-8B. Intervention experiments show that retaining only the tangential FFN component preserves most model quality, whereas retaining only the radial component causes performance to collapse. The tangential component also preserves output diversity under aggregation pressure. As a practical application, layers with small commutator defects can be approximately parallelized with only a modest increase in loss, whereas layers with large defects degrade rapidly. These findings support the interpretation of FFN layers as directional steering fields that shape Transformer residual geometry and govern the feasibility of block-level interventions.

## Metadata
- **Published**: 2026-08-03T11:15:31Z
- **Authors**: Timur Mudarisov, Mikhail Burtsev, Radu State
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02071v1)