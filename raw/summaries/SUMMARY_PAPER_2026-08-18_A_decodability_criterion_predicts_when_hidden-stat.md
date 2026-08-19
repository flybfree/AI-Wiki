---
title: A decodability criterion predicts when hidden-state selection beats majority voting in large language models
url: http://arxiv.org/abs/2608.17124v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_21-02-10Z_Adecodabilitycriterionpredictswhenhidden_statesele.md
generated_at: 2026-08-18 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CASE (Correctness‑Axis SElection) and a decodability criterion that predicts when hidden‑state selection outperforms majority voting in large language models. Experiments show the criterion correlates strongly with actual gains, with a Pearson correlation of 0.75 on held‑out data, and it improves performance by up to 19 points on medium‑difficulty questions.

## Key Takeaways
- Decodability is defined as a leakage‑free measure that ranks correct candidates above incorrect ones, providing a reliable predictor of selection versus voting accuracy.  
- A conventional probe appears accurate only because of question‑identity leakage; its performance disappears when questions are grouped together.  
- CASE delivers up to 19 point gains on medium‑difficulty tasks and 16.8 points on hard tasks across general and medical LLMs.

## Context
Test‑time information fusion in LLMs often relies on majority voting, which can be unreliable when sampled answers share correlated errors. Selecting the best answer by reading a correctness signal from hidden states offers an alternative, but its effectiveness varies without a clear metric. This work supplies such a metric to guide model developers and practitioners.

## Implications
The decodability criterion is practical because it can be measured in advance for any given model and task, enabling informed decisions between selection and voting strategies. Its transferability across domains suggests that the approach could improve robustness of AI systems without requiring large retraining efforts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17124v1)
