---
title: Accurate Ensembles, Fragile Narratives: Multi-Scale Stacking and a Fidelity Audit of LLM-Generated Explanations for Credit Risk
url: http://arxiv.org/abs/2608.08126v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_13-22-14Z_AccurateEnsembles_FragileNarratives_Multi_ScaleSta.md
generated_at: 2026-08-11 13:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a system that combines a multi‑scale stacking ensemble of gradient‑boosting and neural models with an LLM to generate credit‑risk explanations, then audits the fidelity of those narratives. The ensemble achieves strong predictive performance (ROC‑AUC 0.9539) but only yields modest operational gains, while the narrative layer frequently misrepresents risk drivers, omits key factors, or invents irrelevant ones.

## Key Takeaways
- The ensemble’s ranking improvement is real yet small: it avoids six additional missed defaults out of 1,422 applicants, reducing cost‑weighted loss by under 2%, indicating limited practical benefit.  
- Attribution alignment fails despite SHAP and LIME overlap at 0.80; the order of importance is uncertain (tau = 0.43, p = 0.18) and attribution signs are near random for the most sensitive input (modal‑sign share 0.53).  
- Calibration and perturbation stability metrics fall short of thresholds (ECS = 0.117, DPD = 0.078), showing that constrained prompting alone does not guarantee reliable explanations.

## Context
Explainable AI for credit scoring is a growing concern as regulators demand transparent risk assessments. Current approaches often rely on post‑hoc attribution methods that may mislead stakeholders, and integrating LLMs introduces new failure modes such as hallucinations or contradictory narratives. This work highlights the gap between high predictive power and trustworthy explanations.

## Implications
For practitioners, the study suggests that ensemble models should be paired with rigorous validation of narrative outputs rather than assuming prompt‑driven explanations are sufficient. Industry adoption must incorporate verification steps to prevent misleading risk assessments and maintain regulatory compliance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08126v1)
