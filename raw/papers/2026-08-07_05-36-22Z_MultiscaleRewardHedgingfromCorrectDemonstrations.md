---
title: Multiscale Reward Hedging from Correct Demonstrations
published: 2026-08-07T05:36:22Z
authors: Pahan Dewasurendra
url: http://arxiv.org/abs/2608.06825v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multiscale Reward Hedging from Correct Demonstrations

## Abstract
Learning from correct demonstrations is harder than supervised learning when many answers are correct: after predicting, the learner sees one valid answer but not whether its own answer was valid, nor any reward. Existing reward-hedging guarantees consequently assume a finite reward class. We give the first horizon-free guarantee for continuous classes. The key is to hedge in one shared vote over tolerant optimality tests at every accuracy scale. A target reward has one surviving proxy per scale, and a prediction with gap above that scale doubles the proxy. This yields the simultaneous tail bound $|\{t:\ell_t>2^{-j}\}|\leq \log_2\mathcal N(\mathcal G,2^{-j-1})+j$, where $\mathcal G$ is the class of optimality-gap functions. Integrating the tails gives cumulative hidden gap bounded by a metric-entropy integral, independently of the number of rounds. Polynomial entropy $(A/ε)^d$ gives $O(d\log A)$ total gap and a fast $O(d/m)$ statistical rate. For bounded linear contextual recommendation, the result is $O(d)$ regret for arbitrary compact menus. This is the first polynomial finite bound without structural restrictions on the menus, at the price of improper prediction. Although the general vote can be expensive, it is exactly polynomial-time for one-dimensional Lipschitz parameter curves. Fixed-radius rank-two recommendation takes $O(KT^2)$ time for menus of size $K$. We also prove an $Ω(d)$ lower bound, low-rank and bounded ReLU-network corollaries, and a robust theorem that adds only the demonstrator's cumulative suboptimality. A reproducible adaptive stress test illustrates the predicted scale adaptation. After factorization, an exact MovieLens audit runs in 1.7 CPU seconds across ten users and improves mean latent gap over both a demonstrated-rating policy and a proper online baseline. The learner uses only action demonstrations and never observes a reward or a loss.

## Metadata
- **Published**: 2026-08-07T05:36:22Z
- **Authors**: Pahan Dewasurendra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06825v1)