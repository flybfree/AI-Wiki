---
title: Do LLM Recommenders Know When They're Hallucinating? Auditing Confidence Calibration in Catalog Faithfulness
url: http://arxiv.org/abs/2608.10008v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-07_21-41-16Z_DoLLMRecommendersKnowWhenThey_reHallucinating_Audi.md
generated_at: 2026-08-11 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper evaluates four zero-shot LLM recommenders across twelve catalog-item popularity cells to see if they hallucinate titles and how their confidence scores reflect that. It finds that hallucination rates vary from near zero on MovieLens to up to 8.4% on Yelp, while the models’ self‑reported confidence is systematically too low even when no hallucinations occur. The authors also show that a conformal abstention threshold can only modestly cut hallucinations at the expense of removing many correct recommendations.

## Key Takeaways
- Hallucination rates are catalog dependent ranging from 0% to 8.4%, and they are not uniformly high across all vendors or datasets.
- Verbalized confidence is miscalibrated even when OOD is zero, with ECE up to 0.223 on MovieLens despite perfect recall.
- The under‑confident channel creates an elicitation mismatch; conformal thresholds mainly eliminate correct items rather than distinguishing hallucinations.

## Context
LLM recommenders are widely used in recommendation systems but most audits focus only on out‑of‑domain rates, ignoring model confidence. This gap leaves practitioners unaware that a model may be over‑confident about wrong answers or under‑confident when it is right. The study highlights the need for calibration metrics alongside OOD to guide safe deployment.

## Implications
For researchers, audits must include both hallucination and confidence calibration to avoid misleading safety assessments. For industry, deploying conformal thresholds requires trade‑off awareness between reducing false positives and losing correct recommendations. Practitioners should adopt catalog‑anchored prompts rather than generic confidence questions to obtain reliable signals.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10008v1)
