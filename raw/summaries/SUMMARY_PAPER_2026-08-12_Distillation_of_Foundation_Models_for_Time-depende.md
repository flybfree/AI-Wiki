---
title: Distillation of Foundation Models for Time-dependent PDEs
url: http://arxiv.org/abs/2608.11937v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_11-24-08Z_DistillationofFoundationModelsforTime_dependentPDE.md
generated_at: 2026-08-12 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Teacher Rollout Extension (TREX) as a knowledge distillation method that compresses large foundation models for time-dependent PDEs into efficient student networks. It shows that students can match or exceed teacher accuracy while using far fewer parameters and faster inference. The approach generates synthetic long trajectories from the teacher rollout distribution, optionally with noise injection.

## Key Takeaways
- TREX augments limited downstream data by generating long synthetic trajectories through teacher rollouts, allowing the student to learn behavior around states encountered during autoregressive prediction.
- The method reduces model size by several orders of magnitude without sacrificing predictive capability, achieving more than an order-of-magnitude speedup in inference.
- Students can incorporate task-specific inductive biases such as equivariance that teachers do not enforce.

## Context
Foundation models for PDEs have demonstrated strong generalization across diverse physical systems, yet their large size hampers real-time applications. This work addresses the trade‑off between accuracy and computational cost by distilling knowledge into lightweight surrogates suitable for fast numerical solvers.

## Implications
The distilled students enable rapid prototyping and deployment of PDE solvers in resource‑constrained environments such as robotics, climate modeling, and autonomous control. Practitioners can now obtain high‑fidelity predictions with minimal latency and memory footprint, accelerating research cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11937v1)
