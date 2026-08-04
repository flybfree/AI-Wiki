---
title: Crushing the Evidence: A Dual-Penalty Evasion Framework for Fooling White-Box Explainable AI Auditors
published: 2026-08-01T10:03:14Z
authors: Niraj Kumar, Harsh Kasyap
url: http://arxiv.org/abs/2608.00566v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Crushing the Evidence: A Dual-Penalty Evasion Framework for Fooling White-Box Explainable AI Auditors

## Abstract
Post-hoc model explainers such as LIME, SHAP, and Integrated Gradients are widely deployed to audit models in high-stakes sensitive domains, including finance, healthcare, and social welfare. This ensures the model's transparency and acceptability. However, a few studies have examined potential attacks in the explainability pipeline. Adversaries can attempt to conceal algorithmic biases or backdoors using adversarial explanation attacks. These attacks have relied on scaffolding out-of-distribution (OOD) detectors that toggle predictions when queried by an explainer. Consequently, defenses have been developed to successfully neutralize these black-box attacks by identifying their anomalous perturbation footprints. In this paper, we demonstrate a critical vulnerability by introducing a more potent white-box, gradient-regularized evasion attack framework. By employing a continuous-embedding dual-penalty framework, we directly penalize trigger feature gradients during training on in-distribution data. Since our approach embeds the evasion logic natively into the model parameters, without relying on OOD scaffolding wrappers, it generates smooth, in-distribution predictions that leave no anomaly footprint. Empirical evaluations across four benchmark tabular datasets (COMPAS, German Credit, IEEE-CIS, and Communities & Crime) confirm that our method systematically crushes target feature attribution to near-zero (<0.02), maintains >90% Attack Success Rates, and fundamentally bypasses Conditional Anomaly Detection.

## Metadata
- **Published**: 2026-08-01T10:03:14Z
- **Authors**: Niraj Kumar, Harsh Kasyap
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00566v1)