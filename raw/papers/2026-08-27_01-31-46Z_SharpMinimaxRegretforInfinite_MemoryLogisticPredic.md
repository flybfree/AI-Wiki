---
title: Sharp Minimax Regret for Infinite-Memory Logistic Prediction
published: 2026-08-27T01:31:46Z
authors: Vaneet Aggarwal
url: http://arxiv.org/abs/2608.26515v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sharp Minimax Regret for Infinite-Memory Logistic Prediction

## Abstract
We study online prediction for a specific finite-alphabet, exogenously driven source with infinite input memory. Independent Rademacher inputs $(U_t)$ are observed sequentially, and the next binary mark has logit $\sum_{j=1}^{t}θ_jU_{t+1-j}$, where $\abs{θ_j}\leq r_j$ and $\sum_jr_j\leq B$. Regret is expected cumulative excess log loss. Lag $j$ can affect prediction by scale $r_j$ and enters only $n_{T,j}=T-j+1$ prediction rounds, leading to the lag-resolved spectrum $Γ_T(r)=\sum_{j=1}^{T}\log\!\left(1+n_{T,j}r_j^2\right)$. For every summable envelope, a localized Bayesian mixture proves $\cR_T(r)\leq CΓ_T(r)$. For exponential and polynomial envelopes, under the stated finite-sample dimension condition, a Toeplitz-design converse proves $\cR_T(r)\geq cΓ_T(r)$, with constants allowed to depend on the fixed decay parameters and the logit bound. Thus $Γ_T(r)$ is the minimax cumulative-regret scale for this source class in these canonical regimes, giving $Θ(α^{-1}\log^2T)$ for $r_j=Ae^{-αj}$ and $Θ(T^{1/(2s)})$ for $r_j=Aj^{-s}$, $s>1$. The converse is specific to the exogenous lagged model and is not a profile-only theorem for arbitrary stationary infinite-memory sources. Retaining only the most recent $h$ inputs costs order $\sum_{j>h}n_{T,j}θ_j^2$, yet the same worst-case truncation profile can correspond to polynomially different regret. A scaled online Newton predictor attains the spectrum upper bound.

## Metadata
- **Published**: 2026-08-27T01:31:46Z
- **Authors**: Vaneet Aggarwal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26515v1)