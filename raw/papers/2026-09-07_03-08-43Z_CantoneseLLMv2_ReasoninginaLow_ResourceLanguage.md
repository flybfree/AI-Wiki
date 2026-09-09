---
title: CantoneseLLM v2: Reasoning in a Low-Resource Language
published: 2026-09-07T03:08:43Z
authors: Tsz Chung Cheng, Chung Shing Cheng, Chaak Ming Lau, Cheuk Hei Chong
url: http://arxiv.org/abs/2609.06970v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CantoneseLLM v2: Reasoning in a Low-Resource Language

## Abstract
Cantonese is widely spoken but remains low-resource in written data, with no large corpus of native Cantonese reasoning traces available for model training. We develop and release CantoneseLLM v2, comprising models based on Qwen3 8B and 30B-A3B. The models are trained through CPT on 784 million Cantonese and Hong Kong-related tokens, chat-vector merging, SFT, DPO, and RLVR. Evaluation across the training stages shows that chat-vector merging transfers instruction following but preserves the donor model's reasoning language, while SFT with limited Cantonese reasoning data substantially shortens or removes reasoning traces and reduces benchmark performance. DPO restores the reasoning-block format, particularly for the 8B model, but recovers only part of the lost performance. The RLVR training with Cantonese language and Traditional Chinese scripts as multiplicative constraints introduced Cantonese language alignment and restored the lost performance. The 30B-A3B model reaches 73.16 on HKCanto-Eval, within 1.20 points of its merged checkpoint, while retaining the Cantonese reasoning behaviour absent from that checkpoint. We release the model checkpoints, the training environments, and a thirteen-year Traditional Chinese Common Crawl dataset. The models can be accessed at https://huggingface.co/collections/hon9kon9ize/cantonesellm-v20

## Metadata
- **Published**: 2026-09-07T03:08:43Z
- **Authors**: Tsz Chung Cheng, Chung Shing Cheng, Chaak Ming Lau, Cheuk Hei Chong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06970v1)