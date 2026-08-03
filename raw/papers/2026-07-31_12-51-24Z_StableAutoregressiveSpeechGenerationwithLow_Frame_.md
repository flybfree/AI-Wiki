---
title: Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens
published: 2026-07-31T12:51:24Z
authors: Yi Luo, Rongzhi Gu, Jixun Yao
url: http://arxiv.org/abs/2607.29363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens

## Abstract
Balancing sequence length, representational capacity, and long-horizon stability is a central problem in autoregressive (AR) speech and audio generation. Representations with higher frame rates or greater capacity can preserve more signal detail, but they also make streaming generation more vulnerable to distribution drift and AR error accumulation. Conversely, shorter and more compressed representations simplify AR modeling, but their limited bandwidth may discard important components and constrain the upper bound of reconstruction fidelity and generation quality. We ask whether a low-frame-rate, high-dimensional, high-bandwidth continuous representation can be co-designed with a streaming generation framework to support robust high-fidelity reconstruction, strong single-token predictability, and superior long-horizon stability. We decompose this goal into two coupled problems: what geometric and statistical properties a high-dimensional representation space should have, and how an AR continuous-token generator should be structured to resist error accumulation. Accordingly, we propose Locodec, a locally encoded codec that shapes its representation space to improve the interpolatability of a lower-dimensional core manifold and the identifiability of the native high-dimensional coordinates, thereby improving the predictability of high-dimensional high-bandwidth tokens. We also propose MP-ELD, a single-token AR flow-matching framework that uses multi-path information routing and residual classifier-free guidance to mitigate error accumulation. Experiments with 8-Hz, 768-dimensional tokens show that our design preserves reconstruction quality, improves single-token predictability, achieves competitive WER, and maintains stable long-form synthesis, without using external SSL/ASR models, pretrained text language models, or post-training stages.

## Metadata
- **Published**: 2026-07-31T12:51:24Z
- **Authors**: Yi Luo, Rongzhi Gu, Jixun Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29363v1)