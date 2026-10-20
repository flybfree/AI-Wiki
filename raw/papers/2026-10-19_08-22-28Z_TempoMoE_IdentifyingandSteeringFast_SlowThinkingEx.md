---
title: TempoMoE: Identifying and Steering Fast-Slow Thinking Experts for Efficient Multimodal Reasoning
published: 2026-10-19T08:22:28Z
authors: Xiyue Zhang, Keru Zhou, Ziyi Wang, Bing Hu, Li Wang
url: http://arxiv.org/abs/2610.25999v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TempoMoE: Identifying and Steering Fast-Slow Thinking Experts for Efficient Multimodal Reasoning

## Abstract
Multimodal Mixture-of-Experts (MoE) reasoning models rely on long chain-of-thought (CoT) for complex tasks, yet often overthink easy inputs, increasing token cost and latency, and sometimes degrading accuracy. Existing methods optimize reasoning length during training or impose external control at inference, but leave the underlying reasoning mechanism a black box. We find that fast and slow thinking exhibit distinct expert-routing patterns: holding the input fixed and varying only the prompted reasoning tempo produces stable routing shifts. Suppressing slow-thinking experts shortens the reasoning chain, whereas suppressing fast-thinking experts lengthens it, providing causal evidence that these experts influence reasoning depth. Based on this finding, we propose TempoMoE, a training-free, two-stage framework. It identifies fast- and slow-thinking experts via tempo-contrastive routing analysis and redistributes routing weights within the original top-k set according to sample difficulty. It amplifies fast-thinking experts and suppresses slow-thinking experts on easy inputs and reverses this adjustment on hard ones, enabling difficulty-adaptive control over reasoning depth. We evaluate TempoMoE on Kimi-VL, Qwen3-VL, and ERNIE-4.5-VL across six benchmarks. Compared with Vanilla, TempoMoE consistently improves accuracy while reducing output tokens, with accuracy gains of up to 2.6 points and token reductions of up to 35.4%.

## Metadata
- **Published**: 2026-10-19T08:22:28Z
- **Authors**: Xiyue Zhang, Keru Zhou, Ziyi Wang, Bing Hu, Li Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25999v1)