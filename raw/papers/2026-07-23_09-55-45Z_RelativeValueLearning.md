---
title: Relative Value Learning
published: 2026-07-23T09:55:45Z
authors: Marc Höftmann, Jan Robine, Stefan Harmeling
url: http://arxiv.org/abs/2607.21120v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Relative Value Learning

## Abstract
In reinforcement learning, critics typically estimate absolute state values $V(s)$, estimating how good a particular situation is in isolation. However, it turns out that only differences in value are relevant for control. Motivated by this, we propose Relative Value Learning (RV), a framework that learns value differences directly via an antisymmetric function $Δ(s_i, s_j) = V(s_i) - V(s_j)$. We introduce a pairwise Bellman operator and prove it is a $γ$-contraction with a unique fixed point equal to the true value differences, derive well-posed $1$-step, $n$-step and $λ$-return targets and reconstruct generalized advantage estimation from pairwise differences to obtain an unbiased policy-gradient estimator (R-GAE). Beyond theoretical results, we integrate RV with PPO and achieve competitive performance on the Atari benchmark (49 ALE games) compared to standard PPO, indicating that relative value estimation is an effective alternative to absolute critics.

## Metadata
- **Published**: 2026-07-23T09:55:45Z
- **Authors**: Marc Höftmann, Jan Robine, Stefan Harmeling
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21120v1)