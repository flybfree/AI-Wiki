---
title: One Model, Two Paths: Balancing Single-Pass and Looped Performance in Language Models
published: 2026-10-24T07:50:29Z
authors: Jiarun Shen, Lei Zhao, Xiao Li
url: http://arxiv.org/abs/2610.33517v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Model, Two Paths: Balancing Single-Pass and Looped Performance in Language Models

## Abstract
Repeating Transformer layers can improve language-model performance without adding parameters. A pretrained model can be adapted to support both single-pass and looped inference by reusing middle-layer weights for additional computation. Because both paths share weights, training to improve looped predictions can degrade single-pass quality. We study joint training strategies using weighted losses on both outputs, with guidance from the frozen original model. Joint supervision substantially reduces single-pass degradation compared to looped-only training, while preserving looped gains over ordinary continued training. Most of this benefit comes from adjusting the single-pass loss weight, with guidance from the frozen original model further improving the looped output. With validation-selected weights, our method preserves single-pass quality within a predefined tolerance of ordinary continued training while improving looped predictions.

## Metadata
- **Published**: 2026-10-24T07:50:29Z
- **Authors**: Jiarun Shen, Lei Zhao, Xiao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33517v1)