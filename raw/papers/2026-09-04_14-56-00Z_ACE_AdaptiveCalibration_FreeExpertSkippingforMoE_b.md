---
title: ACE: Adaptive Calibration-Free Expert Skipping for MoE-based LLMs
published: 2026-09-04T14:56:00Z
authors: Zukang Xu, Zhixiong Zhao, Xing Hu, Jiangyong Yu, Houji Wen, Jun Li, Zhe Jiang, Dawei Yang
url: http://arxiv.org/abs/2609.05228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ACE: Adaptive Calibration-Free Expert Skipping for MoE-based LLMs

## Abstract
Mixture-of-Experts (MoE) architectures provide an efficient paradigm for scaling large language models (LLMs), yet fixed top-k routing activates the same number of expert slots for every token, causing substantial redundant computation. Existing expert-skipping methods often rely on router confidence, calibration data, or additional training, and therefore cannot reliably estimate the actual contribution of routed experts. To this end, we propose ACE, a training-free, calibration-free, and checkpoint-preserving framework for token-adaptive expert skipping in MoE-based LLMs. ACE contains two complementary components: 1) Global Spectral Proxy (GSP), which estimates global transformation capacity from the coupled gate, up, and down projections together with RMSNorm scaling; and 2) Router-Conditioned Refinement (RCR), which constructs expert-specific direction prototypes from centered router weights and evaluates expert responses along routing-preferred directions. During inference, ACE combines both estimates with runtime router gates and skips an expert slot only when both views identify it as low-contribution, while always retaining the top-1 expert. All expert statistics are computed offline, leaving only table lookups and lightweight scalar operations online. Extensive experiments across three MoE-based LLMs and eight benchmarks demonstrate that ACE consistently outperforms existing static and dynamic baselines, with increasingly pronounced advantages under aggressive expert skipping. For instance, at a 50% skipping ratio on Qwen3.6-35B-A3B, ACE reduces WikiText-2 perplexity by 7.96% and improves average downstream accuracy by 4.15 percentage points over the strongest competing method.

## Metadata
- **Published**: 2026-09-04T14:56:00Z
- **Authors**: Zukang Xu, Zhixiong Zhao, Xing Hu, Jiangyong Yu, Houji Wen, Jun Li, Zhe Jiang, Dawei Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05228v1)