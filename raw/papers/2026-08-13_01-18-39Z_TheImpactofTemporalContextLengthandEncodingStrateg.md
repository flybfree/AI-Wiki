---
title: The Impact of Temporal Context Length and Encoding Strategies on Self-Supervised ECG Representation Learning
published: 2026-08-13T01:18:39Z
authors: Ahmed Sameh, Ramzi Al-Sharawi, Yogatheesan Varatharajah
url: http://arxiv.org/abs/2608.12695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Impact of Temporal Context Length and Encoding Strategies on Self-Supervised ECG Representation Learning

## Abstract
Self-supervised electrocardiogram (ECG) models are often trained on a few seconds of ECG signal and, increasingly, on discretized token sequences. It remains unclear whether these choices sacrifice information needed for rhythm inference and longitudinal consistency in real-world ambulatory recordings. We present a controlled study on the Icentia11k single-lead dataset that varies (i) the input horizon (16 seconds, 1 minute, 5 minutes, and 10 minutes) and (ii) the front-end representation (continuous convolutional patch embeddings vs. fixed vector-quantized tokens), while holding the Transformer backbone and training protocol constant. Representations are assessed by downstream abnormal rhythm detection and by patient-level retrieval that probes cross-session stability. Our results show that increasing temporal context beyond 16-second snapshots yields stronger transfer and higher retrieval accuracy, with the strongest performance achieved by the 5- and 10-minute models, indicating improved capture of slow-varying rhythm dynamics and individual-specific structure. Across all evaluated horizons, continuous patch embeddings outperform discretized tokens, suggesting that quantization can discard clinically relevant waveform detail. These findings motivate ECG foundation models that emphasize extended context and continuous encoders for clinical prediction and similarity-based applications. Our code and pretrained models are publicly available at https://github.com/muha-0/ecg-ssl-representation-learning.

## Metadata
- **Published**: 2026-08-13T01:18:39Z
- **Authors**: Ahmed Sameh, Ramzi Al-Sharawi, Yogatheesan Varatharajah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12695v1)