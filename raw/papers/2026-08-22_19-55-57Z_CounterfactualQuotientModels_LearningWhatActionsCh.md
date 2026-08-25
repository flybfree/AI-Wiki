---
title: Counterfactual Quotient Models: Learning What Actions Change, Not What the World Does
published: 2026-08-22T19:55:57Z
authors: Junlin Chen, Ruijie Wang, Jianxin Li
url: http://arxiv.org/abs/2608.22092v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Counterfactual Quotient Models: Learning What Actions Change, Not What the World Does

## Abstract
Reinforcement-learning models commonly predict complete future states, observations, or feature occupancies, even though action selection depends only on differences between the consequences of candidate actions. As a result, these models may devote substantial statistical and representational capacity to high-dimensional phenomena that evolve independently of the agent's current choice. We introduce the Counterfactual Quotient Model, which treats action-conditioned futures as equivalent when they differ only by a component shared across actions. Its canonical centered representation removes this common component while preserving every pairwise action comparison expressible by the modeled reward family. The implemented model learns these action-dependent effects directly from synchronized counterfactual rollouts, so shared stochastic dynamics cancel before function approximation rather than after complete futures have been predicted. We establish the decision sufficiency, identifiability, common-mode invariance, approximation behavior, and regret properties of the resulting representation. Controlled experiments in physics-based environments provide initial evidence for these properties: direct effect learning suppresses action-independent variation, supports previously unseen reward queries, and improves action ranking relative to models trained to predict absolute futures.

## Metadata
- **Published**: 2026-08-22T19:55:57Z
- **Authors**: Junlin Chen, Ruijie Wang, Jianxin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22092v1)