---
title: LoOPSD: On-Policy Self-Distillation with Looped Teachers
published: 2026-10-13T11:07:04Z
authors: Wei Fan, Qingyue Yang, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Kejiang Chen, Weiming Zhang, Nenghai Yu
url: http://arxiv.org/abs/2610.18162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoOPSD: On-Policy Self-Distillation with Looped Teachers

## Abstract
On-policy self-distillation improves a model using guidance from the model itself, but it still requires a teacher that provides more useful predictions than the student. Existing approaches obtain such guidance by giving the teacher additional context or instructions. We ask whether it can instead come from changing how the same model uses its own layers. To address this, we introduce LoOPSD, which searches over a model's layer execution order to construct a stronger teacher and distills its advantage into the student. Specifically, we keep the model weights unchanged while searching for layers to repeat, and use the resulting teacher's predictions on student-generated prefixes to guide learning. We then alternate search and distillation, rebuilding the teacher from the updated student in each round so that the student progressively absorbs the gains from alternative layer execution. Experiments on mathematical and logical reasoning tasks show improvements across models. On GSM8K with a 400-token thinking budget, LoOPSD raises Qwen3-1.7B accuracy from 42.30% to 79.61%; subsequent distillation rounds yield further gains beyond the first round. Together, these findings show that by searching layer execution to construct teachers, we can turn a model's additional computation into improved student capabilities, opening a new avenue for self-distillation to derive supervision from the model's own computation.

## Metadata
- **Published**: 2026-10-13T11:07:04Z
- **Authors**: Wei Fan, Qingyue Yang, Chao-Hong Tan, Qian Chen, Wen Wang, Xiangang Li, Kejiang Chen, Weiming Zhang, Nenghai Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18162v1)