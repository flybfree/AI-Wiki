---
title: Not All LLM Reasoning is Visible in the Chain-of-Thought
published: 2026-07-24T21:32:48Z
authors: Vatsal Baherwani, Tom Goldstein, Ashwinee Panda
url: http://arxiv.org/abs/2607.22925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not All LLM Reasoning is Visible in the Chain-of-Thought

## Abstract
A key question for AI safety is whether a language model expresses all of its reasoning in its output tokens. We demonstrate a concrete failure mode where frontier models exhibit invisible reasoning by leveraging semantically irrelevant filler tokens to improve performance on synthetic reasoning tasks. We evaluate 13 frontier language models across three tasks and find that many models benefit significantly from filler tokens, with accuracy improvements of up to 13 percentage points. The benefit depends on which tokens are used and differs across models. We further show that filler tokens enable Claude Opus 4.5 to satisfy a hidden modular arithmetic constraint without sacrificing accuracy on its primary task, demonstrating that invisible reasoning can serve objectives entirely invisible to CoT monitoring. Reinforcement learning gives Qwen3-235B strong preferences over filler token content, but neither RL nor supervised fine-tuning produces a filler token benefit that persists at test time. Our results indicate that frontier models already perform consequential computation with no interpretable trace in their output tokens.

## Metadata
- **Published**: 2026-07-24T21:32:48Z
- **Authors**: Vatsal Baherwani, Tom Goldstein, Ashwinee Panda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22925v1)