---
title: Sub-Quadratic Bisimulation Metrics via Approximate Nearest Neighbors: Coverage-Augmented Guarantees and Computable Two-Sided Certificates
published: 2026-08-07T03:32:40Z
authors: Ibne Farabi Shihab, Joyanta Jyoti Mondal
url: http://arxiv.org/abs/2608.06762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sub-Quadratic Bisimulation Metrics via Approximate Nearest Neighbors: Coverage-Augmented Guarantees and Computable Two-Sided Certificates

## Abstract
Bisimulation metrics quantify behavioral similarity in Markov decision processes, but their Wasserstein fixed-point operator updates every state pair and incurs quadratic pairwise work. We give a certificate-carrying sub-quadratic method for MDPs with bounded transition support and a useful low-dimensional indexing representation: an approximate-nearest-neighbor index selects the pairs updated by the exact restricted operator, while monotone lower and upper runs enclose the exact metric at every sweep. The main analytical result is a coverage-augmented anytime bound: local index quality alone cannot control global error, because uncovered pairs retain their initialization gap. The limiting error is at most $\max(ρ,\eop/(1-γ))$, and with exact covered backups the lower arm satisfies $\|\dann-d\|_\infty=ρ$. Because $ρ$ depends on the unknown exact metric, the algorithm returns the observable sandwich width instead; agreement of the induced lower and upper clusterings certifies exact recovery of the covered aggregation. A reward-oblivious lower bound shows sub-quadratic index-first coverage cannot remove the coverage term, while a separate adaptive lower bound requires $Ω(|\Scal|)$ pair evaluations. Exact-operator experiments verify the identity and enclosure in every seeded run, and timing experiments recover quadratic versus sub-quadratic scaling under both cheap and full Wasserstein backups. On the grouped $|\Scal|=64$ benchmark, exact restricted refinement reaches the exact-metric skyline once retrieval covers roughly half of all pairs, while independently trained MICo and DBC baselines stay $22$-$33\times$ above that skyline at every retrieval budget. Taxi shows the certificate abstaining under an uninformative embedding, while a $2500$-state gridworld improves over a reward-only metric by $28.6\%$ using $12.8\%$ of one quadratic sweep.

## Metadata
- **Published**: 2026-08-07T03:32:40Z
- **Authors**: Ibne Farabi Shihab, Joyanta Jyoti Mondal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06762v1)