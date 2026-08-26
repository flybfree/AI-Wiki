---
title: A Formal Methodological Framework for Auditing Robustness and Fidelity in Explainable AI: From Application to Trust Certification
published: 2026-08-24T20:54:04Z
authors: Rosa Elysabeth Ralinirina, Jean Christian Ralaivao, Niaiko Michaël Ralaivao, Alain Josué Ratovondrahona, Thomas Mahatody
url: http://arxiv.org/abs/2608.23817v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Formal Methodological Framework for Auditing Robustness and Fidelity in Explainable AI: From Application to Trust Certification

## Abstract
SHAP and LIME are now standard tools for interpreting black-box predictions, yet their outputs can vary substantially when the input is perturbed by small amounts of noise--a problem we observed firsthand in our previous work on food security in Madagascar (Ralinirina et al., 2025). This variability raises the question of whether such explanations can be trusted at all. We address it by constructing an auditing protocol that measures two properties of any post-hoc explainer: robustness (how stable the explanation is under input perturbation) and fidelity (whether the features deemed important actually drive the model's prediction). These two quantities are combined into a single Trust Score. We run the protocol on a multi-sectoral dataset from Madagascar (83 features, 253 records, 4 malnutrition classes) using three classifiers and two explainers, plus their regularized counterparts. The results are sobering: models with AUC above 0.99 can produce numerically degenerate or flatly uninformative explanations, and fidelity scores lose discriminative power when the model is overfitted. These findings suggest that auditing XAI outputs is not optional but necessary, particularly when they inform decisions in sensitive domains.

## Metadata
- **Published**: 2026-08-24T20:54:04Z
- **Authors**: Rosa Elysabeth Ralinirina, Jean Christian Ralaivao, Niaiko Michaël Ralaivao, Alain Josué Ratovondrahona, Thomas Mahatody
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23817v1)