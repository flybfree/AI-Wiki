---
title: Do Tabular Foundation Models Agree with Themselves?
url: http://arxiv.org/abs/2608.06004v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_13-09-54Z_DoTabularFoundationModelsAgreewithThemselves.md
generated_at: 2026-08-06 20:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether tabular foundation models (TFMs) produce joint distributions that satisfy two consistency conditions: marginalization consistency and factorization consistency. The authors find that all evaluated TFMs violate both requirements across classification and regression tasks on diverse datasets.

## Key Takeaways
- Marginalization consistency is violated because the model’s predicted marginals do not match the conditional predictions obtained by directly sampling target variables, indicating a mismatch between joint modeling and univariate inference.
- Factorization consistency is broken as different orders of factorizing features into factors yield distinct joint distributions, showing that TFMs are order‑dependent and thus non‑factorizable.
- The violations occur for both classification and regression tasks, suggesting that current TFM designs do not faithfully represent the true posterior predictive distribution.

## Context
Tabular foundation models aim to unify diverse tabular prediction problems under a single transformer architecture, offering scalable and flexible solutions. Their design relies on approximating Bayesian posteriors with pre‑trained language models, yet the paper reveals that this approximation lacks internal consistency across different factorization strategies.

## Implications
For practitioners, these findings caution against assuming TFMs automatically produce valid joint distributions without explicit checks. It may lead to overconfident predictions that are inconsistent with underlying data structures, prompting a need for additional validation protocols in model deployment and evaluation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06004v1)
