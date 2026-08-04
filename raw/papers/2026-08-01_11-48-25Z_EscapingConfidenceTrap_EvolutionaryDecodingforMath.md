---
title: Escaping Confidence Trap: Evolutionary Decoding for Mathematical Reasoning in Diffusion LLMs
published: 2026-08-01T11:48:25Z
authors: Zhenhong Sun, Hanqing Zhao, Yatao Bian, Rongcheng Tu, Liuyue Xie, Xu Zhang, Jue Wang, Davide Modolo, Daoyi Dong, Dacheng Tao
url: http://arxiv.org/abs/2608.00605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Escaping Confidence Trap: Evolutionary Decoding for Mathematical Reasoning in Diffusion LLMs

## Abstract
Diffusion large language models (dLLMs) have emerged as a promising alternative to autoregressive LLMs, offering efficient generation through block-wise progressive unmasking. However, their strong general-purpose performance does not necessarily translate into reliable mathematical reasoning, where correctness depends on preserving coherent numerical-symbolic reasoning trajectories. In this work, we analyze the decoding trajectories of LLaDA 2.0 and identify a recurring diffusion confidence trap: local token confidence can become misaligned with global reasoning correctness during progressive block decoding. Our analysis reveals two representative failure regimes: sampling-sensitive failures, where correct paths exist but are unstable, and sampling-consistent failures, where repeated sampling converges to repetitive high-confidence but incorrect continuations. Motivated by this observation, we propose Evolutionary Decoding, a training-free test-time scaling framework that views diffusion decoding as an evolutionary process over candidate reasoning states. The framework combines step-wise selection, which preserves useful numerical-symbolic signals and suppresses repetitive patterns, with block-wise mutation, which introduces structured alternatives to escape incorrect high-confidence basins. Experiments on multiple benchmarks show that Evolutionary Decoding improves LLaDA 2.0 over confidence-based decoding, leading to more reliable mathematical reasoning.

## Metadata
- **Published**: 2026-08-01T11:48:25Z
- **Authors**: Zhenhong Sun, Hanqing Zhao, Yatao Bian, Rongcheng Tu, Liuyue Xie, Xu Zhang, Jue Wang, Davide Modolo, Daoyi Dong, Dacheng Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00605v1)