---
title: CompMat-Bench: Benchmarking AI Agents for Computational Materials Science
published: 2026-09-30T19:37:09Z
authors: Chenmu Zhang, Levi Felix, Jun-Jie Zhang, Xingfu Li, Xuelian Jiang, Tao Jiang, Subhendu Mishra, Xixi Qin, Boris Yakobson
url: http://arxiv.org/abs/2610.00636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CompMat-Bench: Benchmarking AI Agents for Computational Materials Science

## Abstract
Evaluating AI agents on scientific research tasks is constrained by the time and resources required for the underlying experiments or calculations. In computational materials research, repeating the same expensive simulations across agents and trials can make evaluation impractical. We introduce CompMat-Bench, a benchmark of 94 tasks derived from recently published computational materials studies, each asking agents to complete a step toward achieving the study's scientific goal. We reproduce the research steps in advance and assess agents on preparing inputs and analyzing outputs for expensive simulations, so expensive simulations can be avoided during evaluation. The reproduced inputs and results serve as ground truth for grading agents with fixed rules, without an LLM judge. The benchmark supports four evaluation conditions: single tasks and workflows composed of related tasks, each with full or reduced methodological guidance. With full guidance on single tasks, agents based on three LLMs demonstrate the ability to complete individual materials research steps, with pass rates of 66.0-90.4% across 94 tasks. Both longer workflows and reduced guidance can limit agent performance, but in different ways for different agents: they lower the pass rates of the weaker agents, whereas the strongest agent falls only when a long workflow is combined with reduced guidance. Failure analysis attributes most failures to scientific errors rather than to errors in software usage. CompMat-Bench provides a basis for comparing agents on the steps of real materials research and for analyzing agent failure modes.

## Metadata
- **Published**: 2026-09-30T19:37:09Z
- **Authors**: Chenmu Zhang, Levi Felix, Jun-Jie Zhang, Xingfu Li, Xuelian Jiang, Tao Jiang, Subhendu Mishra, Xixi Qin, Boris Yakobson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00636v1)