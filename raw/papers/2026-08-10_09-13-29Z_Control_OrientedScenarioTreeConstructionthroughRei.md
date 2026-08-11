---
title: Control-Oriented Scenario Tree Construction through Reinforcement Learning
published: 2026-08-10T09:13:29Z
authors: Fabio Pavirani, Bert Claessens, Pierre Pinson, Chris Develder
url: http://arxiv.org/abs/2608.09335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Control-Oriented Scenario Tree Construction through Reinforcement Learning

## Abstract
Multistage stochastic model predictive control (MPC) handles uncertainty by optimizing over a scenario tree, a finite branching approximation of future outcomes constructed from sampled forecasts. To build such a tree, conventional methods focus on matching the underlying probability distribution---e.g., via Wasserstein-based scenario reduction---but improved distributional accuracy does not necessarily yield better control performance. We propose a control-oriented approach that learns scenario tree construction directly from its impact on downstream decisions. Fixing the tree topology, we formulate tree construction as a sequential assignment of sampled scenarios to leaves. This assignment is parameterized by an attention-based policy over the scenario set and trained using reinforcement learning, with closed-loop control profit as the objective. Training is stabilized by an asymmetric critic that leverages realized future trajectories. We evaluate the method on a risk-averse battery arbitrage problem. Across a range of forecast set sizes, the learned construction consistently achieves the highest profit, outperforming classical forward and backward reduction methods and certainty-equivalent (single-trajectory forecast) control. The learned policy also exhibits greater robustness on challenging instances, consistently demonstrating better tail-risk characteristics. Analysis of the resulting trees indicates that our method constructs compact, selectively branching structures that capture high-impact events while keeping most trajectories nearly deterministic. These findings highlight that the value of a scenario tree depends critically on the decisions it supports, and provide an effective framework to train scenario tree constructors merely based on the closed-loop control optimization signal.

## Metadata
- **Published**: 2026-08-10T09:13:29Z
- **Authors**: Fabio Pavirani, Bert Claessens, Pierre Pinson, Chris Develder
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09335v1)