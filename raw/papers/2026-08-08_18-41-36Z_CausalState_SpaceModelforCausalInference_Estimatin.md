---
title: Causal State-Space Model for Causal Inference: Estimating Longitudinal Individual Treatment Effects
published: 2026-08-08T18:41:36Z
authors: Abisoye Abidakun, Mingjun Zhong, Georgios Leontidis
url: http://arxiv.org/abs/2608.08288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal State-Space Model for Causal Inference: Estimating Longitudinal Individual Treatment Effects

## Abstract
Estimating counterfactual outcomes over time from longitudinal observational data is central to clinical decision support. Existing methods rely on domain confusion -- adversarial training that renders representations invariant to treatment assignment -- yet this invariance creates a mutual information conflict: it suppresses treatment-correlated covariate signals necessary for accurate outcome prediction. We formalise this tension via a Jensen-Shannon divergence bound on counterfactual prediction error and develop two complementary models. CSSD (Causal State-Space model with Direct decoder) adapts selective State Space Models with a parallel multi-step decoder that eliminates accumulated rollout error by producing all prediction horizons simultaneously in a single forward pass. CSSPD (Causal State-Space model with Predictive regularisation and Direct decoder) augments CSSD with Contrastive Predictive Coding and Local Information Maximisation to reinforce temporal predictability in the balancing representation and recover local covariate information destroyed by domain confusion. On MIMIC-III, CSSPD achieves lower counterfactual RMSE than the Causal Transformer at every horizon tau >= 2 at O(T) encoder cost, with gains from 0.02 (2-step) to 0.07 (6-step). On Cancer Simulation across confounding strengths gamma in {0,1,2,3,4}, CSSPD outperforms CT at gamma <= 3 (margins 25.9%--37.0%), and CSSD achieves the lowest overall average RMSE (12.7% reduction over CT), confirming the MI conflict analysis. To our knowledge, this is the first work to formalise the balancing-prediction MI conflict and propose a structured resolution through complementary predictive and information-theoretic training objectives.

## Metadata
- **Published**: 2026-08-08T18:41:36Z
- **Authors**: Abisoye Abidakun, Mingjun Zhong, Georgios Leontidis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08288v1)