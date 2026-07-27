---
title: SceneActBench: Can Agents Act on the 3D Scenes They See?
url: http://arxiv.org/abs/2607.22393v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_15-16-47Z_SceneActBench_CanAgentsActonthe3DScenesTheySee.md
generated_at: 2026-07-26 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SceneActBench, a benchmark that tests vision-language agents' ability to act on multi-object 3D scenes using visual inputs and optional 3D assets. Agents perform actions in an agent-environment loop, and their outcomes are compared to hidden ground truth via geometric metrics across eleven VLM configurations.

## Key Takeaways
- SceneActBench evaluates full multi-object 3D scene actions rather than single-object tasks, providing a unified evaluation framework.
- The benchmark includes five 3D tasks derived from 210 source instances and 520 task cases with paired input conditions to ensure comprehensive testing.
- Across eleven proprietary VLM configurations the overall scores range from 38.6 to 50.2, indicating no model performs consistently well.

## Context
This work addresses a gap in current AI benchmarks that focus on textual descriptions or isolated object manipulations, highlighting the need for holistic assessment of agent behavior in complex 3D environments. By integrating visual and geometric metrics, SceneActBench offers a more realistic measure of multimodal reasoning.

## Implications
For researchers developing VLM agents, the findings suggest that performance cannot be assumed to transfer across diverse 3D tasks without careful evaluation. Practitioners should adopt such benchmarks to guide model design and deployment in real-world interactive systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22393v1)
