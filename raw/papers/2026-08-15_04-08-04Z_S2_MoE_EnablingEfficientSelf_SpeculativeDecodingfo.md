---
title: S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices
published: 2026-08-15T04:08:04Z
authors: Haochen Huang, Shengxuan Qiu, Meng Li
url: http://arxiv.org/abs/2608.15018v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices

## Abstract
Deploying large language models (LLMs) for inference on edge devices is challenging due to severe memory and bandwidth constraints. While speculative decoding and Mixture-of-Experts (MoE) have been proposed to improve inference efficiency, naively combining them often incurs excessive verification overhead and poor expert reuse, limiting their effectiveness in memory-bound edge settings. In this work, we propose S2-MoE, an efficient self-speculative decoding framework for MoE inference on edge devices. S2-MoE reduces redundant verification through routing-aware adaptive speculative expansion, improves verification efficiency with reuse-aware expert gating, and aligns draft and target execution via shared context. Implemented in llama.cpp, S2-MoE achieves up to 5.3x speedup (about 2.0x on average) over standard autoregressive de?coding across diverse MoE models and datasets on edge devices.Code is available at https://github.com/angerybob/S2-MoE.

## Metadata
- **Published**: 2026-08-15T04:08:04Z
- **Authors**: Haochen Huang, Shengxuan Qiu, Meng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15018v1)