---
title: LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection
published: 2026-08-10T14:13:23Z
authors: Peter Lorenz, Anjith George, Marcel Sébastien
url: http://arxiv.org/abs/2608.09633v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoRA-based Adaptation Alone Is Not Enough: Understanding the Limits of Foundation Models for Face Presentation Attack Detection

## Abstract
Face presentation attack detection (PAD) aims to reliably detect a wide range of presentation attacks. While PAD methods achieve strong performance within individual datasets, their performance degrades under cross-dataset evaluation. Variations in sensors or lighting conditions can reduce the effectiveness of detectors from near-perfect to nearly random. Foundation models (FMs) have emerged as a promising alternative because typical PAD datasets, such as the MCIO benchmarks (MSU-MFSD, CASIA-FASD, Replay-Attack, and OULU-NPU), are small relative to the scale used for web-based pretraining. However, existing PAD systems primarily focus on CLIP-based foundation models, while overlooking other FMs with different architectures and training procedures. This study addresses this question by systematically evaluating 32 FMs. Zero-shot prompting achieves performance near chance across model families and scales. The vision encoders, when low-rankadapted (LoRA) with fewer than 1% trainable weights, achieve below 2% intra-dataset ACER in most cases, while cross-dataset ACER is substantially higher. LoRA primarily refines the decision boundary within a dataset, suggesting that pretrained representations and the adaptation dataset play a larger role in cross-dataset generalization than the evaluated lightweight adaptation strategy.

## Metadata
- **Published**: 2026-08-10T14:13:23Z
- **Authors**: Peter Lorenz, Anjith George, Marcel Sébastien
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09633v1)