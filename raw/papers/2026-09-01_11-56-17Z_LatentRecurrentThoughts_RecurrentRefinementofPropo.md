---
title: Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs
published: 2026-09-01T11:56:17Z
authors: Zhaoliang Chen, Jie Fu
url: http://arxiv.org/abs/2609.01117v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs

## Abstract
Chain-of-thought reasoning unfolds in discrete token space: each step is committed as text, errors propagate, and eliciting good traces presupposes traces to imitate. Reasoning instead in a model's continuous representation space - where intermediate states are vectors rather than words - sidesteps these constraints, but leaves open how those latent states should be computed. We approach this along two axes. First, we keep a large language model (LLM) frozen and use it for what it is already good at - modeling and decoding sequences - while a small auxiliary network supplies continuous latent thoughts as input. Second, we produce those latents by recurrence: a tiny recurrent reasoner refines them over many steps, decoupling the depth of computation from the size of the model, so that the latents are a product of iterative processing rather than a single forward pass. We instantiate this as Latent Recurrent Thoughts (LRT): a task-dedicated proposer supplies base latents, a recurrent reasoner refines them through bounded residual corrections, and the frozen LLM decodes the answer. On symbolic reasoning with answer supervision but no reasoning traces (Countdown-4, Sudoku) and on natural-language reasoning (HumanEval, MBPP, StrategyQA), LRT substantially outperforms prior frozen-decoder continuous-space reasoning methods under an identical decoder, prompt, data, and training budget, and outperforms non-thinking-mode chain-of-thought prompting on the same backbone at a small fraction of its inference compute.

## Metadata
- **Published**: 2026-09-01T11:56:17Z
- **Authors**: Zhaoliang Chen, Jie Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01117v1)