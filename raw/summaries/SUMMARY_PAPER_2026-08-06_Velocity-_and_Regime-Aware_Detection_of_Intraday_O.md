---
title: Velocity- and Regime-Aware Detection of Intraday Options Market Manipulation, with Explainable Attribution
url: http://arxiv.org/abs/2608.05373v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_19-51-54Z_Velocity_andRegime_AwareDetectionofIntradayOptions.md
generated_at: 2026-08-06 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a minute‑level detection pipeline that identifies intraday options manipulation by focusing on the velocity of market state rather than its level, producing explainable alerts with SHAP attribution. On an Indian index‑options test it matches regulator‑identified days and achieves high precision when regimes are ignored, while regime conditioning reduces recall. The same dynamic signature is observed in thinly traded U.S. equities, confirming cross‑market transferability.

## Key Takeaways
- The detection relies on a smoothed velocity of option‑Delta for index options and price velocity for equities, flagging pump‑and‑crash patterns that are distinct from normal volatility.
- Regime‑aware classification improves precision but sacrifices recall, highlighting the trade‑off between using inferred market regimes versus treating unlabeled days as normal under the closed‑world assumption.
- Exact SHAP attribution aligns with regulator‑identified manipulation days (cosine similarity 0.99), indicating that unconfirmed alerts share the same underlying cause.

## Context
This work advances AI detection in financial markets by integrating explainable machine learning with regime analysis, moving beyond black‑box models to provide transparent evidence for regulators. It demonstrates how dynamic signatures can be learned and transferred across instruments, enriching the toolkit for real‑time anomaly spotting.

## Implications
For market participants, the pipeline offers a practical framework that balances recall and precision while delivering auditable explanations. Practitioners can leverage these alerts to monitor compliance and reduce false positives, fostering trust in automated surveillance systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05373v1)
