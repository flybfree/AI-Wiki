---
title: Training Advisors for LLM Agents from Task Outcomes
published: 2026-10-07T11:14:26Z
authors: Sergei Polezhaev, Barys Liskavets, Ori Press, Alexander Golubev
url: http://arxiv.org/abs/2610.09858v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Advisors for LLM Agents from Task Outcomes

## Abstract
Large language model agents tackle multi-step tasks by interleaving reasoning and tool calls with observations from the environment. Prior work has shown that natural-language feedback can help these agents revise their decisions during task execution. We introduce Caddie, a method for training critics to provide natural-language analysis and advice as agents work through a task. Unlike approaches that rely on step-level labels or reference critiques, Caddie learns from whether the agent ultimately succeeds after receiving the critic's feedback. We optimize the critic through reinforcement learning while keeping the base model frozen. Trained on multi-hop question answering with a single base model, our Qwen3-4B critic improves success rates across four base models of different scales and architectures, including three not used during critic training. On the MuSiQue benchmark, the trained critic improves Qwen3-4B's success rate by more than 25 percentage points, surpassing the performance of Kimi K3 without a critic. The same critic also yields gains on out-of-domain interactive benchmarks, including $τ^3$ and DeepDive, with no additional training. Our results show that agents can decide when to seek help from a critic at inference time and that outcome-based critic training can produce guidance that transfers across base models and task domains.

## Metadata
- **Published**: 2026-10-07T11:14:26Z
- **Authors**: Sergei Polezhaev, Barys Liskavets, Ori Press, Alexander Golubev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09858v1)