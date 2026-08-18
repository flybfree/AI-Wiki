---
title: Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain
url: http://arxiv.org/abs/2608.16164v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_06-30-45Z_Trajectory_LevelAutomaticCurriculumLearningforLegg.md
generated_at: 2026-08-17 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a trajectory-level automatic curriculum learning framework for teaching legged locomotion on unstructured terrain. It learns a difficulty function that guides the selection of new tasks, improving success rates significantly compared to training without curriculum or using handcrafted curricula.

## Key Takeaways
- The evaluator learns a difficulty score for each trajectory task, enabling an adaptive curriculum that matches policy evolution.
- Curriculum updates are driven by the learned evaluator, forming a closed loop between policy and task selection.
- Quantitative results show a 56.3% increase in success rate over direct training and up to 39.74% improvement on diverse approach directions.

## Context
Automatic curriculum learning is crucial for complex robotics tasks where environment difficulty cannot be predefined. This work addresses the gap between heuristic curricula designed for parameterized terrains and real-world unstructured settings, highlighting the need for data-driven adaptation.

## Implications
The framework provides a scalable method for training robots on unpredictable environments without manual difficulty ordering. Practitioners can integrate this approach to boost performance in autonomous navigation and exploration applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16164v1)
