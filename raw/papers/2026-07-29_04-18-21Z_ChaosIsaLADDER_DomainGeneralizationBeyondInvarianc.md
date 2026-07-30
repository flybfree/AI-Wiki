---
title: Chaos Is a LADDER: Domain Generalization Beyond Invariance via Reweighting
published: 2026-07-29T04:18:21Z
authors: Yuhang Jiang, Fengchuan Zhang, Sanguo Zhang, Guojun Zhu
url: http://arxiv.org/abs/2607.26458v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Chaos Is a LADDER: Domain Generalization Beyond Invariance via Reweighting

## Abstract
Domain generalization (DG) aims to learn from multiple source domains and generalize to unseen target domains. Most DG methods pursue invariance: they seek a causal representation whose prediction rule is invariant across domains. This principle is effective when the causal mechanism is stable, but becomes restrictive when the domain itself modulates how causal content maps to the response. In this case, directly feeding domain style into the predictor can create misleading shortcuts, since style does not by itself cause the response. Yet the apparent chaos of multiple styles can become a ladder: style can locate the unseen target domain among source domains and guide which domain-dependent prediction rules should be trusted. We propose \emph{Latent Adaptive Domain Disentanglement and Environment Reweighting} (LADDER), a fixed-model DG pipeline that learns causal/style representations, freezes the encoders, fits source-specific classifiers, and uses an unlabeled target-domain covariate set only at inference to compute weights over these fixed classifiers, with no target labels or model-state updates. We establish theoretical guarantees for source reweighting and validate LADDER on simulations, FMoW, and a location-grouped iWildCam protocol, with gains in overall and group-averaged accuracy.

## Metadata
- **Published**: 2026-07-29T04:18:21Z
- **Authors**: Yuhang Jiang, Fengchuan Zhang, Sanguo Zhang, Guojun Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26458v1)