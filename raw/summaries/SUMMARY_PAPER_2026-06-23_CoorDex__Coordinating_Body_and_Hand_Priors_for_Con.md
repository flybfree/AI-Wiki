---
title: CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation
url: http://arxiv.org/abs/2606.23680v1
type: paper-summary
date: 2026-06-23
source_paper: 2026-06-22_17-59-20Z_CoorDex_CoordinatingBodyandHandPriorsforContinuous.md
generated_at: 2026-06-23 00:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CoorDex, a learning pipeline that integrates high-dimensional body and hand control into a coordinated latent residual policy for continuous humanoid loco-manipulation. It demonstrates that a Unitree G1 robot with a 20‑DoF WUJI hand can perform tasks like bottle grasping while walking. The approach outperforms traditional methods in dexterous manipulation during locomotion.

## Key Takeaways
- CoorDex converts high-dimensional body and hand demonstrations into latent priors that guide residual control, allowing natural whole-body motion while improving finger-level contact reliability.
- The pipeline uses a frozen proprioception‑conditioned latent prior as the action space for downstream reinforcement learning, which is more effective than joint‑space PPO or monolithic predictions under limited reward budgets.
- Ablations show that only the coordinated latent‑prior interface and residual structure enable high-dimensional contact‑rich loco‑manipulation to be trainable.

## Context
This work addresses a key challenge in humanoid robotics: integrating fine motor control with locomotion without sacrificing stability. By decoupling body motion from hand actions through latent priors, CoorDex aligns with the trend toward modular, differentiable control architectures that support continuous interaction.

## Implications
For industry, CoorDex enables robots to handle objects autonomously while moving, reducing reliance on stop‑and‑go cycles and improving safety. Practitioners can adopt the latent‑prior framework to design more flexible humanoid systems capable of complex tasks in real environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.23680v1)
