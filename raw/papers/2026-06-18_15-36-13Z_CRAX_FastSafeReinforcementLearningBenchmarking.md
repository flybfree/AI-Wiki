---

title: "CRAX: Fast Safe Reinforcement Learning Benchmarking"
published: "2026-06-18T15:36:13Z"
authors: Tristan Tomilin, Mourad Boustani, Mickey Beurskens, Thiago D. Simão
url: http://arxiv.org/abs/2606.20376v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# CRAX: Fast Safe Reinforcement Learning Benchmarking



**Source**: [Original Paper](http://arxiv.org/abs/2606.20376v1)
## Abstract
Safety is a core concern for deploying reinforcement learning (RL) agents in real-world domains such as robotics and autonomous driving. While benchmarks have been central to progress in RL, existing safety benchmarks with high-fidelity 3D physics remain computationally slow, limiting large-scale experimentation and rapid prototyping. To address this gap, we propose CRAX (Constrained RL Accelerated with JAX). Built on top of the MuJoCo XLA (MJX) physics engine with realistic 3D dynamics, CRAX leverages vectorized operations and hardware acceleration, yielding up to ~100x speedups over comparable CPU-based safety benchmarks. The benchmark features six environment suites and three agent-specific tasks, each spanning three difficulty levels. Evaluating six popular safe RL methods shows that no single approach dominates across all tasks, and reveals the trade-offs between performance and safety. We find that curriculum learning across difficulty levels and safety transfer can improve performance over direct training in harder settings.

## Metadata
- **Published**: 2026-06-18T15:36:13Z
- **Authors**: Tristan Tomilin, Mourad Boustani, Mickey Beurskens, Thiago D. Simão
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.20376v1)