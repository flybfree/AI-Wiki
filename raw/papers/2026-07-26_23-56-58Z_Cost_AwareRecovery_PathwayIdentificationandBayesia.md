---
title: Cost-Aware Recovery-Pathway Identification and Bayesian Optimization for Autonomous Materials Discovery
published: 2026-07-26T23:56:58Z
authors: Debajyoti Ray, Niranjan Srinivas
url: http://arxiv.org/abs/2607.23896v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cost-Aware Recovery-Pathway Identification and Bayesian Optimization for Autonomous Materials Discovery

## Abstract
Autonomous laboratories automate experimental execution, but a campaign must also decide which recovery pathway merits optimization. We formulate this as a sequential decision problem with a discrete pathway-identification stage and a continuous within-pathway optimization stage under heterogeneous experimental costs. Our implementation, Coactive learning, combines a cost-sensitive Bayesian hypothesis-discrimination policy motivated by EC2 (Golovin et al., 2010) with Gaussian-process Bayesian optimization (Srinivas et al., 2010). Under explicitly stated assumptions, the expected spend of one fixed-budget campaign attempt is bounded by the expected pathway-identification cost plus the capped within-pathway optimization budget. We evaluate the method on synthetic benchmarks constrained by selected results reported for PNNL's CICERO selective-precipitation study (Ritchhart et al., 2026). The method performs comparably to an oracle-pathway Bayesian-optimization reference and to a strong split-plate baseline that discriminates pathways with its first plate, without receiving an oracle label for the correct pathway. It is given a candidate hypothesis space and a diagnostic likelihood model. On an NdFeB-inspired instance, it avoids the simulated penalty of a commit-first baseline that initially selects a plausible but inferior hydroxide pathway. This hypothetical wrong-first-commitment scenario is motivated by the hydroxide-oxalate performance contrast reported by CICERO. We characterize the sensitivity of these conclusions to the assumed cost model. The code and benchmark are open source.

## Metadata
- **Published**: 2026-07-26T23:56:58Z
- **Authors**: Debajyoti Ray, Niranjan Srinivas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23896v1)