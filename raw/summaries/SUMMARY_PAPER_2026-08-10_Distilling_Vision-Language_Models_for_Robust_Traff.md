---
title: Distilling Vision-Language Models for Robust Traffic Sign Perception in Autonomous Vehicles
url: http://arxiv.org/abs/2608.08815v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_17-05-00Z_DistillingVision_LanguageModelsforRobustTrafficSig.md
generated_at: 2026-08-10 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LAMDA a framework for improving traffic sign recognition robustness against adversarial attacks such as shadow perturbations natural light interference and printed patches without adding inference overhead or using adversarial examples. It achieves consistent gains across multiple backbones datasets and attack types while maintaining clean accuracy. The method relies on language‑grounded structure via prototype banks from VLM descriptions.

## Key Takeaways
- LAMDA transfers language‑grounded structure into TSR models by creating fixed prototype banks using a frozen OpenCLIP text encoder which supervise visual features with two auxiliary losses during training.
- The adapter and prototype banks are discarded at inference leaving only the standard backbone and classifier so there is no runtime overhead.
- Evaluated on GTSRB LISA across four backbones and three attack types LAMDA is the only method that consistently improves robustness across all combinations delivering up to 12.5 pp gain under shadow attacks and 13.2 pp under natural‑light attacks while preserving or improving clean accuracy.

## Context
Traffic sign recognition remains a critical task for autonomous vehicles where perception must be reliable under real‑world lighting and occlusion conditions. Existing defenses often trade robustness for clean performance highlighting the need for methods that improve both without sacrificing safety. This work contributes to the broader effort of making deep models robust in deployment scenarios.

## Implications
For industry practitioners LAMDA offers a practical solution that can be integrated into existing VLM pipelines with minimal changes. The consistent boost across diverse conditions suggests that language‑anchored supervision could become a standard technique for enhancing perception robustness in safety‑critical applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08815v1)
