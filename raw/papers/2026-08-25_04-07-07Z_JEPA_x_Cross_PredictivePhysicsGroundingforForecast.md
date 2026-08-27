---
title: JEPA-x: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics
published: 2026-08-25T04:07:07Z
authors: Kehan Wen, Ziming Li, Siyuan Luo, Fan Shi
url: http://arxiv.org/abs/2608.24044v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# JEPA-x: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics

## Abstract
Latent world models plan by predicting how candidate actions advance learned latent dynamics. In self-predictive models, however, the encoder and predictor are optimized jointly and can co-adapt to latent transitions that are easy to predict but weakly constrained by the physical evolution of the scene. We introduce the cross-predictive JEPA (JEPA-x), which grounds visual latent dynamics in privileged physical trajectories. JEPA-x treats visual observations and physical states as corresponding views of the same action-conditioned trajectory, advances both through a shared predictor, and matches predictions from either view to future representations in both modalities. This requires the action-conditioned predictor to learn a common transition rule for both the visual and physical descriptions of the scene. The physical branch is used only during training, leaving no computational overhead at deployment. Empirical results show that JEPA-x reduces the rollout drift of a newly fitted predictor from $0.361$ to $0.104$ and increases mean control success from $53.6\%$ to $78.2\%$ on a multi-task suite spanning six evaluation subfamilies. We additionally show that making physical state decodable is not the load-bearing factor; rather, the gains arise from how cross-prediction shapes the geometry of the learned latent dynamics.

## Metadata
- **Published**: 2026-08-25T04:07:07Z
- **Authors**: Kehan Wen, Ziming Li, Siyuan Luo, Fan Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24044v2)