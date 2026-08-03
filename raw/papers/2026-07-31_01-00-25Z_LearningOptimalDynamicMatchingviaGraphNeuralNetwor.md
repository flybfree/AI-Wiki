---
title: Learning Optimal Dynamic Matching via Graph Neural Networks
published: 2026-07-31T01:00:25Z
authors: Genta Okada, Shunya Noda, Junpei Komiyama, Akira Matsushita
url: http://arxiv.org/abs/2607.28925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Optimal Dynamic Matching via Graph Neural Networks

## Abstract
Dynamic matching markets require decisions about whom to match and when: matching now yields value but removes participants who may create better future opportunities. We develop a value-based reinforcement-learning framework for this problem on finite, evolving weighted graphs. We study an infinite-horizon continuous-time model with stochastic arrivals, node-type transitions, edge realizations, and exogenous exits. We prove an event-time reduction: without loss of optimality, the planner acts immediately after each exogenous event and then waits for the next one. We further show that the optimal edge-wise $Q$-function is characterized by a single continuation-value function on post-decision residual graphs, reducing the learned object from state-action values to graph values. Exact action selection still requires combinatorial matching optimization; we approximate the value with a graph neural network, train it by temporal-difference learning, and use it in a forward-greedy matching heuristic. In a binary-type benchmark, the learned policy substantially outperforms immediate and threshold-greedy rules by preserving common nodes for rare arrivals of valuable matches while forming lower-value matches only in thick pools. In a kidney paired donation benchmark, it performs similarly to immediate greedy when exits are unpredictable, recovers the logic of patient matching when warnings are reliable, and outperforms the better of Immediate Greedy and Patient Greedy across intermediate warning probabilities. These results show that residual-graph value learning yields state-dependent dynamic matching policies that adapt to realized connectivity and exit information.

## Metadata
- **Published**: 2026-07-31T01:00:25Z
- **Authors**: Genta Okada, Shunya Noda, Junpei Komiyama, Akira Matsushita
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28925v1)