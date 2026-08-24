---
title: MentorPulse: Refreshing Cross-Model Latent Guidance for Long-Form Generation
published: 2026-08-21T09:49:09Z
authors: Ziwu Liu, Guozhong Li, Chen Qiu, Weiyang Kong, Panos Kalnis
url: http://arxiv.org/abs/2608.20927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MentorPulse: Refreshing Cross-Model Latent Guidance for Long-Form Generation

## Abstract
Cross-model latent guidance lets a frozen large mentor encode an input once and a frozen small student generate from the resulting signal. Existing methods keep this signal fixed, assuming it stays useful as the output grows; we show this fails in long-form generation. On multi-turn instruction following, static guidance pushes a 4B student's constraint satisfaction 2.5 points below its no-guidance baseline; a training-free refresh every 16 tokens changes only the memory content and restores a 2.0-point gain over that baseline. We propose MentorPulse to keep guidance fresh at practical cost: it compresses mentor states into a capped slot memory, incrementally processes newly generated tokens, and updates the memory that the student reads through gated cross-attention without resetting the student's KV cache. Windowed Refresh Training exposes the bridge to prefix-conditioned memory. Across thirteen datasets, MentorPulse closes 52.2% of the mentor-student gap on macro average, outperforming C2C, T2T, and equal-budget LoRA, with the largest gains on long outputs. It performs best on all eleven mentor-student pairs from three model families, with margins that narrow as the capability gap grows, and a lightweight read-pattern check predicts the gain before deployment. Measured costs identify refresh intervals that dominate text guidance on long outputs.

## Metadata
- **Published**: 2026-08-21T09:49:09Z
- **Authors**: Ziwu Liu, Guozhong Li, Chen Qiu, Weiyang Kong, Panos Kalnis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20927v1)