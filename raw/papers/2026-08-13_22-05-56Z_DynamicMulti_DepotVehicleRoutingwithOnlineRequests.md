---
title: Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking
published: 2026-08-13T22:05:56Z
authors: Faezeh Ardali, Gerald M. Knapp
url: http://arxiv.org/abs/2608.13799v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Multi-Depot Vehicle Routing with Online Requests: Event-Driven Transformer--DRL and Rolling-Horizon Benchmarking

## Abstract
This paper presents an event-driven learning and benchmarking framework for the Dynamic Multi-Depot Vehicle Routing Problem with progressively revealed requests and evolving vehicle states. Masked MLP and Transformer policies are trained through behavior cloning and proximal policy optimization. Deterministic feasibility masking prevents invalid vehicle--request assignments, while fixed-prefix/flexible-suffix route commitments protect completed, active, and near-term decisions and separately measure vehicle reassignment and resequencing. The learned policies are compared with dynamic insertion heuristics and time-limited rolling-horizon optimization. In a 20-scenario policy benchmark, all methods completed every request without invalid actions, but nearest feasible achieved the lowest mean objective and outperformed the learned policies in routing quality, waiting time, stability, makespan, and runtime. Across five independent training runs, PPO had little average effect on the MLP and improved the Transformer on average, although with greater seed variability. Under the common protocol, nearest feasible achieved the lowest combined objective and route disruption, whereas rolling horizon achieved the lowest waiting times and makespan at substantially higher computational cost. The learned policies retained millisecond-level decisions and transferred to instances with up to 80 requests without retraining, but did not outperform the strongest heuristic. No single method was best across routing efficiency, service responsiveness, stability, and online computation.

## Metadata
- **Published**: 2026-08-13T22:05:56Z
- **Authors**: Faezeh Ardali, Gerald M. Knapp
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13799v1)