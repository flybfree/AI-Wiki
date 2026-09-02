---
title: TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models
published: 2026-09-01T14:12:57Z
authors: Chao Zhou, Yiling Chen, Qi Chu, Tao Gong, Nenghai Yu, Tianyi We
url: http://arxiv.org/abs/2609.01277v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models

## Abstract
Although pretrained joint audio-visual diffusion models offer rich control over \emph{what} to generate, they provide no explicit control over \emph{when} an utterance should occur. To address this, we study \emph{inference-time speech scheduling}, a novel task that places coupled speech and visual articulation within user-specified begin--end intervals without finetuning the backbone model. We uncover two intrinsic properties of the denoising process that enable this task. First, a timing-sensitive text-to-audio cross-attention head exposes each utterance's model-implied source span along the latent timeline. Second, the predicted clean latent already organizes coupled speech and visual articulation, allowing their temporal placement to be edited without regenerating the content. Building on these discoveries, we propose \textbf{TimeSteer}, a training-free framework that localizes each utterance's source span through \textbf{Source Span Localization} and transfers the associated audio-visual latent content from the source interval to the specified target interval through \textbf{Region-Aware Latent Remapping}. We further introduce \textbf{SpeechShift}, the first benchmark for interval-level speech scheduling in joint audio-visual generation. Experiments across two representative backbones show that TimeSteer substantially improves interval controllability over training-free baselines while maintaining competitive overall generation quality.

## Metadata
- **Published**: 2026-09-01T14:12:57Z
- **Authors**: Chao Zhou, Yiling Chen, Qi Chu, Tao Gong, Nenghai Yu, Tianyi We
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01277v1)