---
title: Online Self-Weighted Fine-Tuning
published: 2026-09-01T05:12:45Z
authors: Haiquan Wen, Yiwei He, Bei Peng, Guangliang Cheng
url: http://arxiv.org/abs/2609.00734v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Online Self-Weighted Fine-Tuning

## Abstract
Standard supervised fine-tuning (SFT) assigns the same explicit loss weight to every expert demonstration, regardless of the model's changing competence over training queries. Reinforcement learning (RL) based methods adapt update strength using model-generated rollouts, but often require substantially more sampling and can be unstable on hard tasks. We propose \textbf{Online Self-Weighted Fine-Tuning (OSW-FT)}, a simple method that augments SFT with online, trajectory-level weighting. For each query, OSW-FT estimates the model's current success rate using a small number of inference-only rollouts and rescales the standard SFT loss accordingly. The optimization direction remains anchored to the expert trajectory, while the update magnitude adapts online. For binary-verifiable reasoning, we connect this weighting to SFT and RL at the gradient level, inspired by variance-reduction principles. The resulting estimator is unbiased for the exact OSW-FT surrogate update for any finite rollout count, and we analyze convergence with respect to the corresponding surrogate objective. Evaluated across Qwen3 series ranging from 0.6B to 4B on multiple challenging benchmarks (e.g., AIME), OSW-FT consistently improves over SFT on small-to-medium scale models. OSW-FT offers a favorable compute-performance trade-off as a practical approach for fine-tuning small-to-medium LLMs on binary-verifiable reasoning tasks with only \textbf{2 online rollouts}.

## Metadata
- **Published**: 2026-09-01T05:12:45Z
- **Authors**: Haiquan Wen, Yiwei He, Bei Peng, Guangliang Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00734v1)