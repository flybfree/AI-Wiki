---
title: Path-dependent Discrete Amortized Inference
published: 2026-08-09T11:35:05Z
authors: Tiago da Silva, Esmeralda S. Whitammer, Salem Lahlou
url: http://arxiv.org/abs/2608.08644v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Path-dependent Discrete Amortized Inference

## Abstract
We consider the problem of sampling compositional and discrete objects from a given unnormalized posterior distribution. Notably, recent studies have shown that this problem can be efficiently solved by learning a deterministic Markov Decision Process (MDP) that progressively builds each object in proportion to the posterior. In this work, however, we demonstrate that the Markovian assumption can both hamper signal propagation during training and catastrophically reduce the learned sampler's expressivity due to state aliasing. To address these issues, we propose lifting the MDP with a learnable latent dynamical system that allows the underlying policy to depend on the entire past trajectory---and not only on the current state. In view of this, we refer to the resulting method as path-dependent discrete amortized inference. Importantly, we provably extend existing learning algorithms for discrete amortized samplers to our setting. In experiments on standard benchmark problems, we also show that our approach often leads to faster learning convergence and improved state space exploration relatively to prior techniques.

## Metadata
- **Published**: 2026-08-09T11:35:05Z
- **Authors**: Tiago da Silva, Esmeralda S. Whitammer, Salem Lahlou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08644v1)