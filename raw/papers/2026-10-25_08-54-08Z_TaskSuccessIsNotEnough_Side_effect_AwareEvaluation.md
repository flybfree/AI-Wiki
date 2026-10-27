---
title: Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents
published: 2026-10-25T08:54:08Z
authors: Jiaju Huang, Shaobin Chen, Xinglong Liang, Xinyu Ma, Hao Yang, Wei Ke, Tao Tan, Yue Sun
url: http://arxiv.org/abs/2610.34167v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents

## Abstract
Tool-using language model agents are usually evaluated by whether they finish the user's task. That metric misses a common failure: an agent can complete the requested work while also taking an unauthorized side-effecting action, such as writing to the wrong object, expanding the scope of the request, or contacting an unintended recipient. We call this failure mode collateral damage (CD). We introduce SABench (Side-effect-Aware Benchmark), a benchmark of 201 email, calendar, and ticket tasks. Each task crosses one of four state structures (independent, dependent, externally reachable, cross-tool) with one of four trap families (ambiguity, mis-targeting, cascade harm, overreach), and each task has a deterministic trace-based oracle for both goal satisfaction and authorization compliance. Across 2,211 model-task pairs from 11 frontier LLMs spanning major commercial and open model families, 15.2% of all runs incur CD, with risk concentrated in ambiguity tasks (38.8% violation rate) while non-ambiguous traps average 8.4% CD. Among goal-satisfied runs, 12.8% still produce unauthorized writes. Cross-tool and dependent states have about twice the CD rate of independent states. CD rates vary by 4.7x across models at comparable goal rates, which suggests that task success alone is a poor proxy for safe tool use. The SABench task corpus is released at https://huggingface.co/datasets/Phaedrus/sabench; the traces, oracle, code, and analysis pipeline are released at https://github.com/hjj194/sabench-artifact.

## Metadata
- **Published**: 2026-10-25T08:54:08Z
- **Authors**: Jiaju Huang, Shaobin Chen, Xinglong Liang, Xinyu Ma, Hao Yang, Wei Ke, Tao Tan, Yue Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34167v1)