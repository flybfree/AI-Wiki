---
title: Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking
url: http://arxiv.org/abs/2608.13799v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_22-05-56Z_DynamicMulti_DepotVehicleRoutingwithOnlineRequests.md
generated_at: 2026-08-16 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an event‑driven learning framework that trains Transformer and Masked MLP policies for the Dynamic Multi‑Depot Vehicle Routing Problem with online request arrivals. The benchmark compares these learned policies against deterministic feasibility masking, fixed‑prefix route commitments, dynamic insertion heuristics, and a time‑limited rolling‑horizon optimizer across twenty scenarios. Learned methods completed all requests without invalid actions, yet nearest feasible routing achieved the lowest combined objective and disruption, while rolling horizon reduced waiting times and makespan at higher computational expense.

## Key Takeaways
- Deterministic feasibility masking prevents invalid vehicle‑request assignments by explicitly marking infeasible edges in the policy output.  
- Nearest feasible routing consistently delivered the lowest combined objective value and minimal route disruption across all metrics, outperforming both learned policies and heuristics in overall efficiency.  
- Rolling horizon optimization minimized waiting times and makespan but required substantially more computation, highlighting a trade‑off between responsiveness and resource usage.

## Context
The study addresses a growing need for AI methods that can adapt to rapidly changing routing demands without retraining. Event‑driven Transformers enable online decision making by conditioning on partial information, while rolling horizon provides a classical optimization baseline. This work situates these approaches within the broader AI research agenda of integrating reinforcement learning with real‑time operational constraints.

## Implications
For industry practitioners, the findings suggest that learned policies can be deployed for millisecond‑level decisions and transferred to instances up to 80 requests without retraining, yet they should not replace proven heuristics when computational cost is a concern. Balancing responsiveness against efficiency remains critical as autonomous fleets scale in dynamic logistics environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13799v1)
