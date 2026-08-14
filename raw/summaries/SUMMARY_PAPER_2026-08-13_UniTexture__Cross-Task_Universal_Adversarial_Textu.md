---
title: UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models
url: http://arxiv.org/abs/2608.13453v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_16-38-57Z_UniTexture_Cross_TaskUniversalAdversarialTexturesf.md
generated_at: 2026-08-13 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces UniTexture, a cross‑task universal adversarial texture attack that exploits shared visual cues to degrade vision‑language‑action models across multiple manipulation tasks. By backpropagating gradients from the policy’s action outputs through a differentiable renderer, it optimizes a single textured 3D object to steer actions toward attacker‑defined targets without task‑specific textures. Experiments on OpenVLA and π0.5 show mean success rates dropping from 90 % to 48.4 %, demonstrating reliable cross‑suite and cross‑model transfer.

## Key Takeaways
- UniTexture uses a single textured 3D object to cause targeted deviations across multiple tasks, showing that shared vulnerabilities exist.
- The attack optimizes the texture jointly over task, instruction, state, and viewpoint distributions using an action‑space objective rather than per‑task textures.
- Results indicate mean success rates can fall below half (48.4 %) under attack, highlighting severe cross‑task robustness issues.

## Context
Vision‑language‑action models aim to be generalist robotic agents but are vulnerable to adversarial manipulation that could lead to unsafe physical actions. This work shows that such vulnerabilities persist even when the model is not explicitly fine‑tuned for each task, raising questions about the safety of multitask AI systems.

## Implications
For robotics developers, UniTexture underscores the need for cross‑task adversarial testing and texture‑aware defenses in VLA pipelines. Industry practitioners should consider embedding universal adversarial checks to prevent unintended unsafe behaviors across diverse manipulation scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13453v1)
