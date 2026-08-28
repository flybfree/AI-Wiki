---
title: Making Latent Evolution Explicit: Operator-Structured Transitions for World Action Models
published: 2026-08-27T15:43:44Z
authors: Xiaoxiao Lu, Yunlong Dong, Jiahao Shi, Ye Yuan
url: http://arxiv.org/abs/2608.27259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Making Latent Evolution Explicit: Operator-Structured Transitions for World Action Models

## Abstract
World Action Models (WAMs) augment robot policies by predicting how task-relevant scene states may evolve under interaction. Recent WAMs increasingly perform such prediction in latent representation spaces, avoiding full appearance-level generation while preserving control-relevant information. Yet latent transitions are commonly realized with Transformer-based predictors whose inductive structure is centered on token interaction rather than temporal evolution. We study transition realization as an architectural choice distinct from predictive representation and prediction-policy coupling. We introduce the Latent Evolution Operator Network (LEON), which models latent evolution in a learned observable space through context-modulated operator-based propagation and additive forcing. Grounded in the controlled Koopman generator view of evolution, LEON organizes context-dependent transition variation around a shared evolution-operator structure while retaining a complementary path for additive change. Controlled dynamical systems verify the resulting evolution-specific inductive bias and the complementary roles of operator propagation and forcing. Across two WAM formulations that integrate latent prediction into the policy differently, LEON improves closed-loop performance and robustness while remaining effective under full transition replacement. These results establish transition realization as a consequential architectural choice in latent WAMs.

## Metadata
- **Published**: 2026-08-27T15:43:44Z
- **Authors**: Xiaoxiao Lu, Yunlong Dong, Jiahao Shi, Ye Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27259v1)