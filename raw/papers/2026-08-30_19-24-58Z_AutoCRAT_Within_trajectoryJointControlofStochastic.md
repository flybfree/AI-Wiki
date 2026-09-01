---
title: AutoCRAT: Within-trajectory Joint Control of Stochasticity and Compute for LLM Reasoning
published: 2026-08-30T19:24:58Z
authors: Hanjun Luo, Qiushi Liu, Jingya Zhang, Haihong Pang, Jiaheng Wen, Yifei Ma, Yu Yao, Chengxi Zhang, Hanrong Zhang, Yankai Chen, Hanan Salam
url: http://arxiv.org/abs/2608.29988v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoCRAT: Within-trajectory Joint Control of Stochasticity and Compute for LLM Reasoning

## Abstract
Large language models (LLMs) achieve strong reasoning performance, which depends critically on inference-time decisions. Yet these decisions are commonly handled by static, one-size-fits-all policies, limiting adaptation to diverse tasks and reasoning stages. Recent adaptive methods partially address this limitation, but they primarily adapt either decoding stochasticity (how the model explores) or reasoning compute (how long the model reasons) in isolation, leaving their interaction within a single reasoning trajectory unmodeled. To address this challenge, we shift toward a within-trajectory joint control view, and instantiate it in AutoCRAT, a decoder-side controller for frozen backbones. Using only signals available during decoding, AutoCRAT jointly adjusts sampling stochasticity and reasoning budget during generation. AutoCRAT operates over a discrete action space and updates control decisions only at semantic boundaries, improving stability while remaining responsive to the evolving reasoning process. Comprehensive evaluation across 6 benchmarks demonstrates that AutoCRAT (I) uses 13.8-52.7% fewer inference tokens on average than recommended static configurations, (II) surpasses recommended static and adaptive baselines by 1.5-4.5% in relative accuracy, and (III) enjoys strong cross-backbone transferability.

## Metadata
- **Published**: 2026-08-30T19:24:58Z
- **Authors**: Hanjun Luo, Qiushi Liu, Jingya Zhang, Haihong Pang, Jiaheng Wen, Yifei Ma, Yu Yao, Chengxi Zhang, Hanrong Zhang, Yankai Chen, Hanan Salam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29988v1)