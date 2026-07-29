---
title: AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight Speech Emotion Recognition
url: http://arxiv.org/abs/2607.25289v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_04-53-27Z_AMRD_AdaptiveMulti_TeacherRelationalDistillationfo.md
generated_at: 2026-07-28 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Adaptive Multi-Teacher Relational Distillation (AMRD), a method that improves on traditional multi-teacher knowledge distillation for speech emotion recognition by addressing batch‑wise teacher reliability and the relational structure of logits. The authors show that AMRD yields higher accuracy than single‑teacher baselines across IEMOCAP and CREMA‑D datasets with four student architectures, confirming that both the adaptive weighting and relational loss contribute to performance gains.

## Key Takeaways
- Teacher reliability varies per batch; AMRD uses a one‑class SVM on each teacher’s logit similarity matrix to assign per‑batch weights that favor more coherent teachers.  
- The method employs a relational distillation loss that aligns teacher and student similarity matrices, capturing the structural information lost by simple logit matching.  
- Ablations demonstrate complementary gains from both components, with neither alone achieving the full performance improvement observed in AMRD.

## Context
Speech emotion recognition on edge devices demands lightweight models that retain high accuracy while minimizing computational cost. Multi‑teacher distillation is a common technique to compress large self‑supervised models, yet existing approaches often ignore batch‑specific reliability and relational logits, limiting their effectiveness for real‑time applications.

## Implications
AMRD provides a practical framework for deploying accurate emotion classifiers on resource‑constrained hardware without sacrificing performance. Practitioners can adopt the adaptive weighting strategy to handle noisy or inconsistent teacher outputs, while the relational loss offers a principled way to preserve inter‑sample structure in distilled models. This approach supports scalable deployment of AI services that require continuous, low‑latency emotion analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25289v1)
