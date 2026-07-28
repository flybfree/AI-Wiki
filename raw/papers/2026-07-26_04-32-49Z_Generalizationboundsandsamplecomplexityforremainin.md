---
title: Generalization bounds and sample complexity for remaining useful life prediction from complete degradation trajectories
published: 2026-07-26T04:32:49Z
authors: Huy Hoang Le, Kim-Anh Nguyen
url: http://arxiv.org/abs/2607.23454v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generalization bounds and sample complexity for remaining useful life prediction from complete degradation trajectories

## Abstract
Data-driven remaining useful life (RUL) prediction requires complete degradation trajectories for training, yet such run-to-failure data are scarce and expensive. Practitioners currently lack principled guidance on how many failure examples suffice for a given model and accuracy target. This paper develops a sample complexity framework for RUL prediction comprising seven main results organised around three themes. First, we establish fundamental learning rates: a distribution-free generalization bound shows that the uniform deviation of the mean squared error decreases as $O(B^{2}\sqrt{p/n})$, where $p$ is the model complexity and $n$ the number of trajectories, and a minimax lower bound proves that the $Θ(p/n)$ rate is unimprovable.} \rev{Second, we quantify how domain knowledge accelerates learning: incorporating degradation physics reduces data requirements by up to two orders of magnitude for deep networks, a Bernstein-type analysis achieves the minimax-optimal $O(p/n)$ rate under high signal-to-noise conditions, and closed-form penalties reveal when an incorrectly assumed physics model hurts rather than helps. Third, we characterise the impact of data quality: fleet variability induces an irreducible bias$-$variance tradeoff, while right-censored observations suffer an efficiency loss that depends critically on the degradation class.} Closed-form expressions are provided for exponential, power-law, and stretched-exponential degradation. \rev{Cross-domain validation against published turbofan, battery, and bearing benchmarks confirms the theoretical predictions within a factor of 2$-$3 on average. The results yield practical guidelines for planning data collection, selecting model complexity, and evaluating physics model assumptions in prognostics applications.

## Metadata
- **Published**: 2026-07-26T04:32:49Z
- **Authors**: Huy Hoang Le, Kim-Anh Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23454v1)