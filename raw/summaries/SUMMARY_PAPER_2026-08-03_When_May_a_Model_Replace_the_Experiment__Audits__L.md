---
title: When May a Model Replace the Experiment? Audits, Licenses, and the Price of Trust in Surrogate-Driven Design
url: http://arxiv.org/abs/2608.01378v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_16-59-29Z_WhenMayaModelReplacetheExperiment_Audits_Licenses_.md
generated_at: 2026-08-03 23:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates when machine‑learning surrogates can be trusted to replace costly experiments in design research and shows that such substitution is only safe under specific conditions. It proves that a surrogate may act as an oracle for ranking but cannot guarantee accuracy, and that trust must be bought through audits that are optimal in query complexity.

## Key Takeaways
- Predictive accuracy does not justify replacing experiments because near‑perfect R² can still lead to worst possible selections, introducing a quantifiable selection tax with provable upper and lower bounds.
- Safety is enforced by an architectural rule: predictions may be used freely but every certified conclusion must rest on true evaluations, which is both sufficient and necessary to avoid deterministic self‑confirmation failures.
- Audited surrogates reduce the cost of certified oracle evaluations by a factor of 25 while maintaining high Spearman rank correlation (0.80–0.99) between surrogate predictions and deployed search performance.

## Context
In fields such as chemistry, materials science, and machine learning, experimental evaluation is expensive and time‑consuming. Surrogates are used to propose candidates and even grade them, creating a feedback loop that blurs the line between prediction and measurement. This paper addresses the theoretical safety of that loop by providing clear criteria for when it can be trusted.

## Implications
For researchers, the result means they can safely adopt surrogates only after rigorous audits, avoiding costly mistakes in design optimization. For industry, it offers a pathway to reduce experimental budgets while maintaining high‑quality outcomes, but requires disciplined verification processes rather than reliance on model confidence alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01378v1)
