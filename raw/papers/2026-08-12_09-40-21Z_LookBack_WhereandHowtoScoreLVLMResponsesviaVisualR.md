---
title: LookBack: Where and How to Score LVLM Responses via Visual Reference Usage
published: 2026-08-12T09:40:21Z
authors: Beomsik Cho, Jinhyeong Kim, Dongseok Lee, Jaehyung Kim
url: http://arxiv.org/abs/2608.11847v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LookBack: Where and How to Score LVLM Responses via Visual Reference Usage

## Abstract
Large Vision-Language Models (LVLMs) integrate visual perception with language generation, enabling responses that span image understanding and complex reasoning. However, LVLMs do not just inherit the text-level hallucinations; they also hallucinate against the image, producing fluent responses ungrounded in what they see. This makes LVLM response scoring inherently harder, and our diagnostics show that existing confidence-based metrics adopted from LLMs are insufficient for LVLMs. Specifically, removing the input image barely changes confidence-based selection, suggesting that output-space confidence primarily captures textual plausibility rather than agreement with the image. To address this gap, we propose LookBack, a training-free LVLM response scoring method that augments token likelihood with visual lookback score, a lightweight measure of how strongly each response token refers to image tokens. Across four benchmarks and three models, LookBack consistently improves Best-of-$N$ selection over existing baselines with negligible additional overhead.

## Metadata
- **Published**: 2026-08-12T09:40:21Z
- **Authors**: Beomsik Cho, Jinhyeong Kim, Dongseok Lee, Jaehyung Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11847v1)