---
title: Does 1/2-Tsallis-INF Also Work Well for Best-Arm Identification?
published: 2026-08-15T18:38:36Z
authors: Jingxin Zhan, Yuze Han, Zhihua Zhang
url: http://arxiv.org/abs/2608.15365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does 1/2-Tsallis-INF Also Work Well for Best-Arm Identification?

## Abstract
Regret minimization (RM) and best-arm identification (BAI) are two fundamental objectives in multi-armed bandits. Among regret-minimizing algorithms, $1/2$-Tsallis-INF is a canonical best-of-both-worlds FTRL algorithm: it achieves logarithmic pseudo-regret in stochastic bandits while retaining minimax-optimal regret in adversarial bandits, without knowing the environment in advance. This raises a natural question: can the same algorithm, without additional exploration, also identify the best arm reliably? We study this question in stochastic bandits by analyzing the failure probability $\operatorname{Err}_t$, defined as the probability that the empirical best arm determined by the cumulative importance-weighted loss estimates of 1/2-Tsallis-INF differs from the true optimal arm. The main difficulty is that, at the logarithmic-regret scale, suboptimal arms are sampled with probability heuristically of order $1/t$. Consequently, importance weighting causes the cumulative estimator to fluctuate on the same linear scale as its mean separation. To overcome this obstacle, guided by a diffusion toy model, we construct a Lyapunov function for the gap process between the estimated cumulative loss of the optimal arm and that of the best competing arm. This leads to polynomial upper bounds on $\operatorname{Err}_t$: for learning rate $η_t=α/\sqrt t$, $\operatorname{Err}_t$ decays at rate $t^{-2+α^2μ_{i_*}/4+ρ}$ for any $ρ>0$, where $μ_{i_*}$ denotes the mean loss of the true optimal arm. We also establish a lower bound $Ω(t^{-2-\varepsilon})$ for any $\varepsilon>0$, showing that the exponent $2$ is essentially tight.

## Metadata
- **Published**: 2026-08-15T18:38:36Z
- **Authors**: Jingxin Zhan, Yuze Han, Zhihua Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15365v1)