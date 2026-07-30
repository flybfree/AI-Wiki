---
title: Uncertainty-Guided LLM Semantic Augmentation for Heterogeneous Treatment Effect Estimation
published: 2026-07-29T08:20:17Z
authors: Jialu Xu, Mengkun Liang, Guannan Liu, Xiaojie Mao, Junjie Wu
url: http://arxiv.org/abs/2607.26599v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty-Guided LLM Semantic Augmentation for Heterogeneous Treatment Effect Estimation

## Abstract
Estimating heterogeneous treatment effects is central to targeted interventions, such as personalized promotions and precision medicine. We focus on the conditional average treatment effect (CATE), a standard estimand for characterizing such heterogeneity. Even under standard identification conditions, finite-sample CATE estimation requires learning the nuisance structure for covariate adjustment and treatment-effect heterogeneity, often together with an effective representation of X. Raw numerical and categorical encodings can leave semantic relations and higher-order interactions implicit, making this joint task locally unstable. A motivating study further shows that this instability appears through partially separable assignment- and heterogeneity-side channels. Building on this observation, we propose CURL (Causal Uncertainty-guided Representation Learning), a plug-in adapter that uses estimator uncertainty to allocate pretrained semantic capacity to locally unstable units. CURL queries a frozen LLM through two role-conditioned prompts, constructs assignment- and heterogeneity-oriented representations from the observed covariates, and routes them through separated pathways. On four benchmarks, CURL improves ten host learners in most settings, while ablation, refinement-dynamics, route-reassignment, and probe analyses support the intended design and roles of the two channels.

## Metadata
- **Published**: 2026-07-29T08:20:17Z
- **Authors**: Jialu Xu, Mengkun Liang, Guannan Liu, Xiaojie Mao, Junjie Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26599v1)