---
title: Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation
url: http://arxiv.org/abs/2609.01596v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-58-07Z_Facet_0_ARoboticFoundationModelforContact_RichPrec.md
generated_at: 2026-09-01 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
Facet-0 is a robotic foundation model that predicts how its actions will affect contact with objects and learns to value those consequences. The system combines multimodal representation learning with reinforcement learning over Cartesian commands while maintaining an auxiliary wrench head for contact prediction. On five sub‑millimeter assembly tasks it achieves 82% success, 0.5 mm placement accuracy, and 50 ms latency.

## Key Takeaways
- Facet-0 unifies vision‑language semantics with kinematic state to generate action chunks that are paired with the expected future wrench profile.
- The distributional Action‑Wrench Critic learns to differentiate motions that progress tasks similarly but produce different contact outcomes, guided by phase‑aware rewards and credit assignment focused on decisive interactions.
- A lightweight bounded actor reuses frozen representations for part‑specific adaptation, keeping RL defined over executable Cartesian actions while preserving a non‑commanded wrench head.

## Context
The paper addresses the challenge of achieving sub‑millimeter precision in real‑world robotics where contact reliability is critical. By integrating causal wrench prediction with reinforcement learning, it moves beyond simple command execution toward a model that anticipates and values physical interactions.

## Implications
This work demonstrates that foundation models can guide precise manipulation without explicit fine‑tuning for each part, reducing development time. For industry, the 82% success rate shows feasibility of high‑accuracy assembly robots in manufacturing cells with minimal latency overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01596v1)
