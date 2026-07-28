---
title: Constrained Reinforcement Learning Using Successor Representations
published: 2026-07-27T06:57:01Z
authors: Michael Girstl, Alexander Mattick, Christopher Mutschler
url: http://arxiv.org/abs/2607.24057v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Constrained Reinforcement Learning Using Successor Representations

## Abstract
Real-world Reinforcement Learning depends on the ability to formulate safety constraints into a policy. A common way to model such constraints is to introduce an additional cost signal in the Markov Decision Process, which notifies the agent of unwanted behavior independently of the reward signal. Unfortunately, current methods are hard to adapt to changes in the cost function introduced by, e.g., domain shift or obstacles moving over time. The lack of adaptability means that policies are too unflexible to deal with complex real-world conditions. We propose the Safe Deep Successor Representation (SafeDSR), a novel method that allows quick retraining of policies towards new cost structures. SafeDSR extends the Deep Successor Representation (Kulkarni et al., 2016) to Constrained Reinforcement Learning by introducing a single learnable weight matrix to decouple the learned value function across dynamics, rewards, and costs. This matrix can be updated in a supervised manner instead of having to adapt the whole network if the cost structure of the environment changes. We demonstrate this ability in a freely configurable two-dimensional navigation environment and show that our method is competitive on a simple navigation task while being considerably more flexible

## Metadata
- **Published**: 2026-07-27T06:57:01Z
- **Authors**: Michael Girstl, Alexander Mattick, Christopher Mutschler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24057v1)