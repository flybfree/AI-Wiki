---
title: GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation
url: http://arxiv.org/abs/2608.19759v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_08-03-39Z_GOAG_GenerativeandObject_AgnosticGraspPlannerforDe.md
generated_at: 2026-08-20 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GOAG, a generative and object-agnostic grasp planner that learns a compact latent representation of a gripper’s contact surface distribution to sample valid grasps without requiring object-specific training. Experiments on the MultiDex dataset show an average success rate of 86.93% with significantly faster processing than comparable data-driven methods.

## Key Takeaways
- GOAG learns a compact latent representation of the gripper's contact surface distribution, enabling efficient sampling of valid grasp configurations independent of object features.
- The model only uses object features at inference time to retrieve admissible contact areas compatible with the gripper’s capabilities.
- The approach achieves state-of-the-art results on MultiDex with an average success rate of 86.93% and significantly faster processing when generating numerous grasps compared to data-driven planners.

## Context
Generative grasp planning is a key challenge in multi-fingered robotics, where generalization across diverse objects remains limited by object-specific training. This work advances the field by decoupling gripper geometry learning from object perception. The decoupling also enables the reuse of learned surface representations across different robotic platforms, fostering modular design.

## Implications
For industry, this reduces reliance on extensive dataset collection for each new object, accelerating deployment of robotic arms. Practitioners can implement a single planner that works across varied grippers and objects, lowering development time and cost. Such modularity translates into lower maintenance costs and faster adaptation to new tasks in real-world factories.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19759v1)
