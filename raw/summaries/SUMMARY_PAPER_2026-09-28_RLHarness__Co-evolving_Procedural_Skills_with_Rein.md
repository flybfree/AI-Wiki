---
title: RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning
url: http://arxiv.org/abs/2609.32326v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_07-42-16Z_RLHarness_Co_evolvingProceduralSkillswithReinforce.md
generated_at: 2026-09-28 22:08
model: qwen3.6-35b-a3b
---

## Summary
RLHARNESS addresses the program cold-start problem and the staleness of fixed skill banks in long-horizon multimodal reasoning by introducing a co-evolutionary framework that alternates policy learning with dynamic Harness reconstruction. The method organizes skills, protocols, demonstrations, and task contracts into a unified versioned structure, ensuring external procedural guidance remains consistent with an evolving policy. This approach yields significant accuracy and F1 score improvements across multiple tasks, demonstrating that continuous alignment between the policy and its supporting program is essential for robust reasoning performance.

## Key Takeaways
- RLHARNESS employs a two-phase co-evolution cycle where an initial Exploration-Distillation Harness builds verified traces for supervised fine-tuning, followed by a Post-RL Reconstruction Harness that rebuilds skills, execution protocols, and demonstrations from fresh rollouts to maintain alignment with the updated policy during DAPO II adaptation.
- The framework mitigates the limitations of terminal-only reinforcement

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32326v1)
