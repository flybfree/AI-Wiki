---
title: Optimistic Rates for Multiclass PAC Learning
published: 2026-08-11T12:46:03Z
authors: Xiaoyu Li, Andi Han, Jiaojiao Jiang, Junbin Gao
url: http://arxiv.org/abs/2608.10869v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimistic Rates for Multiclass PAC Learning

## Abstract
Worst-case multiclass bounds do not become smaller when the best classifier is already nearly correct: what is missing is an optimistic rate, a guarantee whose fluctuation scales with the oracle risk itself. For a class of Natarajan dimension $d_N$ and Daniely-Shalev-Shwartz dimension $d_{DS}$, the optimal excess risk is known at the two endpoints ($d_{DS}/n$ realizable, $\sqrt{d_N/n}+d_{DS}/n$ agnostic [HMZ24, CEH+26, Pab26]) and open in between. We close the gap: at every fixed oracle risk $L^\star$, the optimal excess risk is $\widetildeΘ(\sqrt{L^\star d_N/n}+d_{DS}/n)$, uniformly in the alphabet size, attained by a learner that knows neither $L^\star$ nor the confidence level. The upper bound composes the cover-menu-compression architecture of [CEH+26], at the realizable rate of [Pab26], with a new comparator-facing relative compression theorem: a size-$k$ compression rule that empirically dominates a comparator $h$ has population risk at most $L(h)+O(\sqrt{L(h)Γ}+Γ)$ with $Γ=(k\log n+\log(1/δ))/n$, without stability; this transfers the comparison principle of the sharp binary theory [MQZ26] while discarding its Boolean-cube geometry, which does not lift to multiclass labels. The lower bound forces both terms using one class and one distribution at every fixed $L^\star$, by a pair-Assouad scheme calibrated to $L^\star$ and a fiber argument on the pseudo-cubes underlying the Natarajan-versus-DS separation of [BCD+22]. Both theorems extend to list learning: against the best $r$-tuple of hypotheses, the same architecture and the same two engines yield an optimistic rate and a lower bound of the same shape, forcing the fluctuation term that [Pab26] expected to be necessary against list comparators, and removing the factor $r$ from the known realizable list lower bound.

## Metadata
- **Published**: 2026-08-11T12:46:03Z
- **Authors**: Xiaoyu Li, Andi Han, Jiaojiao Jiang, Junbin Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10869v1)