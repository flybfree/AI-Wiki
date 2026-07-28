---
title: Omni-Prune: Query-Aware Unified Token Pruning for Efficient Omnimodal Large Language Models
published: 2026-07-26T03:51:39Z
authors: Yiming Zhong, Chang Nie, Caifeng Shan
url: http://arxiv.org/abs/2607.23445v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Omni-Prune: Query-Aware Unified Token Pruning for Efficient Omnimodal Large Language Models

## Abstract
Omnimodal large language models (OmniLLMs) are rapidly extending multimodal reasoning to cover synchronized audio and video. However, the resulting audio-video token sequences are long, leading to high prefill latency and GPU memory usage at inference time. Existing token pruning methods, designed mainly for vision-only inputs, miss both the cross-modal links between audio and video and the user query that decides which content matters. To bridge this gap, we present Omni-Prune, a training-free, query-aware audio-visual token pruning framework that jointly removes redundancy from both modalities while keeping task-relevant cross-modal evidence. Specifically, Omni-Prune first splits the token sequence into adaptive time windows placed at audio saliency peaks, then scores audio and video tokens on a single scale that combines encoder attention with text-query relevance, and pairs related audio-video tokens so that they are kept together. Within each window, a final K-medoids step then selects a few representative tokens, adding diverse cues that score-based selection alone would miss. Extensive experiments demonstrate that Omni-Prune outperforms established baseline methods, delivering up to 3.25x prefill speedup and 1.3x memory reduction while retaining over 99% of full-model performance.

## Metadata
- **Published**: 2026-07-26T03:51:39Z
- **Authors**: Yiming Zhong, Chang Nie, Caifeng Shan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23445v1)