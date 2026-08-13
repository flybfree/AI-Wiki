---
title: Adaptation of Generalist Robot Policies with Minimal Data
url: http://arxiv.org/abs/2608.11363v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_19-15-26Z_AdaptationofGeneralistRobotPolicieswithMinimalData.md
generated_at: 2026-08-12 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MiDAS, a method for adapting robot policies from a single demonstration to new tasks through minimal human guidance and subsequent autonomous online learning. By combining behavior cloning with value‑based online RL on a residual policy, MiDAS recovers strong task performance and demonstrates robust improvement over several hours of interaction. This work provides the first reliable demonstration that robots can adapt from just one task demonstration.

## Key Takeaways
- MiDAS enables adaptation from as little as one demonstration by first cloning behavior onto the target task and then fine‑tuning a residual policy online, achieving strong performance on both LIBERO and RoboCasa.  
- The method generalizes beyond demonstrated conditions, showing that learned policies can handle unseen variations without additional human data.  
- Starting from a fragile low‑success policy, MiDAS improves robustness and learns new successful behaviors within ~6 hours of autonomous interaction.

## Context
Fully autonomous robot learning remains challenging due to sparse rewards and weak zero‑shot exploration. This paper addresses the minimal‑data adaptation regime as a tractable proxy for such autonomy, offering insights into how limited human feedback can bootstrap self‑improving policies. The approach aligns with broader trends toward sample‑efficient and online reinforcement learning.

## Implications
For robotics engineers, MiDAS reduces reliance on extensive task‑specific data collection, accelerating deployment in real‑world settings. Practitioners can leverage this framework to create robots that quickly adapt to new environments or tasks using minimal supervision. The method also supports scalable training pipelines where human feedback is costly but occasional demonstrations suffice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11363v1)
