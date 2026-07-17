---
title: RoboTTT: Context Scaling for Robot Policies
url: http://arxiv.org/abs/2607.15275v1
type: paper-summary
date: 2026-07-16
source_paper: 2026-07-16_17-59-06Z_RoboTTT_ContextScalingforRobotPolicies.md
generated_at: 2026-07-16 23:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
RoboTTT introduces a robot foundation model that extends the visuomotor context from single-step to eight thousand timesteps, achieving three orders of magnitude beyond current methods while keeping inference latency unchanged. The approach enables one‑shot imitation from human video demonstrations and fully completes a five‑minute ten‑stage assembly task, improving overall performance by 87% over a baseline with only one‑step context.

## Key Takeaways
- RoboTTT allows one‑shot in‑context imitation using human video demonstrations as the sole training signal.  
- The model can improve its policy on the fly during inference, adapting to new tasks without retraining.  
- Extending pretraining context length yields steady gains in closed‑loop performance across longer tasks.

## Context
Robot foundation models have traditionally been limited by short memory horizons, similar to early large language models. RoboTTT demonstrates that scaling context can unlock capabilities previously thought impossible for robots, aligning with the trend of multi‑modal LLMs handling long sequences.

## Implications
For researchers this paper establishes a new scaling axis beyond model size, showing that longer contexts improve robot performance without latency penalties. In industry, it opens pathways to autonomous systems performing complex, prolonged tasks such as assembly lines or surgical procedures where continuous adaptation is essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15275v1)
