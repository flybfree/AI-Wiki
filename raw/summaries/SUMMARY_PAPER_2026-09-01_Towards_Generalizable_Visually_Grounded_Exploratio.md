---
title: Towards Generalizable Visually Grounded Exploration of Household Devices
url: http://arxiv.org/abs/2609.00845v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_07-42-45Z_TowardsGeneralizableVisuallyGroundedExplorationofH.md
generated_at: 2026-09-01 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VGEBench, a benchmark for evaluating generalizable visually grounded exploration of household devices by VLMs. It shows that current models struggle to translate semantic knowledge into physical actions and maintain long-horizon state tracking. The authors demonstrate the need for active visual perception and feedback-driven correction.

## Key Takeaways
- Existing benchmarks rely on static annotated trajectories, ignoring the dynamic hypothesis-interaction-refinement loop required for functional device operation.
- Current VLMs face significant challenges in translating abstract world knowledge into concrete physical execution of novel devices.
- The Logic-Driven State Machine framework creates multi-turn interaction loops that force agents to ground abstract knowledge into fine-grained visual affordances.

## Context
The rapid progress of Vision-Language Models has shifted research toward embodied AI, yet most evaluation methods remain static and document-driven. This work highlights a gap in measuring true generalization beyond pre-programmed instructions. The paper contributes a dynamic framework that better reflects real-world interaction complexity.

## Implications
For industry practitioners, VGEBench offers a practical tool to assess whether their models can operate devices without manuals. For researchers, it pushes the field toward more realistic benchmarks that capture active perception and iterative learning. This could accelerate development of truly autonomous household robots.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00845v1)
