---
title: Rethinking Privileged Information in On-Policy Self-Distillation
published: 2026-08-18T19:42:16Z
authors: Samyak Shrestha, Alexander Tessier
url: http://arxiv.org/abs/2608.18271v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Privileged Information in On-Policy Self-Distillation

## Abstract
On-policy self-distillation (OPSD) trains a student on its own responses using token-level supervision from the same model conditioned on privileged reference information. We investigate whether performance gains from OPSD show that the student learned the information in the reference or instead reflect recovery of reasoning behavior already present in the base model. We perform OPSD experiments on science and mathematics datasets using Qwen3 models ranging from 1.7B to 8B. Our analysis framework separates the supervision induced by the reference from the supervision provided by the teacher without the reference and measures how each aligns with changes in the student's predictions. The correct reference does not provide a consistent performance benefit across teacher generation modes, model sizes, and training datasets. Students can improve without the correct reference, and a solution from another problem can outperform the correct solution on several mathematical reasoning benchmarks. The student's predictions align more strongly with the base model's thinking behavior than with the supervision induced by the reference, but controls constructed from other problems reproduce much of both alignments. Moreover, stronger alignment attributable to the correct reference does not reliably coincide with a greater performance benefit from the reference. Performance gains and distributional alignment alone therefore cannot determine how privileged reference information contributes to student learning in OPSD.

## Metadata
- **Published**: 2026-08-18T19:42:16Z
- **Authors**: Samyak Shrestha, Alexander Tessier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18271v1)