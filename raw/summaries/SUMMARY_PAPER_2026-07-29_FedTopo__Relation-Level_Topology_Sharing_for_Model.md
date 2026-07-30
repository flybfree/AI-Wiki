---
title: FedTopo: Relation-Level Topology Sharing for Model-Heterogeneous Federated Learning
url: http://arxiv.org/abs/2607.26801v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_11-39-21Z_FedTopo_Relation_LevelTopologySharingforModel_Hete.md
generated_at: 2026-07-29 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
FedTopo introduces a new approach for federated learning that shares class relation topology instead of model parameters or prototypes, enabling reliable knowledge transfer across clients with heterogeneous backbones. The method builds local topology from client‑specific prototypes and uploads it together with class statistics, which the server aggregates in a reliability‑aware fashion to produce a global topology. Experiments on three datasets with eight diverse architectures show that FedTopo outperforms baseline methods while keeping communication low and avoiding inference overhead.

## Key Takeaways
- The paper proposes encoding global knowledge as class relation topology rather than absolute feature values, allowing alignment across different client models.
- Each client constructs its own topology from local prototypes and shares it with the server along with class statistics for aggregation.
- The aggregated global topology is used to bias local training toward negative classes that share similar relational patterns.

## Context
Federated learning struggles when clients use diverse network architectures because shared parameters or prototypes assume a common representation space. Existing solutions often require costly alignment steps or ignore heterogeneity, limiting scalability and robustness in real‑world deployments.

## Implications
This work demonstrates that topology‑based sharing can be as effective as parameter sharing while reducing communication burden, offering a practical path for heterogeneous federated ecosystems. Practitioners may adopt FedTopo to improve convergence speed and generalization without centralizing raw data or heavy inference.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26801v1)
