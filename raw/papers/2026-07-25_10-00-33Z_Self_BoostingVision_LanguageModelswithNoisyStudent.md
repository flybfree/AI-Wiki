---
title: Self-Boosting Vision-Language Models with Noisy Student On-Policy Self-Distillation
published: 2026-07-25T10:00:33Z
authors: Shuai Wang, Daoan Zhang, Zhe Tang, Hao Cheng, Jiaheng Wei
url: http://arxiv.org/abs/2607.23125v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Boosting Vision-Language Models with Noisy Student On-Policy Self-Distillation

## Abstract
Post-training enables vision-language models (VLMs) to understand human instructions and perform various downstream tasks. Current post-training methods usually rely on human-annotated data, distillation from external models, reinforcement learning with human feedback, or verifiable answers. This limits their ability to improve without external supervision. To tackle this, we propose NOPD (Noisy Student On-Policy Self-Distillation), a simple yet effective self-distillation approach that improves VLMs without any external models or ground-truth answers. Our key insight is that prediction discrepancies between clean and corrupted inputs naturally induce a self-supervision signal. In NOPD, the model learns from corrupted inputs while using its own predictions under clean inputs as token-level supervision. We show the effectiveness of NOPD on five visual reasoning tasks; it can match and even outperform reinforcement learning approaches or distillation from external models. Notably, when trained with 2.1K samples from Geometry3K, NOPD improves Qwen2.5-VL-7B by 20 points on its validation set. It also shows generalization on out-of-distribution test sets and achieves 7.4 point gains on MathVista. Furthermore, we demonstrate that NOPD is a general approach to enhance VLMs, achieving improvements across three models on 12 benchmarks.

## Metadata
- **Published**: 2026-07-25T10:00:33Z
- **Authors**: Shuai Wang, Daoan Zhang, Zhe Tang, Hao Cheng, Jiaheng Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23125v1)