---
title: ArborMem: Navigating Interaction States with Memory Forests
published: 2026-08-18T08:54:55Z
authors: Zongwei Lv, Yuemeng Xu, Yilun Yao, Siyi Ding, Xinyu Tan, Yaoming Li, Guangxiang Zhao, Weihong Lin, Lin Sun, Xiangzheng Zhang, Tong Yang
url: http://arxiv.org/abs/2608.17534v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ArborMem: Navigating Interaction States with Memory Forests

## Abstract
Large language models increasingly serve as persistent conversational assistants, requiring memory that preserves relevant experience and maintains continuity across interactions. Existing methods improve access to conversational history through long-context processing, selective retrieval, and structured memory organization. However, most systems treat memory access as retrieving relevant past information without first determining which prior interaction state the current turn resumes. This limitation becomes particularly important when conversations interleave multiple tasks, people, and plans that may be interrupted and later revisited. We introduce ArborMem, an online memory framework that represents a long-running conversation as a navigable forest of interaction states. Each branch preserves a locally coherent trajectory, while the forest maintains multiple trajectories that may later be resumed. For each new input, ArborMem localizes the relevant state, restores its branch-local context, and augments it with reusable evidence retrieved across branches, preserving interaction continuity without conflating semantically related but structurally distinct trajectories. Existing long-term memory benchmarks cover diverse memory and reasoning capabilities but do not explicitly isolate branch-structured challenges. We therefore introduce BranchMemEval, a controlled diagnostic benchmark for interleaved and resumable interaction trajectories. Experiments on LongMemEval, LoCoMo, BEAM 100K, and BranchMemEval show that ArborMem outperforms the strongest baselines by 3.36 to 10.31 percentage points on the three established benchmarks and by 5.0 points on BranchMemEval. Its advantage grows under constrained read budgets, while complete memory queries remain below half a second.

## Metadata
- **Published**: 2026-08-18T08:54:55Z
- **Authors**: Zongwei Lv, Yuemeng Xu, Yilun Yao, Siyi Ding, Xinyu Tan, Yaoming Li, Guangxiang Zhao, Weihong Lin, Lin Sun, Xiangzheng Zhang, Tong Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17534v1)