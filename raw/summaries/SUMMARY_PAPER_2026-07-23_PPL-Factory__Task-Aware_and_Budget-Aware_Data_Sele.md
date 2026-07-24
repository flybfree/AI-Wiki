---
title: PPL-Factory: Task-Aware and Budget-Aware Data Selection from Language Modeling to Reasoning
url: http://arxiv.org/abs/2607.18199v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_17-38-38Z_PPL_Factory_Task_AwareandBudget_AwareDataSelection.md
generated_at: 2026-07-23 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PPL-Factory, a task‑aware and budget‑aware data selection method that uses perplexity scores to pick informative training samples for fine‑tuning large language models. Experiments on GSM8K show it can achieve comparable or better performance with only 1 % of the data, exceeding full‑data fine‑tuning by up to 4.8 points on MATH.

## Key Takeaways
- PPL-Factory combines task‑specific perplexity scores with a budget constraint, allowing selection of just a few percent of training examples while preserving performance.
- The method outperforms existing heuristics such as data quality or diversity measures, which are often fixed and not adaptable to different tasks.
- On GSM8K, using 10 % of the data yields an accuracy gain of 0.9 over full‑data fine‑tuning, and on MATH it gains 4.8 points.

## Context
Efficient fine‑tuning is critical as training large models consumes significant compute resources. Prior approaches often treat all tasks uniformly or rely on static heuristics that ignore the learning objectives of downstream tasks. This work addresses those limitations by making selection both task‑aware and budget‑constrained.

## Implications
Practitioners can reduce fine‑tuning costs without sacrificing performance, especially in resource‑limited settings such as cloud services or edge devices. The framework’s simplicity makes it easy to integrate into existing pipelines, encouraging wider adoption of data‑efficient training strategies across the AI community.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18199v1)
