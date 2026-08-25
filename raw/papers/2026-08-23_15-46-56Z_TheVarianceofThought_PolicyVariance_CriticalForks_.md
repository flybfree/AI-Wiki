---
title: The Variance of Thought: Policy Variance, Critical Forks, and Local Credit Assignment
published: 2026-08-23T15:46:56Z
authors: Yingru Li
url: http://arxiv.org/abs/2608.22467v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Variance of Thought: Policy Variance, Critical Forks, and Local Credit Assignment

## Abstract
Long-horizon language-model tasks --- multi-step reasoning and tool-using agents alike --- are limited by credit assignment. We analyze it through the policy variance $σ_π^2(s)=\operatorname{Var}_{a\simπ}[Q_π(s,a)]$, which in a deterministic MDP is the sole source of return variance and is injected in discrete pulses at states we call critical forks. Three results follow. (i) Policy variance is a discovery budget: observing an action of advantage $c$ requires $Ω(c^2/σ_π^2(s))$ draws, a bound that is exact on the canonical two-point fork. (ii) Policy variance is bounded by the policy's Gini dispersion, $σ_π^2(s)\le 1-\|π(\cdot|s)\|_2^2$, a rollout-free necessary condition for criticality computable from logits alone. (iii) The remaining horizon sets the estimation cost: at a fork whose downstream success probability is $P$, the Monte Carlo advantage estimate has signal-to-noise ratio of order $\sqrt{P}$, so its sample cost scales as $1/P$ --- a cost that branched sampling shares. Bootstrapping removes it by converting a product of survival probabilities into a sum, provided the value representation is multiplicatively accurate, which argues for log-value parameterization.

## Metadata
- **Published**: 2026-08-23T15:46:56Z
- **Authors**: Yingru Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22467v1)