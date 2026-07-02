---
title: Message Passing Enables Efficient Reasoning
published: 2026-07-01T15:35:04Z
authors: Xuecheng Liu, Daman Arora, Gokul Swamy, Andrea Zanette
url: http://arxiv.org/abs/2607.01077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Message Passing Enables Efficient Reasoning

## Abstract
While inference-time scaling has improved the reasoning abilities of large language models (LLMs), the need to generate long chains-of-thought (CoTs) is a computational bottleneck. Thus, in contrast to sequential scaling methods like CoT, recent parallel scaling techniques instead use fork and join (FJ) primitives to divide work across multiple LLM threads. However, in the fork-join paradigm, threads are typically transient and do not communicate pointwise with one another which limits scalability. To tackle this, we introduce Message Passing Language Models (MPLMs), a framework for LLM reasoning in which threads communicate directly via lightweight send and receive primitives. MPLMs enable efficient scaling through two key mechanisms: (1) reduced communication costs, achieved by avoiding redundant context sharing, and (2) preemption, which allows threads to terminate early based on partial information from their peers.   We demonstrate the promise of MPLMs on 3 classes of tasks. First, on Sudoku puzzles, we show that MPLMs require an asymptotically smaller context than both serial CoT and parallel FJ. We then fine-tune a single model to solve 25 x 25 puzzles that remain challenging for standard CoT and FJ approaches, as well as frontier reasoning models without tools. Second, on 3-SAT puzzles, the capability of preemption allows termination of unpromising branches, which results in improved efficiency. Finally, we show that appropriately prompted large pre-trained models follow the MPLM protocol, achieving competitive results on long-context question answering relative to popular fork-join approaches.

## Metadata
- **Published**: 2026-07-01T15:35:04Z
- **Authors**: Xuecheng Liu, Daman Arora, Gokul Swamy, Andrea Zanette
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.01077v1)