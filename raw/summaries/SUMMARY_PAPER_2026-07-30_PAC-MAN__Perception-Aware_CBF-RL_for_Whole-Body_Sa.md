---
title: PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball
url: http://arxiv.org/abs/2607.28623v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-59-35Z_PAC_MAN_Perception_AwareCBF_RLforWhole_BodySafetyi.md
generated_at: 2026-07-30 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PAC-MAN, a perception‑aware CBF‑RL framework that couples safety constraints with real‑time sensor data on a humanoid dodgeball robot. Experiments show the policy can evade collisions within a few points of an oracle using only segmented depth, and it works well in both single throws and repeated throw cycles.

## Key Takeaways
- The joint CBF barrier improves performance when accurate ball states are available but degrades under fixed‑camera observations unless supplemented with tracking aids. - A lightweight Link‑CBF policy can be deployed zero‑shot on the Unitree G1 and succeeds on 95 % of throws despite imperfect perception. - Semantic segmentation enables evasion of different balls by providing clear spatial cues.

## Context
This work bridges reinforcement learning safety guarantees with embodied robotics, demonstrating that clearance constraints can guide training even when the final policy relies solely on limited visual input. It highlights a shift toward perception‑driven safety in mobile humanoid platforms where real‑world sensor noise is inevitable and emphasizes the value of lightweight, zero‑shot deployments.

## Implications
For industry, PAC-MAN shows that safety can be baked into RL pipelines without requiring full privileged state access, lowering development cost for safe navigation systems. Practitioners may adopt similar CBF‑RL hybrids to ensure robust behavior on unstructured tasks like dodgeball or obstacle avoidance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28623v1)
