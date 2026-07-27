---
title: "Summary: On-Policy Distillation"
date: 2025-10-27
type: source-note
tags: [thinking-machines, source-note, distillation, post-training, reasoning]
source_url: https://thinkingmachines.ai/blog/on-policy-distillation/
---

# Summary: On-Policy Distillation

**Source**: [Thinking Machines Lab](https://thinkingmachines.ai/blog/on-policy-distillation/)

Saved: 2026-07-27 10:58

## Summary
Thinking Machines presents on-policy distillation as a good middle ground between autonomous reinforcement learning and plain offline imitation. The post argues for dense supervision on model-generated rollouts so smaller student models can inherit expert behavior more reliably.

## Key Takeaways
- On-policy distillation uses the model's own generated trajectories as the training substrate.
- Dense supervision is presented as especially useful for distilling reasoning and personalization.
- The post frames on-policy distillation as a practical way to train compact, deployable models.

## Context
Smaller models matter when you care about privacy, deployment cost, and iteration speed.
The post is basically saying that the student should learn from rollouts that are close to the behavior you actually want in production.

## Implications
This is a useful pattern for post-training pipelines that want a compact model to preserve high-quality behavior without relying purely on offline imitation or expensive RL loops.
It also lines up with the broader trend toward agentic, continually updated systems.
