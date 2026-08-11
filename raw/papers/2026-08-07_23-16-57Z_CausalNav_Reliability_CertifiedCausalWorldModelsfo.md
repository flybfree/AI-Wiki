---
title: CausalNav: Reliability-Certified Causal World Models for Control under Physical-Parameter Shift
published: 2026-08-07T23:16:57Z
authors: Yiyao Zhang, Diksha Goel, Hussain Ahmad, Shixun Huang, Jun Shen
url: http://arxiv.org/abs/2608.07809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CausalNav: Reliability-Certified Causal World Models for Control under Physical-Parameter Shift

## Abstract
A world model is only useful for physical AI if it changes what the agent does, and only safe if it declines to do so when it is wrong. We study both halves of that requirement with CausalNav, a controller built around a signed, action-conditioned transition graph over identified state coordinates. At deployment CausalNav simulates a small library of intervention sequences, converts their objective error into policy-logit advice, and admits that advice only when a scale-free predictive-reliability certificate, a policy-margin gate, and an argmax-agreement gate all pass; otherwise it falls back exactly to its own model-based base controller. We evaluate against nine controlled baselines (transformer, recurrent, split-latent, graph, causal-induction, and three recent model-based reasoning modules) on CartPole-v1 and discretized Pendulum-v1 with physical-parameter shifts, under one shared PPO trainer, one interaction budget, and ten held-out seeds (200 runs). CausalNav attains the best average rank (1.25 of ten). The diagnostic result is more informative than the ranking: the learned graph recovers structure well above chance (CartPole F1 = 0.59 +/- 0.09), yet per-seed structural fidelity is uncorrelated with per-seed control benefit (r = -0.15, p = 0.67), and the certificate abstains on 10/10 Pendulum seeds, where forcing the planner on costs return. Model fidelity did not predict downstream control utility in our setting; certified abstention, not better prediction, is what made the world model safe to deploy.

## Metadata
- **Published**: 2026-08-07T23:16:57Z
- **Authors**: Yiyao Zhang, Diksha Goel, Hussain Ahmad, Shixun Huang, Jun Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07809v1)