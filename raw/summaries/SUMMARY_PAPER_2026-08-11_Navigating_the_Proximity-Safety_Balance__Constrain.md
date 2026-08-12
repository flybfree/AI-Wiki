---
title: Navigating the Proximity-Safety Balance: Constraint Decomposition for Human Following in Pedestrian Crowds
url: http://arxiv.org/abs/2608.10056v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_17-59-15Z_NavigatingtheProximity_SafetyBalance_ConstraintDec.md
generated_at: 2026-08-11 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a multi‑constraint reinforcement learning framework that explicitly balances proximity to a target pedestrian with safety in dense crowds by decomposing the task into a sparse reward and independent cost constraints. It integrates predicted uncertainty of human motion into the constraints, enabling tunable control over the trade‑off without relying on implicit reward weighting. Experiments show improved performance compared to baselines both in simulation and real‑world deployment.

## Key Takeaways
- The method separates proximity and safety objectives into a sparse task reward and explicit cost thresholds that have direct behavioral meaning, allowing precise tuning of each constraint.
- Human motion prediction uncertainty is quantified and fed directly into the RL costs, enhancing safety when pedestrian behavior is unpredictable.
- The approach yields an effective proximity‑safety balance across in‑distribution and out‑of‑distribution settings, validated by real‑robot deployment.

## Context
Current human following systems treat competing goals as a single dense reward, making the trade‑off opaque and difficult to adjust. This limits adaptability to varying crowd densities and unpredictable behaviors. The proposed decomposition aligns with broader efforts toward interpretable and controllable RL policies for safety‑critical robotics.

## Implications
For industry, this framework offers a clear mechanism to balance closeness and safety, improving both user experience and collision avoidance in autonomous navigation robots. Practitioners can tune constraints independently, enabling deployment in diverse real‑world scenarios where human unpredictability is high.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10056v1)
