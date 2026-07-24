---
title: JANUS: Foreseeing Latent Risk for Long-Horizon Agent Safety
url: http://arxiv.org/abs/2607.19913v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_08-43-43Z_JANUS_ForeseeingLatentRiskforLong_HorizonAgentSafe.md
generated_at: 2026-07-23 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Janus, a foresight‑oriented framework for long‑horizon agent safety that trains guard models to anticipate delayed risks from partial trajectories. The resulting model Vanguard blocks unsafe actions before they are executed and improves safety protection across benchmarks.  

## Key Takeaways
- Janus trains a guard model Vanguard that anticipates delayed risks from partial agent trajectories.  
- The framework uses multi‑agent simulation to synthesize diverse trajectories and learns a shared policy with an anticipation task and an adjudication task.  
- Across four safety benchmarks, Vanguard improves average protection by 15.9 percentage points while increasing benign task completion by 5.1 percentage points.  

## Context
The field of AI safety is shifting from content moderation toward preventing operational failures in long‑horizon agent systems where actions have delayed consequences. This work addresses the challenge of foreseeing risks that manifest after an agent has begun a sequence of steps.  

## Implications
This research shows that foresight mechanisms can be integrated into reinforcement learning agents, offering a path to safer deployment and higher productivity with minimal performance loss. Practitioners may adopt Janus‑based guards to proactively mitigate latent hazards in complex autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19913v1)
