---
title: Lipschitz Bandits with Arbitrary Feedback Delays
published: 2026-08-15T04:39:49Z
authors: Yuhao Liu, Yu Chen, Longbo Huang
url: http://arxiv.org/abs/2608.15036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lipschitz Bandits with Arbitrary Feedback Delays

## Abstract
The Lipschitz bandit problem extends the traditional multi-armed bandit framework to continuous action spaces by assuming that the reward functions satisfy a Lipschitz condition. This work investigates Lipschitz bandits under arbitrary feedback delays, where reward signals are not received immediately upon taking an action but after an arbitrarily chosen delay. We consider both stochastic and adversarial reward settings, proposing an elimination-based algorithm and an EXP3-based algorithm, respectively. For both settings, our algorithms achieve a regret bound of $\tilde{O}\left(T^{\frac{d_z+1}{d_z+2}}+\sqrt{D}\right)$ over a time horizon $T$ with total delay $D$, where the main difference between settings lies in the definition of the zooming dimension $d_z$. Our bounds match existing delay-free regret guarantees for Lipschitz bandits and characterize the additional $\tilde{O}(\sqrt{D})$ impact introduced by feedback delays.

## Metadata
- **Published**: 2026-08-15T04:39:49Z
- **Authors**: Yuhao Liu, Yu Chen, Longbo Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15036v1)