---
title: From Financial Sentiment Classification to Return Predictability: A QLoRA Benchmark of Large Language Models
url: http://arxiv.org/abs/2608.04200v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_19-57-40Z_FromFinancialSentimentClassificationtoReturnPredic.md
generated_at: 2026-08-05 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a benchmark that separates language model performance on financial sentiment classification from its ability to generate economically meaningful return signals. It compares several models including QLoRA‑adapted Qwen2.5, LLaMA3, Mistral and shows that while some achieve high classification accuracy, none produce statistically significant predictive power for stock returns.

## Key Takeaways
- Mistral‑7B reaches the highest test accuracy (0.8840) and macro‑F1 (0.8771), demonstrating strong linguistic performance on the unified three‑class benchmark.
- QLoRA improves Qwen2.5’s macro‑F1 from 0.7274 to 0.8615, showing that fine‑tuning with QLoRA can close the gap between raw models and state‑of‑the‑art classifiers.
- Despite high classification scores, all models produce only small positive rank information coefficients (max 0.0143) for one‑day returns, indicating a clear gap between classification accuracy and tradable cross‑sectional signals.

## Context
Financial sentiment analysis is a cornerstone of quantitative finance where natural language processing models are used to derive trading ideas. This study adds a rigorous benchmark that evaluates both linguistic competence and economic relevance, addressing a longstanding challenge in the field.

## Implications
For practitioners, the results suggest that fine‑tuning techniques like QLoRA can boost sentiment classification but do not automatically translate into profitable strategies. The gap between model performance on benchmarks and real‑world returns underscores the need for domain‑specific validation beyond accuracy metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04200v1)
