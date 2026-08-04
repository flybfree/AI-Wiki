---
title: Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling
published: 2026-08-03T08:32:50Z
authors: Cunchen Hu, Liangliang Xu, Tian Liu, Min Lyu, Yongkun Li, Sa Wang, Shuo Quan, Yanan Yang, Wenda Tang, Yiduo Wang, Fu Yu, Jie Wu
url: http://arxiv.org/abs/2608.01891v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling

## Abstract
Large language model (LLM) serving spans diverse applications with stringent service-level objectives (SLOs), often requiring GPUs to run at maximum frequencies and increasing energy consumption. Existing energy-management approaches adapt GPU frequencies only at the request or inference-phase level, overlooking operator-level differences in frequency sensitivity between Attention and feed-forward networks (FFNs). We find that the energy-optimal frequencies of Attention and FFN (A/F) differ and vary with the inference phase, workload, and system configurations. However, runtime variability and independent A/F frequency control create a large search space and high communication overhead. To address these challenges, we present AFlex, a framework that jointly optimizes resource provisioning and GPU frequency scaling for disaggregated A/F serving. AFlex introduces a global scheduler and a local operator-level dynamic voltage and frequency scaling (DVFS) controller to determine A/F resource allocations and frequencies. It further introduces an interleaved A/F pipeline with dynamic microbatch depth and adaptive request batching to reduce pipeline bubbles. We implement AFlex in SGLang and evaluate it on NVIDIA A800 GPUs using Qwen3-32B and Mixtral-8$\times$7B under production Conversation and Coding traces. \AFlex reduces energy per token by up to 49\% over state-of-the-art disaggregated serving and 48\% over frequency-scaling systems while satisfying TTFT and TPOT SLOs.

## Metadata
- **Published**: 2026-08-03T08:32:50Z
- **Authors**: Cunchen Hu, Liangliang Xu, Tian Liu, Min Lyu, Yongkun Li, Sa Wang, Shuo Quan, Yanan Yang, Wenda Tang, Yiduo Wang, Fu Yu, Jie Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01891v1)