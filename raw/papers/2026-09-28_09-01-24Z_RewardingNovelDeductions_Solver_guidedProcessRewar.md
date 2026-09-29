---
title: Rewarding Novel Deductions: Solver-guided Process Rewards for Logical Reasoning
published: 2026-09-28T09:01:24Z
authors: Muhammad Asif Ali, Wenqing Wang, Huan Wang, Mohammad Raza
url: http://arxiv.org/abs/2609.34660v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rewarding Novel Deductions: Solver-guided Process Rewards for Logical Reasoning

## Abstract
Logical reasoning remains a major challenge for large language models (LLMs), particularly on structured problems that require precise constraint tracking, consistency preservation, and multi-step deduction. This challenge is especially acute for small-scale LLMs, which are more prone to producing inconsistent, redundant, or brittle reasoning trajectories. Existing approaches for improving logical reasoning largely optimize for final-answer correctness, providing only weak supervision over the intermediate reasoning process. In this work, we propose SPRING: (Solver-guided Process Rewards for Novel LogIcal ReasoNing Step Generation). SPRING uses SMT solver as a training-time verifier of intermediate reasoning steps to provide process-level supervision. It introduces the notion of a novel reasoning step, namely, a step that is logically valid, consistent with the evolving reasoning state, and not already implied by previously accepted non-contradictory deductions. Based on this solver-based assessment, it designs process rewards that encourage novel inferential progress while penalizing contradictory and uninformative reasoning steps. Evaluation across three logical reasoning benchmarks, ZebraLogic, AR-LSAT, and Knights and Knaves, and four LLMs shows that SPRING consistently outperforms base LLMs, outcome-only reward baselines, and Logic-LM. On ZebraLogic, SPRING improves puzzle accuracy by up to 49.71 and 15.43 points over the base LLM and strongest outcome-only baseline, respectively. On AR-LSAT, it improves overall accuracy by up to 64.93 and 12.14 points, respectively. On Knights and Knaves, SPRING achieves up to 93.14 puzzle accuracy and 96.05 person accuracy.

## Metadata
- **Published**: 2026-09-28T09:01:24Z
- **Authors**: Muhammad Asif Ali, Wenqing Wang, Huan Wang, Mohammad Raza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34660v1)