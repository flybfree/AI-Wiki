---
title: Steering Instruction Hierarchies at Inference Time
published: 2026-07-28T20:06:31Z
authors: Siqi Zeng, Sewoong Lee, Han Zhao, Julia Hockenmaier
url: http://arxiv.org/abs/2607.26228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Steering Instruction Hierarchies at Inference Time

## Abstract
Instruction hierarchies are a core safety assumption of language model deployment: higher priority inputs, such as system prompts, should override conflicting lower priority inputs from users or tools. Yet frontier LLMs often violate this hierarchy. We introduce V-Steer, a training-free inference time method that restores privileged influence by editing cached value vectors at prompt positions. Using direct logit attribution on the first next token prediction, V-Steer identifies heads where lower priority spans dominate privileged ones, then boosts privileged spans and suppresses conflicting lower priority spans through in-place multiplicative edits to cached V tensors. Since the method acts only on cached values, it remains compatible with fused attention backends and adds only a one time prefill overhead. Across models from 7B to 70B, this attribution guided intervention raises primary constraint accuracy from under 18% up to 92% on controlled role conflict benchmarks, and on broader instruction hierarchy evaluations substantially outperforms prompt only baselines while matching or exceeding SoTA training based methods on 3 of 4 scales of LLMs, with negligible decoding-speed overhead. The code is available at https://github.com/cindy2000sh/v-steer.

## Metadata
- **Published**: 2026-07-28T20:06:31Z
- **Authors**: Siqi Zeng, Sewoong Lee, Han Zhao, Julia Hockenmaier
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26228v1)