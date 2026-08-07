---
title: BioKD: Selective Physiology-to-Video Knowledge Distillation via Reliability Gate for Emotion Recognition
url: http://arxiv.org/abs/2608.06023v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_13-30-13Z_BioKD_SelectivePhysiology_to_VideoKnowledgeDistill.md
generated_at: 2026-08-06 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary  
BioKD is a reliability‑aware physiology‑to‑video knowledge distillation framework that uses physiological signals during training to guide a video‑based student model while relying solely on non‑intrusive video at inference time. Experiments on DEAP and AMIGOS show it consistently outperforms baselines, achieving 68.01 % trial‑wise arousal and 65.29 % subject‑wise valence recognition. The framework adapts knowledge transfer strength based on reliability, suppressing teacher errors and improving stability.

## Key Takeaways  
- BioKD employs a sample‑wise reliability gating mechanism that dynamically adjusts the influence of physiological teacher signals, thereby mitigating high noise and inter‑subject variability.  
- It achieves higher accuracy (e.g., 68.01 % trial‑wise arousal, 65.29 % subject‑wise valence) compared to baseline models.  
- The framework adds no inference‑time overhead and removes the need for physiological sensing and multimodal synchronization.

## Context  
In affective computing, integrating multimodal data is challenging because physiological signals suffer from high noise, inter‑subject variability, and temporal inconsistency. This work addresses those reliability issues by explicitly modeling supervision quality during distillation, offering a more robust alternative to single‑modal video models.

## Implications  
For industry practitioners, BioKD enables deployment with only video input, making emotion recognition scalable, privacy‑friendly, and cost‑effective while maintaining high performance across diverse subjects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06023v1)
