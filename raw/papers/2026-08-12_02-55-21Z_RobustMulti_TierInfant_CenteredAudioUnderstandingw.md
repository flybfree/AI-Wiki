---
title: Robust Multi-Tier Infant-Centered Audio Understanding with Whisper via Structured Speaker Conditioning
published: 2026-08-12T02:55:21Z
authors: Xulin Fan, Jialu Li, Mohammad Nur Hossain Khan, Kexin Hu, Bashima Islam, Mark Hasegawa-Johnson, Nancy L. McElwain
url: http://arxiv.org/abs/2608.11587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Multi-Tier Infant-Centered Audio Understanding with Whisper via Structured Speaker Conditioning

## Abstract
Recent advances in model design and self-supervised audio representations have improved speech and audio understanding, yet infant-centered naturalistic recordings remain challenging due to limited labeled data, low signal-to-noise ratio, and cross-family domain shifts. We present a family-conditioned, multi-tier audio tagger that combines a LoRA-finetuned Whisper encoder with a lightweight, target-speaker-aware Transformer for long-context inference and framewise prediction across tiers. To improve temporal coherence, we incorporate a simple sequence-level smoothing loss, and to enhance robustness across households, we introduce a factorized speaker-token design with a shared tier token and a learned family-specific offset, reducing family bias and promoting generalizable representations. Together, these choices enable efficient and effective infant-centered audio tagging of daylong audio recordings in home environments.

## Metadata
- **Published**: 2026-08-12T02:55:21Z
- **Authors**: Xulin Fan, Jialu Li, Mohammad Nur Hossain Khan, Kexin Hu, Bashima Islam, Mark Hasegawa-Johnson, Nancy L. McElwain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11587v1)