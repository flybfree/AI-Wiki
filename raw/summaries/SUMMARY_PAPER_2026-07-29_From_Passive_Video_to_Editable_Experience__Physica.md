---
title: From Passive Video to Editable Experience: Physically Grounded Experience Synthesis for Embodied Intelligence
url: http://arxiv.org/abs/2607.26903v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_13-35-23Z_FromPassiveVideotoEditableExperience_PhysicallyGro.md
generated_at: 2026-07-29 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Pegasus, a low‑resource framework that translates human manipulation videos into robot‑learnable data by constructing graph representations. It bridges the embodiment gap through structured knowledge transfer and validates performance across multiple robots and benchmarks. The results show reliable cross‑embodiment translation and treat video generation as scalable knowledge transfer.

## Key Takeaways
- Pegasus builds a Task Graph from human videos and converts it into an Affordance and Constraint Graph, producing a Robot Planning Graph that guides robot‑conditioned video synthesis.
- A hierarchical affordance latent space captures relationships among object states, affordances, and tasks, allowing generalization beyond specific object identities.
- The closed‑loop physics verifier filters invalid generations using kinematic feasibility, collision constraints, and joint limits.

## Context
Current embodied AI struggles with the mismatch between human morphology and robot hardware, limiting learning from abundant online videos. This work addresses that bottleneck by reframing video generation as a knowledge transfer problem rather than a data collection challenge.

## Implications
For industry practitioners, Pegasus enables robots to learn from limited robotic datasets using existing human demonstrations, reducing costly sensor‑rich training. The framework’s scalability and cross‑embodiment capability could accelerate robotics research and deployment in real‑world manipulation tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26903v1)
