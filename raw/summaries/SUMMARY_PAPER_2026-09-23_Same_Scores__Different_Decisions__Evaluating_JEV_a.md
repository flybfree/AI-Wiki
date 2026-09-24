---
title: Same Scores, Different Decisions: Evaluating JEV and Language Models for Legal Document Understanding
url: http://arxiv.org/abs/2609.27678v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_10-53-01Z_SameScores_DifferentDecisions_EvaluatingJEVandLang.md
generated_at: 2026-09-23 21:09
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper evaluates the performance of Jev against nine different language models for legal document understanding, specifically focusing on contract inference tasks. The research highlights that aggregate accuracy metrics can be misleading because they often mask inconsistencies in individual decisions made by the model under varying request configurations.

## Key Takeaways
- Aggregate accuracy is an insufficient metric for evaluating AI reliability in legal contexts because a model may consistently return the wrong answer across multiple trials, which simple averages fail to highlight as a systematic error.
- The study utilized the ContractNLI dataset to compare Jev and other language models by analyzing inference cost, response time, and correctness across various conditions, such as hypothesis visibility and output order.
- While hosted language models generally achieved higher baseline accuracy than Jev, they exhibited significant variability in consistency; conversely, Jev demonstrated the lowest inference cost and median response time among the evaluated configurations.
- Development diagnostics revealed that model errors often include "compensating corrections" and regressions, meaning a change in how a prompt is structured can lead to different answers even when the underlying contract data remains identical.

## Context
This research addresses a critical gap in AI evaluation by moving beyond simple accuracy scores toward a more nuanced understanding of model stability in high-stakes domains like law. As Large Language Models (LLMs) are increasingly deployed for professional services, identifying how these models behave under varying input conditions is essential for ensuring reliability and safety.

## Implications
For practitioners and developers, these findings suggest that evaluating an AI model solely on its average accuracy score is insufficient for legal applications where consistency is paramount. Organizations should adopt a multi-dimensional evaluation framework that prioritizes the stability of individual judgments across different prompt configurations alongside traditional metrics like inference cost and response time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.27678v1)
