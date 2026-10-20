---
title: When Empathy Misses the Goal: A Benchmark for Goal Displacement in LLM Advice
published: 2026-10-18T20:35:11Z
authors: Dean Ariel, Guy Laban
url: http://arxiv.org/abs/2610.25522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Empathy Misses the Goal: A Benchmark for Goal Displacement in LLM Advice

## Abstract
Conversational large language models can respond with warmth and reassurance while failing to advance the user's stated goal. We conceptualize this failure as $\textbf{goal displacement}$, the substitution of persona-maintenance content for goal-relevant substance. To measure it, we introduce $\textbf{GDB}$ (Goal Displacement Benchmark), comprising 230 scenarios across nine domains and $4{,}134$ human-scored responses from 18 models. A $2 \times 2$ taxonomy crosses hard constraints with emotional distress, distinguishing failures to confront infeasible goals or combine empathy with practical guidance from reverse displacement, where unsolicited problem-solving replaces requested emotional support. A deletion-test rubric assesses whether substantive help remains after purely supportive sentences are removed. Independent raters achieve weighted $κ= 0.82$ against author scores for displacement severity. Trap displacement ranges from $0.0\%$ to $37.7\%$ and is strongly negatively correlated with Chatbot Arena Elo ($ρ= -0.706$, $n = 15$). Reverse displacement reaches $41.9\%$, including substantial rates in models with negligible trap displacement. A factorial probe supports a distinction from social sycophancy. Human-scored responses in the high-complexity, low-pressure condition exhibit $35.0\%$ sycophancy but $7.5\%$ displacement, with little association between the constructs. Matched OLMo-2 checkpoints show that mixed empathy-with-constraints displacement remains at $52.3\%$ after supervised fine-tuning and falls to $13.8\%$ after direct preference optimization. GDB provides a reproducible diagnostic of whether responses advance the operationalized user goal, supporting model comparison, post-training evaluation, and regression testing. We release the dataset, annotations, and rubric under CC-BY-4.0 and the evaluation code under MIT.

## Metadata
- **Published**: 2026-10-18T20:35:11Z
- **Authors**: Dean Ariel, Guy Laban
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25522v1)