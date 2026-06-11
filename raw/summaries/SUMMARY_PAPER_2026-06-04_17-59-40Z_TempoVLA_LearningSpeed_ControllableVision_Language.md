---
title: TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies
url: http://arxiv.org/abs/2606.06491v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-04_17-59-40Z_TempoVLA_LearningSpeed_ControllableVision_Language.md
generated_at: 2026-06-11 10:53
model: nvidia/nemotron-3-nano-4b
---

## Summary
TempoVLA introduces a method for controlling the execution speed of vision‑language‑action policies by conditioning on an explicit speed parameter, rather than relying on fixed speeds from demonstrations. The approach combines data augmentation that re‑times trajectories with a model‑side mechanism that injects the desired speed into policy inference.

## Key Takeaways
- Variable‑Speed Trajectory Augmentation (VSTA) can stretch or compress demonstration actions to match any target speed while keeping motion semantics intact, achieving negligible motion error.  
- The model receives the speed condition directly, allowing the predicted action magnitude to dictate how quickly the robot moves.  
- Experiments show that TempoVLA provides flexible bidirectional speed control and improves default performance through better data utilization.

## Context
Current VLA systems treat speed as a static attribute inherited from training data, limiting their ability to adapt to real‑world risk profiles where fast transit is needed alongside slow precision. This paper addresses the gap by treating speed as an explicit controllable variable within the policy loop.

## Implications
For robotics engineers, TempoVLA enables safer operation by automatically slowing down during high‑risk contacts without redesigning models. Practitioners can leverage this flexibility to improve performance across diverse tasks, reducing the need for separate fast and slow policies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.06491v1)
