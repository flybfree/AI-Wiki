---
title: When Graph-JEPA Learns the Wrong Thing: Diagnosing and Repairing Category-Conditional Collapse
published: 2026-08-20T19:22:49Z
authors: Gollam Rabby, Sören Auer
url: http://arxiv.org/abs/2608.20516v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Graph-JEPA Learns the Wrong Thing: Diagnosing and Repairing Category-Conditional Collapse

## Abstract
Joint-embedding predictive architectures are selected almost universally by linear probing and effective rank. We report a case where both read healthily while the representation carries zero usable instance information. We repair it, and a second failure appears: the repaired metric saturates on a target carrying no structural information. Our corpus is a scientific-reasoning graph over 57,903 articles, each a subgraph. A Graph-JEPA predicts one masked aspect from a subgraph's remaining aspects, attaining linear-probe accuracy 0.871 and effective rank 18-47, yet retrieval recovers 0.00 of 14.4 bits (MRR 1.9e-4 vs chance 1.99e-4, p=0.98). Three upper bounds on the same pool and code recover nearly everything (+14.28, +14.34, +14.22 bits), ruling out corpus, masking, pool, and metric as causes. We trace this to variance allocation - frozen inputs place 86.05% of variance on subgraph identity and 0.40% on aspect identity, while trained latents place 0.39% and 99.61%. This is a property of the objective's optimum: the degenerate solution is a global minimum of the coupled predictor/EMA-target objective, present already at init. A repaired configuration reaches 14.377 of 14.379 bits, above the 13.865-bit oracle; reverting the loss to regression drops it to 0.307 bits, confirming it. Yet the repair licenses nothing about reasoning: the target is reducible, since intra-subgraph edges are a deterministic function of node census. The oracle reaches 96.4% of the ceiling, and our largest effect is the learning-rate schedule, not architecture. Bits and a reasoning probe show no relation across ten cells. A data-derived target fails a quality gate - 25.96% of nodes are duplicate placeholders, and the rest is more generic than supporting evidence. Rank, probes, and metrics can all saturate on an unsupportive evaluation. We release a harness with a reducibility audit and target gate.

## Metadata
- **Published**: 2026-08-20T19:22:49Z
- **Authors**: Gollam Rabby, Sören Auer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20516v1)