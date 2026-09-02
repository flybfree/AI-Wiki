---
title: SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models
published: 2026-09-01T09:52:10Z
authors: Shiyu Li, Zi-Yuan Hu, Shijia Huang, Yanyang Li, Yiwu Zhong, Liwei Wang
url: http://arxiv.org/abs/2609.01004v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models

## Abstract
Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences. To reduce inference costs, recent studies have explored visual token pruning through vision-centric or text-guided strategies. However, these methods often overlook high-norm outlier tokens, i.e., tokens with abnormally large feature norms, leading to suboptimal pruning decisions. In this work, we show that such high-norm outlier tokens are highly redundant in both feature and spatial dimensions, yet are often mistakenly preserved as informative cues by existing methods.   Motivated by this observation, we propose SinkPruner, a training-free visual token pruning framework for efficient MLLM inference. SinkPruner follows a coarse-to-fine design with two key modules: a visual sanitizer that filters high-norm redundancies and alleviates attention sink and attention dispersion, and a text-guided pruner that further retains tokens semantically aligned with the text query.   Extensive experiments on twelve image-language and four video-language benchmarks demonstrate the effectiveness, efficiency, and generalizability of our framework. Notably, SinkPruner preserves 96.5% (91.8%) of the original performance of LLaVA-1.5 (Qwen2.5-VL) under an 89% token reduction. Experiments further indicate that our visual sanitizer exhibits promising transferability in enhancing the performance of existing pruning methods. Our code is available at https://github.com/LaVi-Lab/SinkPruner.

## Metadata
- **Published**: 2026-09-01T09:52:10Z
- **Authors**: Shiyu Li, Zi-Yuan Hu, Shijia Huang, Yanyang Li, Yiwu Zhong, Liwei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01004v1)