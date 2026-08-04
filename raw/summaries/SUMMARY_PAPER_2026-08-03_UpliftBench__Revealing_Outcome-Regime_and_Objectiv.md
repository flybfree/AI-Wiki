---
title: UpliftBench: Revealing Outcome-Regime and Objective Mismatch in Uplift Evaluation
url: http://arxiv.org/abs/2608.00915v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_00-51-44Z_UpliftBench_RevealingOutcome_RegimeandObjectiveMis.md
generated_at: 2026-08-03 23:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces UpliftBench, a benchmark that evaluates uplift estimators under an outer-test-isolated multi-objective protocol across seven dataset families, revealing that metric disagreement—not model differences—explains why published benchmarks conflict. It finds that F1 correlates weakly with effect accuracy on the IHDP benchmark while AUUC aligns better, and that ranking metrics fail to capture sign-threshold policy risk in Jobs, with Qini selection incurring higher regret than random selection.

## Key Takeaways
- On the standard continuous benchmark IHDP, Qini’s mean rank correlation with effect accuracy is +0.07 (95% CI [-0.03, +0.16]), indicating negligible alignment across 100 realizations.
- AUUC consistently outperforms Qini in alignment, with a paired prefix‑mean gap of +0.49 and the shipped cumulative‑gain AUUC achieving +0.73 correlation.
- In the Jobs case study, sign‑threshold selection yields lower benchmark regret than random model selection, but Qini, AUUC, and uplift‑at‑k incur 14–15% higher regret; threshold calibration reduces this by 81%.

## Context
Uplift modeling is central to personalized marketing and healthcare interventions, yet existing benchmarks often compare models using disparate metrics, leading to misleading conclusions. This work clarifies that metric choice drives observed performance gaps rather than intrinsic model quality.

## Implications
Practitioners should prioritize AUUC or calibrated thresholds over Qini for continuous uplift tasks, and recognize that ranking‑only metrics are unsuitable for sign‑threshold policies in discrete settings. The reproducible UpliftBench protocol encourages transparent benchmarking across diverse real‑world datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00915v1)
