---
title: CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model
published: 2026-08-13T11:25:23Z
authors: Nhan Phan, Ilona Lähteenmäki, Anna von Zansen, Olli-Pekka Pauna, Yaroslav Getman, Tamás Grósz, Mikko Kurimo
url: http://arxiv.org/abs/2608.13101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model

## Abstract
Research on automatic speaking assessment (ASA) has increasingly adopted multimodal speech large language models to assess learners' speaking performance. However, existing studies provide limited analysis of how acoustic and content information contribute to predictions and how stable the resulting performance is. We propose CASA, a simpler architecture combining Whisper-medium and Qwen3.5-2B that achieves state-of-the-art performance while providing a more interpretable separation between speech delivery and content.   On the Speak & Improve Corpus 2025, CASA achieves a root mean square error (RMSE) of 0.358, improving on the previous best RMSE while using approximately half the estimated inference parameters. The general-purpose architecture is designed for adaptation to other ASA corpora without structural changes and relies on three handcrafted fluency features. Through ablations and repeated runs, we analyze the individual and complementary contributions of acoustic and content information, examine performance variability, and demonstrate the potential of large language model reasoning for training-free content validation.

## Metadata
- **Published**: 2026-08-13T11:25:23Z
- **Authors**: Nhan Phan, Ilona Lähteenmäki, Anna von Zansen, Olli-Pekka Pauna, Yaroslav Getman, Tamás Grósz, Mikko Kurimo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13101v1)