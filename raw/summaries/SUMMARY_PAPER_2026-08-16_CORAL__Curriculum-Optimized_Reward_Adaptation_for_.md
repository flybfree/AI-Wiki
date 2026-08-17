---
title: CORAL: Curriculum-Optimized Reward Adaptation for LiDAR-Based Goal-Directed Urban Driving
url: http://arxiv.org/abs/2608.14332v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_14-22-05Z_CORAL_Curriculum_OptimizedRewardAdaptationforLiDAR.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CORAL, a curriculum‑optimized reinforcement learning framework for LiDAR‑based urban driving that combines a progressive five‑stage curriculum with stage‑aware reward shaping to balance multiple competing behaviors. The approach achieves 100 % success on the longest routes under full constraints, outperforming PPO baselines by large margins, and transfers zero‑shot to seven unseen towns with high performance.

## Key Takeaways
- CORAL’s five‑stage curriculum progressively lengthens routes and tightens behavioral constraints, enabling the policy to learn complex tasks step by step.  
- The stage‑aware reward dynamically shifts component weights from mission progress toward route following, safety, smoothness, and rule compliance as the task becomes harder.  
- Neither schedule alone improves performance; disabling both drops success to 55 %, highlighting that their combination is essential.

## Context
Autonomous urban driving requires policies that handle long‑horizon goals while satisfying multiple constraints, a challenge for fixed‑objective reinforcement learning. This work demonstrates how curriculum design and reward engineering can overcome such trade‑offs without resorting to point‑cloud or bird’s‑eye‑view encoders.

## Implications
The findings suggest that curriculum‑aware reward adaptation is a viable path toward robust, transferable autonomous driving agents in real‑world environments. Practitioners can adopt similar staged curricula and modular reward shaping to improve generalization across diverse urban settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14332v1)
