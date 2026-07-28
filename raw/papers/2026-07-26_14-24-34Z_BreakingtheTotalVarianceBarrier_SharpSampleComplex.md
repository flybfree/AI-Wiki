---
title: Breaking the Total Variance Barrier: Sharp Sample Complexity for Linear Heteroscedastic Bandits with Fixed Action Set
published: 2026-07-26T14:24:34Z
authors: Heyang Zhao, Tianyuan Jin, Weixin Wang, Vincent Y. F. Tan, Pan Xu, Quanquan Gu
url: http://arxiv.org/abs/2607.23679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breaking the Total Variance Barrier: Sharp Sample Complexity for Linear Heteroscedastic Bandits with Fixed Action Set

## Abstract
Recent years have witnessed increasing interests in tackling heteroscedastic noise in bandits and reinforcement learning. In these works, the cumulative variance of the noise $Λ= \sum_{t=1}^T σ_t^2$, where $σ_t^2$ is the variance of the noise at round $t$, is used to characterize the statistical complexity of the problem, yielding \emph{simple regret} bounds of order $\tilde{\cal{O}}(d \sqrt{Λ/ T^2})$ for $d$-dimensional linear bandits with heteroscedastic noise. However, with a closer look, $Λ$ remains the same order even if the noise is close to zero at half of the rounds, which indicates that the $Λ$-dependence is not optimal. In this paper, we revisit the stochastic linear bandit problem with heteroscedastic noise, where the action set is prefixed throughout the learning process. We propose a novel variance-adaptive algorithm \texttt{VAEE} (Variance-Aware Exploration with Elimination) for large action set, which actively explores actions that maximizes the information gain among a candidate set of actions that are not eliminated. With the active-exploration strategy, we show that \texttt{VAEE} achieves a \emph{simple regret} with a nearly \emph{harmonic-mean} dependent rate. For finitely many actions, we propose a variance-aware variant of G-optimal design based exploration, which achieves a simple regret with sharper dependence on $d$. We also establish a nearly matching lower bound for the fixed action set setting indicating that \emph{harmonic-mean} dependent rate is unavoidable. To the best of our knowledge, this is the first work that breaks the $\sqrtΛ$ barrier for stochastic linear bandits with heteroscedastic noise.

## Metadata
- **Published**: 2026-07-26T14:24:34Z
- **Authors**: Heyang Zhao, Tianyuan Jin, Weixin Wang, Vincent Y. F. Tan, Pan Xu, Quanquan Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23679v1)