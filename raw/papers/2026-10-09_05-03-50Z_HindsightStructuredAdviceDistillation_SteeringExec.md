---
title: Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics
published: 2026-10-09T05:03:50Z
authors: O. Ozan Koyluoglu
url: http://arxiv.org/abs/2610.13000v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hindsight Structured Advice Distillation: Steering Executor Agents with Advisors Trained on Their Failures and Task Characteristics

## Abstract
Language-model agents are used for specialized work such as financial research, healthcare and law. Such agents are often capable enough for a task but still miss its details. In finance, for example, these details include which filing reports a figure or how a company discloses a metric. Retraining the agent to learn these details is expensive, and often impossible when the agent is a closed or shared system. Writing the missing know-how into the agent's prompt makes the prompt long and identical for every input, although different inputs need different guidance. We propose to learn to generate this guidance instead. A small advisor model reads each input and writes structured advice, which is appended to the prompt of a frozen executor. The advisor is trained with hindsight, following work on distillation with privileged information. On a training pool with graded answers, we analyse the executor's failures, run it under several strategies to see which one worked on each input, and let a teacher that sees the grades and the traces write the advice that would have helped. The advisor then learns, by supervised fine-tuning, to write that advice from the input alone. Because the student is a separate small model rather than the executor, it is cheap to train and adds little latency. We call this approach hindsight structured advice distillation (HSAD). On FrontierFinance, a public benchmark of expert-written financial research queries, an 8B advisor raises the qualification rate of Samaya's proprietary research agent, which already leads the benchmark's leaderboard, from 52.9% to 56.6%. This is above the agent's own high-effort configuration, at 37% lower cost per query. We study the generalization of the proposed approach, and in particular show that HSAD also improves results on WebShop, BIRD text-to-SQL and ExpertLongBench.

## Metadata
- **Published**: 2026-10-09T05:03:50Z
- **Authors**: O. Ozan Koyluoglu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13000v1)