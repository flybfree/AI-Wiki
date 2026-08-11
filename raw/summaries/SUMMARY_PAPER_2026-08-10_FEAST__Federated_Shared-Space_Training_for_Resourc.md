---
title: FEAST: Federated Shared-Space Training for Resource-Heterogeneous Clients
url: http://arxiv.org/abs/2608.09250v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_08-10-59Z_FEAST_FederatedShared_SpaceTrainingforResource_Het.md
generated_at: 2026-08-10 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FEAST, a federated shared-space training framework that learns an elastic supernet composed of subnetworks sized to client budgets. It addresses imbalance in parameter access by jointly training subnetworks within each client's inference limit and uses sparse aggregation for merging slices. Experiments on SuperFedNAS and DeepFedNAS show FEAST achieves 71.06% accuracy at 596M MACs, outperforming baselines.

## Key Takeaways
- FEAST jointly trains multiple subnetworks within each client's limit, sending only relevant supernet portions to reduce traffic.
- The γ-allocation protocol balances training data volumes and inference budgets to prevent accuracy distortion in heterogeneous FL simulations.
- Sub-supernet routing cuts aggregate parameter transmission by 6.8× compared with full supernet sharing.

## Context
Federated learning struggles when clients have varying computational resources, leading to either a single heavy model or many lightweight variants that degrade performance. This paper tackles the problem of parameter access imbalance and inefficient communication in such settings.

## Implications
The γ-allocation protocol offers a practical method for fair resource allocation across diverse devices, improving both fairness and efficiency. For industry practitioners, FEAST enables scalable federated training without sacrificing accuracy or increasing bandwidth costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09250v1)
