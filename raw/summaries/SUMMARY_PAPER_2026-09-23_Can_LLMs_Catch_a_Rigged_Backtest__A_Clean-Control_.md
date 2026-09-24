---
title: Can LLMs Catch a Rigged Backtest? A Clean-Control Calibration Benchmark
url: http://arxiv.org/abs/2609.28090v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_13-25-25Z_CanLLMsCatchaRiggedBacktest_AClean_ControlCalibrat.md
generated_at: 2026-09-23 22:12
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper introduces a specialized benchmark designed to evaluate whether Large Language Models (LLMs) can accurately identify flaws in financial backtests without generating excessive false positives. The research demonstrates that while current models achieve high recall for identifying flawed code, they frequently struggle with specificity, often flagging "clean" control strategies as flawed unless specific "clean-aware" constraints are applied.

## Key Takeaways
- The researchers developed a 96-item paired benchmark where every flawed backtest is matched with a clean control that keeps the code style, dates, and reporting scaffold identical while changing only one methodology detail to isolate the model's ability to detect specific flaws.
- Evaluation of four different text endpoints revealed that while the primary DeepSeek auditor achieved 100% closed and clean-aware code recall, it simultaneously over-flagged 93.8% of clean code controls when using open prompts, indicating a significant lack of specificity in standard configurations.
- The study found that implementing a "clean-aware" warning significantly improves reliability by dropping the DeepSeek model's false positive rate from 20.8% to 0.0% without sacrificing recall, highlighting that proper prompt calibration is essential for reliable automated auditing.

## Context
As LLMs are increasingly integrated into quantitative finance and data science workflows, the ability to perform objective code audits becomes critical for risk management. This paper matters because it moves beyond general reasoning capabilities to test a specific, high-stakes task: distinguishing between subtle methodological errors and valid strategies in complex programming environments.

## Implications
For practitioners and developers, these findings suggest that simply scaling model size may not be sufficient to produce reliable automated auditors; instead, specific calibration techniques like "clean-aware" constraints are necessary to minimize false positives. This research provides a framework for building more trustworthy AI tools where the goal is not just to find errors, but to do so with high precision and minimal hallucination in professional environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.28090v1)
