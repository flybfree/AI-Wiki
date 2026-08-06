---
title: Beyond Global Routing Aggregation: Phase-Aware Expert Merging for MoE Vision-Language Models
published: 2026-08-05T05:09:20Z
authors: Hongyu Zhang, Cheng Yan, Xiang Xia, Wuyang Zhang
url: http://arxiv.org/abs/2608.04454v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Global Routing Aggregation: Phase-Aware Expert Merging for MoE Vision-Language Models

## Abstract
Mixture-of-experts vision-language models (MoE-VLMs) increase model capacity with sparse expert activation, yet deployment requires storing the full expert pool. Training-free expert merging reduces this burden, and many routing-based methods aggregate routing statistics across all tokens to determine merge compatibility. However, MoE-VLM inference is phase-structured: image-context tokens carry visual content, question tokens specify the query, and answer tokens produce the output, with different counts and routing distributions. Because image-context tokens are far more numerous, global aggregation can overemphasize image-context processing and obscure phase-conditioned expert roles, making experts serving different phases appear interchangeable and degrading model performance. We therefore argue that MoE-VLM expert merging should preserve phase-conditioned expert roles, judging compatibility by how experts serve different phases rather than globally aggregated routing statistics. Based on this view, we propose RoleMerge, a training-free method that constructs each expert's Routing Role Profile (RRP) from phase-normalized routing statistics, capturing its relative phase preference. Guided by expert-phase information loss, RoleMerge merges experts with compatible profiles and their corresponding router entries while preserving answer-decoding expert distinctions. Experiments on three models and multiple benchmarks show that RoleMerge preserves more of the full model's performance than alternative expert-merging methods at matched expert-retention ratios, with relative improvements of up to 9.6 percent in six-task macro-average performance. These results validate phase-conditioned expert roles as a more effective basis than global routing aggregation for MoE-VLM expert merging.

## Metadata
- **Published**: 2026-08-05T05:09:20Z
- **Authors**: Hongyu Zhang, Cheng Yan, Xiang Xia, Wuyang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04454v1)