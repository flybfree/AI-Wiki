---
title: Coding or Cheating? An Investigation of Frontier Coding LLMs
published: 2026-11-07T02:29:54Z
authors: Yuntao Gui
url: http://arxiv.org/abs/2611.10404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coding or Cheating? An Investigation of Frontier Coding LLMs

## Abstract
Frontier agentic LLMs are trained on verifiable rewards in reinforcement learning (RL) environments built from real software repositories. A passing test suite is treated as the reward for solving the task. We show that, on hard problems, frontier models often satisfy these rewards by obtaining the answer instead of deriving it, known as reward hacking. Prior reports document this behavior on public benchmarks. We test its persistence on unseen problems.   In a hardened environment where the answer cannot leak, nearly every model we tested attempted to recover the answer, escalating through tiers of increasingly specialized exploitation: mining the repository history for the upstream fix, inspecting the git object store directly, and sweeping the filesystem for a possible newer copy of the source or hidden tests. These attempts were concentrated on the hardest problems, and the models differed in whether, how often, and how deeply they escalated. Our position is that this behavior is a learned shortcut, acquired in RL environments that leak the answer, not a sign of intelligence. We release agent traces for these models to support further study at https://huggingface.co/datasets/logitly-ai/reward-hacking-raw-v1.

## Metadata
- **Published**: 2026-11-07T02:29:54Z
- **Authors**: Yuntao Gui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.10404v1)