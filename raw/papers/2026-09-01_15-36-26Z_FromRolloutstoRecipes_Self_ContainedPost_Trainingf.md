---
title: From Rollouts to Recipes: Self-Contained Post-Training for LLMs
published: 2026-09-01T15:36:26Z
authors: Yifei Li, Lingling Zhang, Muye Huang, Zihan Ma, Jiashuai Liu, Jun Liu
url: http://arxiv.org/abs/2609.01422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Rollouts to Recipes: Self-Contained Post-Training for LLMs

## Abstract
Post-training large language models usually applies a single training recipe to all samples, even though the model's own rollouts reveal different sample-level learning states. We propose Self-Routing, a behavior-conditioned post-training framework that uses rollout correctness and confidence to decide how each sample should be optimized. Depending on its behavior state, a sample is routed to GRPO, on-policy self-distillation, regularization, or skipping, allowing training to adapt without external teachers, extra annotations, or additional sampling. Experiments on mathematical reasoning across Qwen3 and Qwen3.5 backbones show that Self-Routing consistently improves over uniform GRPO, uniform OPSD, fixed mixtures, and simpler routing baselines. Further analyses show that the routing distribution changes over training and reduces unnecessary updates on low-signal or already stable samples.

## Metadata
- **Published**: 2026-09-01T15:36:26Z
- **Authors**: Yifei Li, Lingling Zhang, Muye Huang, Zihan Ma, Jiashuai Liu, Jun Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01422v1)