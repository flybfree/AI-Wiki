---
title: RASP-QAOA: Resource-Aware Per-Instance Selection for Exact QAOA Simulation
published: 2026-08-06T06:41:41Z
authors: Chih-Chung Hsu
url: http://arxiv.org/abs/2608.05646v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RASP-QAOA: Resource-Aware Per-Instance Selection for Exact QAOA Simulation

## Abstract
Exact QAOA simulation spans several computational representations whose useful regions differ sharply across graph structure, circuit depth, precision, and available memory. Choosing only a backend name hides these differences: an executable choice also fixes the representation, adapter, precision mode, and memory policy. We introduce RASP-QAOA, a per-instance selector over ten such actions. It first removes actions that cannot implement the requested QAOA semantics or execution requirements, then orders the remaining actions using instance features; actions outside learned support are handled by analytical work estimates. On a content-disjoint 60-request H200 evaluation, RASP-QAOA succeeds on all 31 requests for which at least one admissible action completes and validates. Within this set it reaches 27/31 top-1 and 31/31 top-2 selection, with 1.051 geometric-mean regret. Its failure-penalized PAR10 score is 0.0396 times that of development-selected CUAOA (95% interval: 0.0085-0.1644). A separate 30-request crossover shows that graph structure changes 16 decisions and improves the paired penalized score, while a depth-1 stump matches gradient boosting. The evidence supports resource-aware representation selection at n <= 35, p <= 5, with gains driven by representation features rather than classifier complexity.

## Metadata
- **Published**: 2026-08-06T06:41:41Z
- **Authors**: Chih-Chung Hsu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05646v1)