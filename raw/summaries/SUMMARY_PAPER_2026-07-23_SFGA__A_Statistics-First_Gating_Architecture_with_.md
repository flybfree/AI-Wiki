---
title: SFGA: A Statistics-First Gating Architecture with Adjudicative Escalation for Trustworthy SFT Data Procurement
url: http://arxiv.org/abs/2607.18960v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_10-52-04Z_SFGA_AStatistics_FirstGatingArchitecturewithAdjudi.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SFGA, a statistics‑first gating architecture that decides whether to purchase supervised fine‑tuning data by evaluating three quality dimensions — diversity, utility, and redundancy — using cheap blind measurements with confidence intervals. A gate only accepts a dataset when all estimates are tight, sample sizes are sufficient, and the axes align; otherwise it triggers an adjudicative debate between advocates and rejectors. On a controlled benchmark of 12 datasets, SFGA achieves 0.90 accuracy and 0.83 F1 at a cost of $0.017 per unit, outperforming baseline methods while staying below the always‑escalate cost.

## Key Takeaways
- The architecture treats procurement as a cost‑aware routing problem across diversity, utility, and redundancy with confidence intervals to gauge reliability.
- Decision acceptance is contingent on tight measurement intervals, adequate sample sizes, and agreement among axes; otherwise escalation occurs.
- Benchmark results show high accuracy (0.90) and F1 (0.83) at a low per‑unit cost ($0.017), beating the always‑verify baseline while staying under the always‑escalate limit.

## Context
AI research increasingly relies on large supervised fine‑tuning datasets, yet acquiring them involves trade‑offs between quality dimensions and financial constraints. Traditional approaches either verify every candidate (high cost) or rely on opaque LLM judgments (risk of bias). SFGA bridges this gap by grounding decisions in statistical evidence and structured debate.

## Implications
For practitioners, SFGA offers a transparent, low‑cost framework to evaluate data provenance before training, reducing wasteful purchases. The adjudicative escalation mechanism also uncovers hidden biases that naive models may conceal, improving overall model reliability and trustworthiness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18960v1)
