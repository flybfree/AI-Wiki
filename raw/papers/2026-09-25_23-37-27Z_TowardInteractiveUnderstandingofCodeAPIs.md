---
title: Toward Interactive Understanding of Code APIs
published: 2026-09-25T23:37:27Z
authors: Dhananjay Ashok, Jesse Thomason, Jonathan May
url: http://arxiv.org/abs/2609.32081v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward Interactive Understanding of Code APIs

## Abstract
Empowered by advances in Language Model agents, systems have made substantial strides in code generation and understanding. However, these approaches often rely on read access to the relevant code, an assumption which does not hold when dealing with external APIs. In this work, we introduce the PAU (Python API Understanding) benchmark, where we provide models with black-box, API-level access to code snippets. Models must query the API with exploratory inputs and draw insights from the resulting outputs, with the goal of describing the snippet's true functionality. By treating the code snippets as external tools that must be understood via interaction alone, PAU studies the more general problem of unsupervised tool understanding, specifically for tools implemented as Python methods. Despite recent progress in coding agents, even frontier models struggle to achieve high performance on PAU, with the best model (Claude-4-Opus) failing to understand over 45% of the PAU test set. An investigation into the common error modes reveals that models are overconfident; they often overrate the quality of their current hypothesis, leading to insufficient exploration and premature termination. Finally, we take inspiration from the Asymmetric Actor Critic (AAC) paradigm, frequently used in robot learning, to post-train models for interactive code understanding. Models trained with AAC conduct more active exploration of the APIs, with an AAC-tuned Qwen3-8B model matching the performance of GPT-5-mini.

## Metadata
- **Published**: 2026-09-25T23:37:27Z
- **Authors**: Dhananjay Ashok, Jesse Thomason, Jonathan May
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32081v1)