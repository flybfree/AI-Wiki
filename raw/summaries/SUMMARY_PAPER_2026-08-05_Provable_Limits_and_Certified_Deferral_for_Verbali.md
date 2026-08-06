---
title: Provable Limits and Certified Deferral for Verbalized Uncertainty in Small Language Models
url: http://arxiv.org/abs/2608.05064v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_17-11-04Z_ProvableLimitsandCertifiedDeferralforVerbalizedUnc.md
generated_at: 2026-08-05 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether small open-weight language models can safely defer to humans based on their verbalized confidence, using eleven instruction-tuned models ranging from 0.5B to 14B parameters evaluated on ARC-Challenge and TruthfulQA with 25,168 local predictions. It derives three theoretical limits for calibration: monotone calibration preserves risk coverage, temperature scaling fails when confidence exceeds one half while accuracy drops below it, and a Clopper-Pearson method yields finite-sample certificates under i.i.d. deployment. Empirically eight of twenty-two model-task pairs meet the temperature-scaling bound within one percent.

## Key Takeaways
- Monotone calibration maintains both risk-coverage frontier and error-detection AUROC across small models.
- Temperature scaling cannot be used when a model’s confidence stays above 0.5 while its accuracy falls below that threshold, limiting its usefulness for deferral decisions.
- A Clopper-Pearson procedure can turn a 200‑question calibration set into a finite‑sample risk certificate under the i.i.d. assumption.

## Context
The rise of small open-weight language models brings new deployment challenges where cost and privacy are paramount, prompting researchers to explore automated safety mechanisms such as confidence‑based deferral. This work contributes to that effort by formalizing how calibration affects risk metrics in these resource‑constrained settings.

## Implications
For practitioners deploying tiny models, the findings suggest that calibrated confidence is essential for reliable human fallback, while temperature scaling offers limited benefit unless strict accuracy thresholds are met. The ability to certify safety with a 20% risk budget informs responsible model integration into automated pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05064v1)
