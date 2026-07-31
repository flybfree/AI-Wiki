---
title: Search as Computation Allocation
published: 2026-07-30T08:45:14Z
authors: Alexander Tuisov
url: http://arxiv.org/abs/2607.27871v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Search as Computation Allocation

## Abstract
Many algorithms spend an internal resource before returning a decision and are evaluated only by the quality of that terminal output. We formalize such procedures as terminal computation-allocation problems: costly computations produce observations, update beliefs about a latent environment, and matter only through terminal decision loss. Bellman equations characterize optimal allocation under fixed budgets, priced computation, and exact certification. We then relate value of computation (VOC) to information. Mutual information equals myopic VOC under log loss, whereas under simple regret VOC is a knowledge-gradient quantity; moreover, information gain can rank computations arbitrarily poorly, although it gives a one-sided upper bound on VOC. Bandit pulls, tree simulations, and node expansions illustrate the same model under different computation topologies. Finally, under an explicit frontier-resolution and heuristic-error model, maximizing approximate VOC recovers weighted A*, with A* and greedy best-first search as limiting cases. The theory identifies a shared decision problem without asserting that one acquisition rule is universally optimal.

## Metadata
- **Published**: 2026-07-30T08:45:14Z
- **Authors**: Alexander Tuisov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27871v1)