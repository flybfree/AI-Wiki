---
title: rl-triton: High-Performance Triton GPU Kernels for Reinforcement Learning Credit Assignment
published: 2026-08-18T10:58:20Z
authors: Lars Simon Zehnder
url: http://arxiv.org/abs/2608.17641v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# rl-triton: High-Performance Triton GPU Kernels for Reinforcement Learning Credit Assignment

## Abstract
We present rl-triton, an open-source library of high-performance GPU kernels for reinforcement learning credit assignment, implemented in Triton. The core contribution is a unified associative scan framework that recasts seven distinct RL estimation algorithms - Generalized Advantage Estimation (GAE), V-Trace, Retrace($λ$), TD($λ$) returns, discounted returns, eligibility traces, and episodic prefix sums - as instances of a single first-order linear recurrence solved in $O(\log T)$ parallel steps. All algorithms share the same associative scan operator, with algorithm-specific fused Triton kernels constructing their recurrence coefficients on-chip. We verify the associative operator algebraically and define the treatment of terminated and truncated episodes explicitly. Benchmarks show a 1.6-5.70$\times$ full-call speedup over a vectorized torch.compile baseline in the massively parallel simulation regime (thousands of environments, short rollouts). The reported range covers all seven algorithms on both GPUs, both with and without per-step truncation handling. For most algorithms, speedups increase at longer sequence lengths, as the baseline requires more scan stages as $\log T$ grows, each adding an intermediate HBM round-trip. The library is available at https://github.com/simonsays1980/rl-triton.

## Metadata
- **Published**: 2026-08-18T10:58:20Z
- **Authors**: Lars Simon Zehnder
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17641v1)