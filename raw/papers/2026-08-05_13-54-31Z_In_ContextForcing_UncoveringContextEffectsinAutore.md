---
title: In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion
published: 2026-08-05T13:54:31Z
authors: Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, Ye Shi
url: http://arxiv.org/abs/2608.05237v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion

## Abstract
Current few-step autoregressive video diffusion models depend on previous fully denoised clean frames as context for all denoising steps of the current frame. However, these clean frames leak excessive local details, which causes the model to take shortcuts, resulting in compromised temporal semantics and dynamics. Inspired by the perspective of diffusion as masking, we explore the impact of noisy contexts on few-step autoregressive generation. Yet, simply applying contexts with the same noise levels provides insufficient guidance, leading to poor temporal consistency. To resolve this dilemma, we introduce In-Context Forcing, a progressive autoregressive paradigm that utilizes contexts with decreasing noise levels. By applying less masking to distant frames and more masking to adjacent ones, this approach provides adaptive guidance, effectively ensuring both robust temporal consistency and high inter-frame dynamics. Furthermore, by decoupling the strict dependence on previous clean frames, our paradigm enables cross-frame parallel denoising, achieving substantial inference acceleration without sacrificing performance. Extensive experiments on VBench demonstrate that our method significantly outperforms state-of-the-art approaches in both visual fidelity and inference speed.

## Metadata
- **Published**: 2026-08-05T13:54:31Z
- **Authors**: Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, Ye Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05237v1)