---
title: An Efficient Near-Optimal Algorithm for Adversarial $m$-Set Bandits
published: 2026-08-12T16:28:06Z
authors: Francesco Bacchiocchi, Tommaso Cesari, Roberto Colomboni
url: http://arxiv.org/abs/2608.12231v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Efficient Near-Optimal Algorithm for Adversarial $m$-Set Bandits

## Abstract
We study adversarial combinatorial bandits with $m$-set actions, where at each round the learner selects $m$ out of $d$ items and observes only the aggregate loss of the selected items. The resulting action set contains $K=\binom{d}{m}$ elements and can therefore be exponentially large. Nevertheless, the loss of every action is determined by the same $d$-dimensional vector of item losses. We propose a computationally efficient algorithm that exploits this structure without explicitly enumerating the action set. Against adaptive non-anticipating adversaries, it guarantees, with probability at least $1-δ$, regret against the best fixed action of \[   R_T =   O\left(\sqrt{dT\log(K/δ)}\right). \] This matches the high-probability regret bound of the finite-action EXP3-KW algorithm of Zimmert and Lattimore, whose direct implementation may require exponential space. Our algorithm instead represents each sampling distribution with $d$ parameters and runs in polynomial time without enumerating the action set. Thus, it resolves the open problem posed by Maiti et al.

## Metadata
- **Published**: 2026-08-12T16:28:06Z
- **Authors**: Francesco Bacchiocchi, Tommaso Cesari, Roberto Colomboni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12231v1)