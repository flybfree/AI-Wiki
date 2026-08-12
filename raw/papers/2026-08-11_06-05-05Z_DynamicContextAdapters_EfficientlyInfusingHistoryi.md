---
title: Dynamic Context Adapters: Efficiently Infusing History into Vision-and-Language Models
published: 2026-08-11T06:05:05Z
authors: Yuhang Song, Bor-Jiun Lin, Jiaxu Liu, Te-Chuan Chiu, Anh Nguyen, Chun-Yi Lee
url: http://arxiv.org/abs/2608.10525v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Context Adapters: Efficiently Infusing History into Vision-and-Language Models

## Abstract
Historical context integration presents a fundamental challenge for Vision-Language Models (VLMs) in sequential decision-making tasks. Current VLMs process visual inputs independently, which creates critical limitations for downstream applications that require temporal understanding. Direct incorporation of historical frames into Transformer inputs produces quadratic attention complexity and excessive memory consumption. Existing approaches suffer from significant drawbacks: computational inflation or substantial information loss through temporal compression. To address these challenges, we introduce Dynamic Context Adapter (DCA), a novel context injection approach for pretrained VLMs. Our method employs fixed-size, dynamically compressed memory to preserve historical semantics without frame concatenation. DCA bridges static VLMs and recurrent policies and enables memory capabilities in pretrained models while maintaining computational efficiency. DCA achieves over $25\%$ reduction in attention FLOPs and $13\%$ memory savings while improving performance on long-horizon tasks.

## Metadata
- **Published**: 2026-08-11T06:05:05Z
- **Authors**: Yuhang Song, Bor-Jiun Lin, Jiaxu Liu, Te-Chuan Chiu, Anh Nguyen, Chun-Yi Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10525v1)