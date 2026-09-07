---
title: Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference
published: 2026-09-04T08:52:36Z
authors: Zhenhe Wu, Yaping Jin, Qinghua Xing, Hang Zhou, Wei He, Xianjie Wu, Xianfu Cheng, Jian Yang, Hanting Chen
url: http://arxiv.org/abs/2609.04895v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference

## Abstract
Mixture-of-Experts (MoE) models activate only a small subset of experts per token, but the full expert set often exceeds GPU memory, causing repeated weight transfers during decoding. We formulate expert-cache management as a model-side algorithmic problem and propose a cache-aware post-training framework that jointly adapts the MoE backbone and lightweight auxiliary cache routers while preserving the native Top-K expert-selection rule at inference. Its update-only mode, Temporal Router, predicts same-layer reuse and retains experts for future tokens without proactive loading. The full Spatio-Temporal Router adds a Spatio Router that uses the causal predecessor's hidden state to refine the temporal cache before target-layer access. We evaluate both modes on Qwen3 and GPT-OSS across GSM8K, MATH, and CommonsenseQA. Temporal Router consistently improves cache hit rate and reduces expert-weight traffic over matched LM-only baselines. On Qwen3, Spatio-Temporal Router achieves the best load-adjusted efficiency across three tasks, improving adjusted hit rate by 1.15--18.03 points and reducing traffic by 4.6--53.3% relative to the strongest evaluated prefetching baseline; results on GPT-OSS are competitive but task-dependent. An auxiliary-only ablation preserves baseline accuracy but yields modest cache gains, whereas joint post-training produces larger improvements. Sensitivity analyses show that cache capacity controls transfer demand, while the refinement budget governs the trade-off between pre-access coverage and proactive traffic.

## Metadata
- **Published**: 2026-09-04T08:52:36Z
- **Authors**: Zhenhe Wu, Yaping Jin, Qinghua Xing, Hang Zhou, Wei He, Xianjie Wu, Xianfu Cheng, Jian Yang, Hanting Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04895v1)