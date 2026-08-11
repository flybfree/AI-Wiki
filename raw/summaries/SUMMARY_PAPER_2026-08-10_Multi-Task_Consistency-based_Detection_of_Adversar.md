---
title: Multi-Task Consistency-based Detection of Adversarial Attacks
url: http://arxiv.org/abs/2608.07750v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-07_20-33-16Z_Multi_TaskConsistency_basedDetectionofAdversarialA.md
generated_at: 2026-08-10 22:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a multi-task consistency-based detection scheme that leverages the mismatch between inference outputs of different vision tasks to identify adversarial perturbations. By computing a consistency score across task pairs, it selects optimal model combinations for robust detection. Experiments on BDD100k show a ROC-AUC of 99.9% against PGD attacks.

## Key Takeaways
- The method uses inconsistency between object detection and instance segmentation outputs as a reliable signal for adversarial presence.
- A consistency score metric quantifies how far the predictions diverge, enabling automated detection thresholds.
- The approach achieves near-perfect detection (ROC-AUC 99.9%) on the validation set with minimal computational overhead.

## Context
Vision systems in autonomous driving rely on multiple perception tasks that share neural architectures but produce distinct outputs. Adversarial attacks can corrupt these outputs independently, making consistency a natural diagnostic cue. This work addresses the need for lightweight defenses that do not require full model retraining or heavy inference costs.

## Implications
Practitioners can integrate this detection into resource-constrained pipelines without sacrificing performance, improving safety in real-time applications. The method's scalability across task pairs suggests broader applicability to other multi-task vision architectures, fostering more resilient AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07750v1)
