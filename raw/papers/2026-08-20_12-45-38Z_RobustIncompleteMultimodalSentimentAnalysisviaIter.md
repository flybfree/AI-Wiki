---
title: Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction
published: 2026-08-20T12:45:38Z
authors: Zhifa Geng, Subin Huang, Hao Guo, Junjie Chen, Sanmin Liu, Chao Kong
url: http://arxiv.org/abs/2608.19971v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robust Incomplete Multimodal Sentiment Analysis via Iterative Proxy Correction

## Abstract
Multimodal sentiment analysis aims to infer affective states by integrating language, visual, and acoustic cues. However, real-world multimodal inputs are often incomplete or corrupted, which can weaken cross-modal complementarity and introduce misleading information into downstream fusion. Existing proxy-based methods for incomplete MSA commonly rely on one-shot proxy construction to compensate for degraded language information, but the generated proxy may be coarse or unreliable at initialization. Prematurely injecting such a proxy into multimodal reasoning can propagate initial errors and compromise sentiment prediction. To address this limitation, we propose an iterative proxy correction framework for robust incomplete MSA. Our method constructs a language-oriented proxy from non-language modalities and progressively refines it under multimodal context through gated residual correction. The corrected proxy is then adaptively fused with the observed language representation according to an estimated language reliability score, allowing the model to balance proxy-based compensation and trustworthy linguistic evidence. In addition, we introduce a stage-wise latent correction objective that uses the complete language representation as a training-time semantic anchor to stabilize the proxy refinement trajectory. Extensive experiments on MOSI, MOSEI, and SIMS under diverse missing-modality settings demonstrate that the proposed framework consistently outperforms competitive baselines and achieves robust sentiment prediction under incomplete inputs.

## Metadata
- **Published**: 2026-08-20T12:45:38Z
- **Authors**: Zhifa Geng, Subin Huang, Hao Guo, Junjie Chen, Sanmin Liu, Chao Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19971v1)