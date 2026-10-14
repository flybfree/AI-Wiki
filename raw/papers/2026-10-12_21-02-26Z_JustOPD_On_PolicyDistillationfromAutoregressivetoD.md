---
title: JustOPD: On-Policy Distillation from Autoregressive to Diffusion Language Models
published: 2026-10-12T21:02:26Z
authors: Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang
url: http://arxiv.org/abs/2610.17397v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JustOPD: On-Policy Distillation from Autoregressive to Diffusion Language Models

## Abstract
On-policy distillation (OPD) is a post-training approach for large language models (LLMs) that enables a student model to learn a teacher model's distribution from sequences sampled from the student's own policy. Despite its promising capability, OPD for diffusion language models (DLMs) remains underexplored and existing studies primarily focuses on DLM-to-DLM distillation. The limited availability of strong teacher DLMs and the flexible generation order of DLMs impose additional technical challenges as well. However, it remains unclear how to effectively distill knowledge from a strong autoregressive language model (ARM) into a weaker DLM, given the mismatch between the left-to-right decoding of ARMs and the flexible decoding order of DLMs. Inspired by Ni et al. (2026), we propose JustOPD, an ARM-to-DLM on-policy distillation method that uses autoregressive rollouts during training to align the student's generation process with the ARM teacher's left-to-right decoding. This alignment enables effective distillation from ARM teachers while preserving the DLM's flexible generation-order capability at inference time. Experiments using Qwen3-14B as the teacher and Dream-7B as the student demonstrate that JustOPD consistently improves mathematical reasoning performance over the base DLM across multiple divergence choices.

## Metadata
- **Published**: 2026-10-12T21:02:26Z
- **Authors**: Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17397v1)