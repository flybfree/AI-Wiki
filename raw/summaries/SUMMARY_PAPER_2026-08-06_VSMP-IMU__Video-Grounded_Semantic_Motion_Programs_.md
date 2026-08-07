---
title: VSMP-IMU: Video-Grounded Semantic Motion Programs for Sensor-Aware Synthetic IMU Generation
url: http://arxiv.org/abs/2608.05782v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_09-16-06Z_VSMP_IMU_Video_GroundedSemanticMotionProgramsforSe.md
generated_at: 2026-08-06 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces VSMP‑IMU, a video‑grounded framework that creates synthetic IMU signals for human activity recognition. It achieves higher performance than real data alone and outperforms prior synthetic baselines across multiple datasets.

## Key Takeaways
- The structured Semantic Motion Program (SMP) separates activity semantics from label preservation, enabling controlled synthetic motion generation.
- VSMP‑IMU improves macro‑F1 scores by over 4 % compared to the strongest prior synthetic baseline and by more than 6 % in low‑resource settings with reduced samples.
- The framework boosts tail‑class performance by nearly 20 % on imbalanced datasets, demonstrating strong generalization.

## Context
Synthetic sensor data is increasingly used to augment limited labeled recordings for wearable activity recognition. However most methods either rely solely on video or text, leading to trade‑offs in realism and controllability. VSMP‑IMU addresses this gap by combining visual grounding with structured motion semantics.

## Implications
This work provides a practical method for generating realistic IMU signals that can be directly used in HAR models without costly real data collection. Practitioners can leverage it to improve model robustness, especially in low‑resource or long‑tail scenarios, accelerating research and deployment of wearable AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05782v1)
