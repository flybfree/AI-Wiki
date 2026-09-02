---
title: Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
url: http://arxiv.org/abs/2609.01532v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_17-00-30Z_KnowledgeDistillationDuringMid_TrainingFavorsReaso.md
generated_at: 2026-09-01 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how knowledge distillation (KD) behaves during the mid‑training phase of self‑supervised language model development. It shows that while forward KL distillation improves reasoning early on, it hinders factual recall acquisition at this stage, leading to a divergence between performance dimensions.

## Key Takeaways
- Forward KL distillation yields superior reasoning gains but slows factual recall during mid‑training because teachers are more confident on procedural tasks than knowledge‑intensive ones.  
- The student’s early accumulation of low‑entropy factual knowledge creates an asymmetry that the standard KD objective cannot resolve.  
- Switch Distillation, which routes distillation to high‑confidence teacher predictions and falls back to cross‑entropy otherwise, restores both reasoning and factual recall while preserving most of the original gains.

## Context
Mid‑training is a critical yet understudied phase where model behavior can shift dramatically, affecting downstream task performance. Understanding how training objectives impact different skill domains helps design more robust pre‑training pipelines for large language models.

## Implications
Practitioners can adopt Switch Distillation to mitigate stage‑dependent weaknesses without sacrificing efficiency, leading to more balanced and reliable model capabilities across reasoning and factual knowledge. This approach offers a practical remedy for the current gap between high‑level performance and accurate recall in deployed systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01532v1)
