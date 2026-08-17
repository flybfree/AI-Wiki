---
title: Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations
published: 2026-08-14T16:06:41Z
authors: Toby D. Pilditch
url: http://arxiv.org/abs/2608.14425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations

## Abstract
LLM evaluations often use fixed sampling budgets, testing every item the same number of times even after estimates are precise. We introduce optstop, a precision-based adaptive stopping framework that treats evaluation as a sequential measurement problem: keep sampling where uncertainty remains high, and stop where estimates are precise or stable enough. The framework builds on hierarchical Bayesian inference, supports binary, ordinal, and continuous outcomes, and keeps every benchmark item eligible for sampling, without requiring a calibrated item bank. It runs live or retrospectively, and includes a safeguard that samples more cautiously as measured performance approaches zero, where rare successes matter most. In an illustrative 200-item, 10-epoch evaluation, it removes 57%-97% of planned trials across nine validation settings, with overall conclusions equivalent to the full run. These results show that LLM evaluation compute can be allocated by uncertainty rather than by fixed repetition counts, with the magnitude of savings depending on evaluation design.

## Metadata
- **Published**: 2026-08-14T16:06:41Z
- **Authors**: Toby D. Pilditch
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14425v1)