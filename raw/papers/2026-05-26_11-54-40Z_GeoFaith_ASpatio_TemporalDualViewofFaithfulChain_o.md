---
title: GeoFaith: A Spatio-Temporal Dual View of Faithful Chain-of-Thought
published: 2026-05-26T11:54:40Z
authors: Weijiang Lv, Wentong Zhao, Jiayu Wang, Yuhao Wu, Jiaheng Wei, Xiaobo Xia
url: http://arxiv.org/abs/2605.26893v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GeoFaith: A Spatio-Temporal Dual View of Faithful Chain-of-Thought

## Abstract
Chain-of-Thought (CoT) reasoning has advanced large language models (LLMs), but outcome-based supervision leads to pervasive post-hoc rationalization, producing plausible yet unfaithful reasoning chains. Most prior faithfulness assessment methods are either unscalable, expensive, or unreliable. We propose GeoFaith, a spatio-temporal framework that leverages latent geometric structure and entropy dynamics to diagnose and enforce faithful reasoning. We develop a scalable bootstrapping pipeline expanding step-level annotations from 1k to 20k samples across four domains, train an 8B faithfulness detector outperforming GPT-5 on standard benchmarks, and design a faithfulness-aware reinforcement learning framework jointly optimizing outcome correctness, process faithfulness, and trajectory consistency. Experiments show the proposed method achieves superior performance on both faithfulness detection and downstream reasoning, producing shorter, more interpretable chains without sacrificing accuracy. Our code will be made available publicly.

## Metadata
- **Published**: 2026-05-26T11:54:40Z
- **Authors**: Weijiang Lv, Wentong Zhao, Jiayu Wang, Yuhao Wu, Jiaheng Wei, Xiaobo Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.26893v1)