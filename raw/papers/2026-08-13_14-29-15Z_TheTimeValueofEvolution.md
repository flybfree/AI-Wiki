---
title: The Time Value of Evolution
published: 2026-08-13T14:29:15Z
authors: Matthew Siper, Ahmed Khalifa, Julian Togelius
url: http://arxiv.org/abs/2608.13297v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Time Value of Evolution

## Abstract
In evolutionary search, a weak child can be a valuable ancestor that makes high-fitness regions reachable. Immediate-return control is blind to this delayed utility, penalizing mutations through their immediate offspring even when they open productive future lineages. We formalize this hidden dynamic as the time value of evolution within a finite-horizon Markov decision process. To exploit it, we introduce Lineage-Value Policy Gradients (LVPG), a long-horizon actor-critic framework for automated trading policy discovery. Our architecture decouples search control into specialized policy heads over a shared generative backbone: a bootstrapped critic head estimates the value of finite-horizon lineage potential from multi-step mutation trees, while an actor head dynamically modulates mutation intensity over the remaining search budget. We isolate the impact of long-horizon credit assignment against immediate-return optimization across 90 paired runs under matched operators, lineage supervision, folds, seeds, and budgets. Path-based credit assignment substantially accelerates finite-budget search, increasing validation best-so-far AUC by 0.394 Sharpe units. LVPG also produces fewer temporary regressions than immediate-return optimization and recovers from them more often. Finite-horizon lineage value yields more selective non-monotonic search and stronger policies within identical resource constraints.

## Metadata
- **Published**: 2026-08-13T14:29:15Z
- **Authors**: Matthew Siper, Ahmed Khalifa, Julian Togelius
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13297v1)