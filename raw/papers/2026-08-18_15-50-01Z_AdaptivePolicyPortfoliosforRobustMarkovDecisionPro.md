---
title: Adaptive Policy Portfolios for Robust Markov Decision Processes
published: 2026-08-18T15:50:01Z
authors: Kasper Engelen, Sebastian Junges, Guillermo A. Pérez, Marnix Suilen
url: http://arxiv.org/abs/2608.17929v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Policy Portfolios for Robust Markov Decision Processes

## Abstract
Robust Markov decision processes optimize one policy against a set of plausible transition functions. This can be conservative when the unknown dynamics are fixed and become partially identifiable after deployment. We study adaptive policy portfolios: finite sets of memoryless randomized policies synthesized offline and paired with a lightweight online selector. Robust regret is a natural measure of portfolio quality: for each plausible environment, it measures the loss of the best portfolio member relative to the policy that would have been optimal had that environment been known. Related regret objectives were studied by Ghavamzadeh et al. (2016) with an emphasis on approximations and relaxations for safe policy improvement. We give a complexity-theoretic account of portfolio certification and synthesis. Certifying a given portfolio is $\forall\mathbb{R}$-complete already for deterministic portfolios in acyclic (s,a)-rectangular RMDPs. Synthesizing a portfolio of unary-bounded size is $\exists\forall\mathbb{R}$-complete for general rational polytopes, even with fixed discount and acyclic dynamics. The single-policy case is already hard, both combinatorially and algebraically. Finally, we present an offline portfolio construction that is amenable to runtime specialization.

## Metadata
- **Published**: 2026-08-18T15:50:01Z
- **Authors**: Kasper Engelen, Sebastian Junges, Guillermo A. Pérez, Marnix Suilen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17929v1)