---
title: OpenStamp: A Watermark for Open-Source Language Models
published: 2026-08-28T04:08:01Z
authors: Miroojin Bakshi, Saksham Rastogi, Danish Pruthi
url: http://arxiv.org/abs/2608.27899v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OpenStamp: A Watermark for Open-Source Language Models

## Abstract
With the growing prevalence of large language model (LLM) generated content, watermarking is considered a promising approach for attributing text to LLMs and distinguishing it from human-written content. A prominent class of techniques embeds subtle but detectable signals in generated text by modifying token sampling probabilities. However, such methods are unsuitable for open-source models, where users have white-box access and can easily disable watermarking during inference. In this work, we introduce OpenStamp, a watermarking technique that encodes the watermarking logic directly into the model weights by modifying only the final projection, or unembedding, layer. Through experiments across two models, we show that OpenStamp achieves superior detection performance, with minimal degradation in model capabilities compared to prior methods. The implanted watermark is explicitly designed, and empirically confirmed, to be more robust to paraphrasing attacks and harder to scrub off through post-hoc fine-tuning than prior open-source watermarks. To enable developers to watermark their models, we release our code alongside watermarked versions of 4 popular open-source models.

## Metadata
- **Published**: 2026-08-28T04:08:01Z
- **Authors**: Miroojin Bakshi, Saksham Rastogi, Danish Pruthi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27899v1)