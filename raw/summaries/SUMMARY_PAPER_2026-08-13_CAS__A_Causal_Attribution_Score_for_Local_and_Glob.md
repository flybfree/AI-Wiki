---
title: CAS: A Causal Attribution Score for Local and Global Explainable Artificial Intelligence
url: http://arxiv.org/abs/2608.12555v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_19-49-01Z_CAS_ACausalAttributionScoreforLocalandGlobalExplai.md
generated_at: 2026-08-13 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAS, a causal attribution score designed to separate predictive explanations from true intervention effects on real-world outcomes. It demonstrates that CAS achieves lower mean local causal attribution error (MAE) than existing normalization approaches across simulated and empirical settings.

## Key Takeaways
- CAS reduces the mean Local CAS MAE to 0.107, compared with 0.173 for one-at-a-time normalisation and 0.213 for a global normalised absolute ATE vector.
- The advantage over one-at-a-time normalisation grows from -0.003 under additivity conditions to 0.091 when strong interactions are present, indicating superior handling of non‑additive effects.
- Empirical evaluations on two real‑world datasets show that Feature-CAS rankings diverge significantly from predictive SHAP/TreeSHAP rankings; for example, in Pennsylvania data dep1 moves from a global rank of 13 to a local Feature-CAS rank of 2.

## Context
This research fills a critical gap in AI interpretability by moving beyond mere prediction to explain how interventions alter outcomes. By integrating causal Shapley contributions into a unified scoring framework, CAS provides a more faithful representation of what truly drives changes, which is essential for trustworthy machine learning systems.

## Implications
Practitioners can use Feature-CAS to prioritize features that genuinely modify causal effects rather than those that merely correlate with the outcome, leading to better-informed decisions in regulated domains such as healthcare and finance. The method also supports regulatory compliance by clarifying the causal impact of each feature, reducing risk associated with opaque model behavior.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12555v1)
