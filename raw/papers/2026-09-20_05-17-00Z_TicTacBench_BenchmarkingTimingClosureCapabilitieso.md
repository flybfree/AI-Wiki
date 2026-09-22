---
title: TicTacBench: Benchmarking Timing Closure Capabilities of Coding Agents
published: 2026-09-20T05:17:00Z
authors: Bowei Wang, Zhigang Fang, Zhijie Yang, Renzhi Chen, Shanshan Li, Lei Wang
url: http://arxiv.org/abs/2609.23363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TicTacBench: Benchmarking Timing Closure Capabilities of Coding Agents

## Abstract
Recent advances in large language models (LLMs) have led to the emergence of coding agents capable of performing complex engineering tasks, including register-transfer level (RTL) design and optimization. Existing RTL benchmarks mainly evaluate functional correctness and performance, power, and area (PPA) of the generated RTL designs, leaving agents' ability for \emph{timing closure} under-evaluated. We propose TicTacBench, a benchmark specifically designed to evaluate coding agents' capabilities for RTL-level timing closure under post-place-and-route (post-PnR) evaluation. TicTacBench contains 30 diverse tasks, each provided with a suboptimal RTL design, realistic timing constraints, functional equivalence verification, and timing reports. With over 300 runs of coding agents driven by 8 frontier LLMs, we find that even the best agent can only close 53.3\% of tasks with 7.18\% area-delay product (ADP) degradation and 8.83\% energy-delay-squared product (EDDP) improvement on average. We identify common failure categories that explain why agents fail to close timing. Then we propose TicTacSkill, a new method that guides agents to follow standard timing-closure procedures and improves the Timing Closure Rate by 9\%. These results suggest that while coding agents have made significant progress in RTL design, their timing-closure capability still has substantial room for improvement.

## Metadata
- **Published**: 2026-09-20T05:17:00Z
- **Authors**: Bowei Wang, Zhigang Fang, Zhijie Yang, Renzhi Chen, Shanshan Li, Lei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23363v1)