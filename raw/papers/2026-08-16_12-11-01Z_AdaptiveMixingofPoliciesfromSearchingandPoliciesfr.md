---
title: Adaptive Mixing of Policies from Searching and Policies from Learning
published: 2026-08-16T12:11:01Z
authors: Gavin B. Rens
url: http://arxiv.org/abs/2608.15700v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Mixing of Policies from Searching and Policies from Learning

## Abstract
Background: Distillation of training targets generated thru search/planning has proven useful in reinforcement learning, but search can take exceedingly long. Objectives: Rather than perform search to the same depth every time (typically at a fixed period of steps), reduce the search depth proportionally to the quality of the policy network priors. Methods: We describe Flexer, an architecture that, for each step, mixes the policy from a neural network and the policy from Monte Carlo tree search. The mixing factor favors the MCTS policy as the policy imitation error of the network and the environment models' variance increases. Results: Flexer outperforms a version of AlphaZero (and DQN and ADP) for some experiments on three toy symbolic problems.

## Metadata
- **Published**: 2026-08-16T12:11:01Z
- **Authors**: Gavin B. Rens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15700v1)