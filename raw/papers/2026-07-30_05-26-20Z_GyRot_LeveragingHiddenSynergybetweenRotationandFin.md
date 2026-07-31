---
title: GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference
published: 2026-07-30T05:26:20Z
authors: Sangjin Kim, Yuseon Choi, Byeongcheol Kim, Jungjun Oh, Hoi-jun Yoo
url: http://arxiv.org/abs/2607.27694v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference

## Abstract
Low-bit quantization is essential for efficient LLM inference, and both rotation and fine-grained group quantization have shown individual promise. However, their combination often leads to accuracy degradation or hardware overhead due to a mismatch between the global nature of rotation and the localized behavior of group scaling. We propose GyRot, a quantization framework and hardware accelerator that bridges this gap through algorithm-hardware co-design. GyRot introduces Coarse Rotation, Fine Grouping (CoRFiG) and Harmonic-Aligned Permutation (HAP) to enable cooperative integration of rotation and group quantization, enhancing quantizability while relaxing scaling factor precision. To further reduce hardware cost, we reformulate asymmetric quantization and introduce a zero-point rounding strategy that enables fully integer dequantization. Implemented on an INT4-based tensor PE architecture, GyRot achieves state-of-the-art 4-bit accuracy across LLaMA-family models, while delivering up to 3.4x speedup and 3.6x energy efficiency over baseline LLM accelerators. These results validate GyRot's practical effectiveness for scalable and energy-efficient LLM deployment.

## Metadata
- **Published**: 2026-07-30T05:26:20Z
- **Authors**: Sangjin Kim, Yuseon Choi, Byeongcheol Kim, Jungjun Oh, Hoi-jun Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27694v1)