---
title: Reliability Challenges in Diffusion Vision-Language Models
published: 2026-09-01T14:38:50Z
authors: Md. Atabuzzaman, Chris Thomas
url: http://arxiv.org/abs/2609.01318v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reliability Challenges in Diffusion Vision-Language Models

## Abstract
Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our key findings are: (1) dLVLMs reverse the yes-bias of AR models in binary visual queries; (2) they achieve competitive hallucination rates yet exhibit degraded linguistic quality; (3) they collapse to near-zero accuracy on underrepresented racial groups with opposite-polarity gender bias; and (4) they exhibit accuracy collapse in multiple-choice settings when the correct option is shorter than its distractors, associated with a length prior that emerges at the first denoising step. Tokens committed at late denoising steps with low confidence further correlate with hallucinated content, pointing to a mechanistic signal unique to diffusion generation. These patterns vary across model families, suggesting reliability is shaped by the generative paradigm together with training data.

## Metadata
- **Published**: 2026-09-01T14:38:50Z
- **Authors**: Md. Atabuzzaman, Chris Thomas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01318v1)