---
title: SelFusion: Self-distillation for Diffusion Language Models
published: 2026-08-24T07:26:35Z
authors: Hyeongsoo Lim, Jinyoung Kim, Eunseo Seo, Minho Jang, Jiwon Yoon
url: http://arxiv.org/abs/2608.22898v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SelFusion: Self-distillation for Diffusion Language Models

## Abstract
Diffusion language models (DLMs) alleviate the inherent latency bottleneck of autoregressive (AR) large language models (LLMs), but their degraded generation quality limits practical applicability. Although knowledge distillation (KD) can be a promising direction for improving performance, we empirically find that naively applying conventional KD yields only marginal gains, or even degrades generation quality. Based on these observations, we propose a novel self-distillation framework for DLMs, namely SelFusion. To enable effective KD without an external teacher model, SelFusion performs two forward passes with different masking levels, defining the hard mode with a larger masking probability and the easy mode with a smaller masking probability. However, the easy mode is not always more accurate than the hard mode and can be overconfident on incorrect tokens. Thus, we introduce bidirectional KD between the two modes, which can dynamically determine the distillation direction based on token-level correctness. Experimental results on instruction-following tasks show that the proposed self-distillation substantially outperforms other KD methods with external LLM and DLM teachers. In many configurations, the student trained with SelFusion even surpasses the performance of the LLM teacher, providing a practical path toward improving DLM generation quality. Source code can be found at https://github.com/scai-research/SelFusion_official

## Metadata
- **Published**: 2026-08-24T07:26:35Z
- **Authors**: Hyeongsoo Lim, Jinyoung Kim, Eunseo Seo, Minho Jang, Jiwon Yoon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22898v1)