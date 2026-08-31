---
title: Load-Bearing Context: The Question Damage Score for Evaluating Context Reliance in Linguistic Reasoning
url: http://arxiv.org/abs/2608.27756v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-27_22-36-49Z_Load_BearingContext_TheQuestionDamageScoreforEvalu.md
generated_at: 2026-08-30 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the Question Damage Score to evaluate how individual context examples support large language model answers in linguistics olympiad puzzles. By deleting either random or load‑bearing context, the authors show that frontier LLMs often continue producing correct answers after removing essential information, indicating limited reliance on provided context.

## Key Takeaways
- The Question Damage Score classifies puzzles as fragile when a single context example is critical for answering a question and robust otherwise.  
- Even when load‑bearing examples are removed, most LLMs rarely abstain and still generate answers that appear correct, suggesting they may rely on prior knowledge or memorization.  
- The framework enables fine‑grained causal analyses of context reliance beyond simple abstention, supporting targeted contamination studies.

## Context
Understanding whether models draw on supplied data versus external knowledge is crucial for building trustworthy AI systems. This study uses a controlled linguistic puzzle setting to isolate the impact of each context fragment, offering a method that can be applied to diverse reasoning tasks.

## Implications
For researchers, the Question Damage Score provides a diagnostic tool to pinpoint which inputs drive model outputs, guiding improvements in instruction following and memory management. Practitioners can use these insights to design better prompting strategies and reduce over‑reliance on memorized answers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27756v1)
