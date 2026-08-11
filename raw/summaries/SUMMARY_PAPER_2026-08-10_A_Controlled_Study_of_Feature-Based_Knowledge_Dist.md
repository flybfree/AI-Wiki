---
title: A Controlled Study of Feature-Based Knowledge Distillation Across Student Designs
url: http://arxiv.org/abs/2608.08294v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_19-10-17Z_AControlledStudyofFeature_BasedKnowledgeDistillati.md
generated_at: 2026-08-10 22:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how feature-based knowledge distillation interacts with student network architecture, using CIFAR-100 and a ResNet-50 teacher. It compares logit‑KD, attention transfer, FitNets across three student designs: CustomResNet width sweep, MobileNetV2, and a constant‑depth width sweep. Across 15 paired runs the results show that logit‑KD consistently outperforms scratch baselines while FitNets underperforms it.

## Key Takeaways
- Logit KD improves every tested student over its scratch baseline, indicating that aligning final logits remains beneficial regardless of architecture.
- Attention Transfer shows no clear size‑dependent effect inside the CustomResNet family but has a negative average impact there and a positive one for MobileNetV2, suggesting design‑specific interactions.
- FitNets is below logit KD in all runs; its gap widens when students are wider yet does not increase for the constant‑depth w=48 student.

## Context
Feature‑based distillation aims to preserve intermediate representations that may be more informative than final logits. Aligning these features across diverse architectures challenges standard distillators, which typically assume uniform training conditions. This study provides empirical evidence of how a single coefficient can produce heterogeneous gradient scales, highlighting the need for architecture‑aware methods.

## Implications
For practitioners, the findings suggest that one‑size‑fits‑all distillation may not be optimal; customizing the feature alignment strategy per student design could yield better performance. In industry, where model compression is critical, this research guides the development of more robust and scalable knowledge transfer techniques.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08294v1)
