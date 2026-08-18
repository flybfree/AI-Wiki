---
title: Measuring Reward Hacking and Reasoning-Answer Decoupling Under Position-Confounded Optimization
published: 2026-08-15T23:13:57Z
authors: Suyash Maniyar, Armaan Sandhu, Abhishek Mishra
url: http://arxiv.org/abs/2608.15445v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Reward Hacking and Reasoning-Answer Decoupling Under Position-Confounded Optimization

## Abstract
When a reward is correct on every training example yet consistent with more than one goal, a model can acquire an unintended one, a failure known as goal misgeneralization. Endpoint accuracy on the training distribution cannot tell the two apart, because solving the task and exploiting a surface feature can satisfy the reward equally well. We treat this as a measurement problem: what does a benchmark score measure once a model has been optimized against a correct but confounded signal? We train language models with GRPO on multiple-choice math problems where the correct answer is always option A, then evaluate on an unseen test set with unbiased answer positions. Across Qwen2.5, Llama 3.x and Gemma-3 models, biased training often drives option-A rates above 0.90 in smaller models and collapses unbiased accuracy toward chance, so accuracy stops measuring math ability and instead measures an answer-position policy. We further find reasoning-answer decoupling: capable models generate reasoning that reaches the correct numeric answer while still selecting A. We track this with numeric extraction and an LLM judge (GPT-4.1-mini; Qwen2.5-3B decoupling rate is about 0.66). The broken construct generalizes beyond the training domain: biased models inflate A-rates on out-of-domain MMLU and value-laden prompts. Continued training on unbiased data reverses the in-domain shift unevenly and only partially reverses the out-of-domain one, so a model can appear restored on its training distribution while remaining biased on unseen inputs. Reasoning-answer decoupling rate, together with answer distributions and out-of-domain behavior, separates capability loss from a learned, transferable shortcut.

## Metadata
- **Published**: 2026-08-15T23:13:57Z
- **Authors**: Suyash Maniyar, Armaan Sandhu, Abhishek Mishra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15445v1)