---
title: Unifying ICL, SFT, KL-Regularized RL Through a Bayesian Lens
published: 2026-09-04T13:06:29Z
authors: Junxin Fan
url: http://arxiv.org/abs/2609.05111v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unifying ICL, SFT, KL-Regularized RL Through a Bayesian Lens

## Abstract
Large language models are now trained and evaluated under a diverse set of paradigms: supervised fine-tuning (SFT), few-shot in-context learning (ICL), KL-regularized RLHF/RLVR, on-policy distillation (OPD), and test-time reasoning with search and chain-of-thought. These methods are often discussed as fundamentally different, and recent empirical results--such as the mixed impact of few-shot prompting on RL-tuned reasoning models--can appear puzzling. This note develops a Bayesian perspective that puts these procedures on the same footing. At the core is a two-step template: (i) construct a (generalized) Bayes or Gibbs posterior q* over outputs or actions given a context, using a prior/reference model and a utility signal (log-likelihood, reward, or advantage); and (ii) approximate q* by a forward-KL projection onto a parametric family, either in-weights (SFT/RL) or in-context (ICL). Part I formalizes few-shot ICL and SFT as amortized and-weights projections onto the Bayes posterior predictive. Parts II-IV show that KL-regularized RLHF/RLVR, reward-weighted SFT, reward-weighted ICL (RW-ICL), and advantage-weighted SFT (AWSFT) are all instances of forward-KL projection onto posteriors induced by rewards or advantages. We disentangle where these equivalences hold (objectives and first-order updates) and where they do not (source and granularity of the learning signal). Part V sketches implications for modern reasoning pipelines: RLHF/RLVR recipes as "posterior design + projection", why cold-start or supervised warm-up is practically unavoidable for importance-weighted KL projections, and DeepSeek-R1 and o1-style reasoning models as combining test-time Bayesian search with training-time KL amortization.

## Metadata
- **Published**: 2026-09-04T13:06:29Z
- **Authors**: Junxin Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05111v1)