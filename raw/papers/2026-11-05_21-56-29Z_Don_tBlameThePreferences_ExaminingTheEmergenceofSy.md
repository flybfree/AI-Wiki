---
title: Don't Blame The Preferences: Examining The Emergence of Sycophancy in LLM Training
published: 2026-11-05T21:56:29Z
authors: Chao Peter Yang, Catherine Zehr, Pranav Bijith, Brandon Fain
url: http://arxiv.org/abs/2611.10045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Don't Blame The Preferences: Examining The Emergence of Sycophancy in LLM Training

## Abstract
AI sycophancy, the tendency of large language models (LLMs) to flatter users and affirm their beliefs, can undermine accuracy and contribute to misinformation, dependence, and overconfidence. Although prior work has benchmarked sycophancy in released models and proposed mitigations, its origins during training remain poorly understood. Preference alignment methods such as RLHF and DPO are often blamed, but their effects are rarely compared with earlier training stages. We investigate sycophancy across the training pipelines of three model families and three benchmarks. We find that sycophancy is largely established by the end of supervised fine-tuning (SFT), rather than introduced by preference alignment. Across all nine model benchmark combinations, SFT checkpoints attain at least 92% of preference aligned models' sycophancy scores and at least 85% of final models' scores; on average, they are about as sycophantic as final models. Preference alignment increases sycophancy in only four of nine cases, by an average of 4.2 percentage points when it does. To probe the underlying causes, we isolate model representations associated with sycophancy using mechanistic interpretability and measure their activation on training datasets from each stage. SFT datasets show roughly the same average activation as other training data but contribute substantially more examples, and the highest-scoring individual datasets all come from SFT. Our findings suggest that addressing sycophancy requires interventions throughout the training pipeline, particularly in data selection and augmentation for pre-training and SFT.

## Metadata
- **Published**: 2026-11-05T21:56:29Z
- **Authors**: Chao Peter Yang, Catherine Zehr, Pranav Bijith, Brandon Fain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.10045v1)