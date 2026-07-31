---
title: Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors
url: http://arxiv.org/abs/2607.28525v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-01-20Z_SameGraphCross_TaskTransferinGNNs_ProtocolsandPred.md
generated_at: 2026-07-30 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper formalizes same-graph node classification (NC) and link prediction (LP) transfer in graph neural networks, addressing unreliable prior evaluations that use incompatible splits or negative sampling. It introduces a leakage‑free protocol that shares a message‑passing encoder while excluding evaluated edges and uses fixed negatives for LP. Experiments across GCN, GraphSAGE, and GPS show NC→LP is consistently beneficial on homophilic graphs, whereas LP→NC often harms performance unless the graph is structure‑dominant.

## Key Takeaways
- The leakage‑free protocol fixes node and edge splits and excludes evaluated edges from the shared message passing to prevent information leakage.  
- Transfer direction matters: NC to LP improves accuracy on homophilic graphs, but LP to NC can degrade it under naive representation reuse.  
- In a structure‑dominant regime where LP is easy but NC is undersaturated, LP→NC becomes reliably positive, indicating that LP can act as structural pretraining.

## Context
Graph neural networks aim to learn from heterogeneous graph data, yet few studies explore how one task can inform another when they share the same underlying graph. This work contributes a principled protocol and metrics for evaluating such cross‑task transfer, filling a gap in reliable evaluation practices.

## Implications
For practitioners, the CoTask Score provides a simple statistical guide to selecting mechanisms that avoid negative transfer, enabling more efficient model design. In industry, leveraging LP as pretraining could reduce data requirements for downstream NC tasks, offering cost savings and improved performance on real‑world graph applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28525v1)
