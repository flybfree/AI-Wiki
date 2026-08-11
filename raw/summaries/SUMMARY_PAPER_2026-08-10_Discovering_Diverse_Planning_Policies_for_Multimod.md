---
title: Discovering Diverse Planning Policies for Multimodal Embodied Agents with Quality-Diversity Optimization
url: http://arxiv.org/abs/2608.08523v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_06-41-53Z_DiscoveringDiversePlanningPoliciesforMultimodalEmb.md
generated_at: 2026-08-10 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a Quality-Diversity framework to discover diverse planning policies for multimodal embodied agents that integrate vision, text, and interaction history. Experiments on ThreeDWorld transport show the method boosts both task success rates and reduces unnecessary interactions compared with baseline planners.

## Key Takeaways
- The method treats planning-policy templates as evolvable individuals organized in a behavior-indexed archive rather than using a single prompt style.
- Rollout trajectories are summarized into structured success and failure experiences to guide policy variation via recombination and mutation.
- The highest-quality policy for each niche defined by interaction intensity and goal-directedness is retained, enabling online fallback when stalls occur.

## Context
Multimodal embodied agents must plan across visual inputs, textual goals, and past actions while adapting in real time. Current approaches often lock into one planning mode, leading to stagnation. This work addresses the need for adaptable, modular strategies within a single agent framework.

## Implications
Practitioners can implement policy switching to improve robustness without retraining large models. The approach offers a template for designing resilient AI systems that recover gracefully from failure and maintain efficiency across diverse environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08523v1)
