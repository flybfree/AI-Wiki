---
title: Learning to Control Coupled-Dynamics Environments with Joint Markov Decision Processes
published: 2026-08-24T03:38:25Z
authors: Ege C. Kaya, Aliasghar Pourghani, Mahsa Ghasemi, Vijay Gupta, Abolfazl Hashemi
url: http://arxiv.org/abs/2608.22765v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Control Coupled-Dynamics Environments with Joint Markov Decision Processes

## Abstract
Coupled-dynamics environments expose the one-step outcomes that would follow from several possible counterfactual actions under a common realization of exogenous randomness. The ordinary Markov decision process formalism allows one to reason about the marginal law of each action but discards dependence across these counterfactual outcomes. The Joint Markov decision process (JMDP) formalism preserves that dependence. Prior work established the formalism and solved the fixed-policy joint moment evaluation problem in JMDPs. This paper develops optimal-control methods. We define a nonparametric distributional Bellman optimality operator for JMDPs, and prove that when the induced marginal MDP has a unique optimal policy, its iterates converge in Wasserstein distance to the optimal joint return law. For the first two moments, we establish convergence under a weaker condition that permits several mean-optimal actions as long as their tie resolutions share a second-moment fixed point. We also derive sampled targets for neural approximation.

## Metadata
- **Published**: 2026-08-24T03:38:25Z
- **Authors**: Ege C. Kaya, Aliasghar Pourghani, Mahsa Ghasemi, Vijay Gupta, Abolfazl Hashemi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22765v1)