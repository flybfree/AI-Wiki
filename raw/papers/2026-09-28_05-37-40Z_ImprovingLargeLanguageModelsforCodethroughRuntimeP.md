---
title: Improving Large Language Models for Code through Runtime Program-State Reasoning
published: 2026-09-28T05:37:40Z
authors: Hongwei Li, Spandan Garg, Yufan Huang
url: http://arxiv.org/abs/2609.34359v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Improving Large Language Models for Code through Runtime Program-State Reasoning

## Abstract
Large language models receive limited explicit training in reasoning about runtime program states. We study whether training models to reason about runtime program states improves downstream software-engineering capabilities. We introduce two complementary program-state reasoning tasks. Buggy input-output reasoning requires a model to generate a concrete input that exposes a behavioral difference between a buggy program and a hidden correct implementation and to predict the resulting execution behavior. Precondition-postcondition reasoning requires an agent to symbolically characterize a bug-triggering precondition, predict the expected postcondition, explain their causal connection, and instantiate this reasoning as an executable regression test. By incorporating these two tasks into a staged post-training pipeline, we develop Comet-9B, a 9B language model based on Qwen3.5-9B Base. We evaluate the resulting checkpoints on repository-level patch generation, regression-test generation, and security PoC generation. Adding both program-state reasoning tasks to supervised fine-tuning (SFT) on issue resolution improves success rates by 7.25 percentage points on SWE-bench Pro and 9.70 points on SWT-Bench Verified. Sequential reinforcement learning on the two tasks yields further gains of 7.25, 26.79, and 4.67 percentage points on SWE-bench Pro, SWT-Bench Verified, and CyberGym, respectively. Despite having only 9B parameters, Comet-9B achieves a score comparable to the reported GPT-5.2 result on SWE-bench Pro and matches the reported success rate of a GPT-4o-based agent on SWT-Bench Verified.

## Metadata
- **Published**: 2026-09-28T05:37:40Z
- **Authors**: Hongwei Li, Spandan Garg, Yufan Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34359v1)