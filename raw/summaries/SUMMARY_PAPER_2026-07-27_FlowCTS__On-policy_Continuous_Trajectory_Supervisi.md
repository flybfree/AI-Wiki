---
title: FlowCTS: On-policy Continuous Trajectory Supervision of Flow Models
url: http://arxiv.org/abs/2607.24522v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_15-03-22Z_FlowCTS_On_policyContinuousTrajectorySupervisionof.md
generated_at: 2026-07-27 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Flow Continuous Trajectory Supervision (FlowCTS), an on‑policy method that matches student and reference trajectories from the same visited state to improve flow model training. Using integral relations between trajectories and velocity fields, it derives a temporally weighted velocity‑matching bound discretized into supervision steps. Experiments show FlowCTS‑OPD outperforms vanilla KL‑based OPD in GenEval, OCR, PickScore and beats mixed‑reward RL baselines.

## Key Takeaways
- FlowCTS matches subsequent student and reference trajectories initialized from the same visited state to eliminate exposure bias and sparse reward issues.  
- The method leverages an integral relation between trajectories and velocity fields, providing a temporally weighted velocity‑matching upper bound that is discretized into practical objectives controlled by supervision steps.  
- Under multi‑reference settings FlowCTS‑OPD improves GenEval from 0.90 to 0.93, OCR from 0.90 to 0.92 and PickScore from 22.75 to 23.06 while beating vanilla KL‑based OPD and mixed‑reward RL baselines.

## Context
Flow models are increasingly used for generative AI tasks where training with sparse rewards is challenging. Traditional on‑policy distillation methods like OPD have been adapted for language models but lack a trajectory‑aware formulation for flow networks, limiting their effectiveness. This work bridges that gap by providing a continuous trajectory supervision framework tailored to flow models.

## Implications
For practitioners developing flow‑based generative systems, FlowCTS offers a concrete way to reduce exposure bias and improve convergence without extensive reward engineering. The method’s scalability across multi‑reference setups suggests it could become a standard component in on‑policy distillation pipelines for continuous latent space generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24522v1)
