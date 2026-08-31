---
title: LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering
published: 2026-08-28T12:44:54Z
authors: Yi Wang, Haopeng Zhang, Chengxiang Huang, Rui Dai, Kaikui Liu, Piotr Koniusz, Xiangxiang Chu
url: http://arxiv.org/abs/2608.28281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering

## Abstract
Loop Engineering is emerging as a practice for organizing development work around coding agents. Instead of writing each prompt by hand, practitioners design loops that monitor progress, assign work, run checks, and decide what the agent should do next. Even with a capable coding agent, a loop may trust a stale progress note, skip needed verification, spend its budget in the wrong direction, or stop before the task is safe to submit. Yet the final outcome of one end-to-end run cannot tell whether success or failure reflects the loop's guidance or the coding agent's ability to carry out the task. We introduce LoopArena, a benchmark for evaluating how well one model can guide a separate coding agent through a long-running task. The model under evaluation is the \textbf{Controller}: after each coding round, it receives a structured summary of the run and instructs a separate, fixed coding agent, the \textbf{Worker}, on what to do or verify next, or decides whether to stop. LoopArena evaluates this ability in three complementary settings that differ in execution scope and cost. Type I scores next-step Loop Contract selection through execution-validated questions without running the Worker at evaluation time. Type II executes repeated control over a selected slice of a full task, while Type III evaluates the paired full task from its original state. On full tasks, the best observed Strict Success Rate is \textbf{24.69\%}, leaving substantial room for improvement in long-horizon loop control. Across Controllers, the paired reduction in estimated inference cost averages \textbf{64.4\%}, and Type II produces a similar ordering under the main Core criterion (Spearman's \(ρ=\textbf{0.9747}\)). We release the benchmark data and evaluation code at https://github.com/AMAP-ML/LoopArena .

## Metadata
- **Published**: 2026-08-28T12:44:54Z
- **Authors**: Yi Wang, Haopeng Zhang, Chengxiang Huang, Rui Dai, Kaikui Liu, Piotr Koniusz, Xiangxiang Chu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28281v1)