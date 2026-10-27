---
title: More: Mode-Optimized Reasoning with Self-Adaptive Effort for Self-Evolving Agents
published: 2026-10-24T14:03:20Z
authors: Dianxing Shi, Dingjie Fu, Tianyu Lei, Wangjie Qiu
url: http://arxiv.org/abs/2610.33684v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# More: Mode-Optimized Reasoning with Self-Adaptive Effort for Self-Evolving Agents

## Abstract
Self-evolving training improves the performance of agents on difficult tasks through verifiable feedback, but it often applies costly deliberation uniformly across tasks. To address this problem, we propose Mode-Optimized Reasoning with Self-Adaptive Effort (MORE), a self-evolving training framework that adaptively selects both reasoning form and computational effort for each task. Specifically, MORE follows a two-stage training paradigm: (i) \emph{Stage 1} establishes a compact prior over direct answering, short and long chain-of-thought, and code-based reasoning, and (ii) \emph{Stage 2} self-evolves this prior with Mode-Adaptive and Test-time Effort PPO (MATE-PPO) on generated, verifiable task streams without curated data. By learning mode selection and token expenditure jointly, MORE allocates concise reasoning to tasks that permit it while retaining extended deliberation where it is useful. Across coding, mathematics, and general-reasoning benchmarks, MORE achieves consistent performance gains on Base and Coder backbones at model scales from 3B to 14B. During inference, MORE demonstrates higher accuracy and better efficiency, with markedly shorter response lengths and reduced inference time.

## Metadata
- **Published**: 2026-10-24T14:03:20Z
- **Authors**: Dianxing Shi, Dingjie Fu, Tianyu Lei, Wangjie Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33684v1)