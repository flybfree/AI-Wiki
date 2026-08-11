---
title: BDH-CQ: In-Context Learning with Recurrent Latent Reasoning
url: http://arxiv.org/abs/2608.09888v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_17-39-16Z_BDH_CQ_In_ContextLearningwithRecurrentLatentReason.md
generated_at: 2026-08-10 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents BDH-CQ, a model that merges in-context learning with recurrent latent reasoning. It updates its memory continuously as new inputs arrive and solves queries iteratively within a high‑dimensional latent space without verbalizing steps. The 150M‑parameter version achieves 29.5% pass@2 on ARC‑AGI‑1 at $0.0007 per task, surpassing prior cost‑accuracy trade‑offs. The approach avoids explicit token‑by‑token generation, reducing latency and hardware load.

## Key Takeaways
- BDH-CQ continuously updates its recurrent memory during inference, enabling iterative computation in latent space.
- The model reaches 29.5% pass@2 on ARC‑AGI‑1 with a compute cost of $0.0007 per task, breaking the previous Pareto frontier.
- It demonstrates that high accuracy can be achieved at very low inference expense.

## Context
The field is moving toward models that balance performance and efficiency, especially as deployment costs become critical. This work shows that recurrent latent reasoning can close the gap between raw capability and cost. This work aligns with trends toward efficient model compression and on‑device inference.

## Implications
For industry practitioners, this model suggests a path to deploying large language systems with minimal operational spend while maintaining strong benchmark scores. Researchers may explore similar architectures for other low‑cost reasoning tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09888v1)
