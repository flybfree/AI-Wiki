---
title: Allocation Before Ranking: Decoupled Token Compression for OmniLLMs
published: 2026-08-03T03:56:33Z
authors: Zhenghui Guo, Yilin Yang, Yuanbin Man, Miao Yin, Weidong Shi, Rabimba Karanjai, Omprakash Gnawali, Chengming Zhang
url: http://arxiv.org/abs/2608.01665v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Allocation Before Ranking: Decoupled Token Compression for OmniLLMs

## Abstract
Token compression in OmniLLMs is typically posed as a single saliency-ranking problem: score each multimodal token, keep the top-K. We argue this abstraction is mis-specified. The same attention score simultaneously decides two things: how much retained capacity each modality receives, and which tokens within a modality are kept. A shared top-K rule therefore inherits this audio-favoring allocation prior, spending retained capacity on audio before video tokens have a chance to compete. We propose Macer, a training-free compressor that first assigns explicit audio and video budgets, then performs allocation-normalized ranking within each modality at modality-specific shallow layers. Macer significantly reduces token cost while preserving accuracy across audio-grounded, audio--video joint, visual-dominant, and video-centric benchmarks. At 25 % retention, Macer preserves 98.7 % of full-token performance on Qwen2.5-Omni-7B and 97.3 % on Qwen2.5-Omni-3B. On Qwen2.5-Omni-7B, this 25 % setting reaches OmniZip-level performance at 45 % retention while using lower FLOPs. On OmniVinci-9B, the same allocation-before-ranking principle improves over shared top-K ranking by up to 12.9 points.

## Metadata
- **Published**: 2026-08-03T03:56:33Z
- **Authors**: Zhenghui Guo, Yilin Yang, Yuanbin Man, Miao Yin, Weidong Shi, Rabimba Karanjai, Omprakash Gnawali, Chengming Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01665v1)