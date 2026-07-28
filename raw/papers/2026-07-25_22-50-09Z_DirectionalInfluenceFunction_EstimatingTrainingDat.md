---
title: Directional Influence Function: Estimating Training Data Influence in Constrained Learning
published: 2026-07-25T22:50:09Z
authors: Xin Wang, R. Tyrrell Rockafellar,  Xuegang,  Ban
url: http://arxiv.org/abs/2607.23388v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Directional Influence Function: Estimating Training Data Influence in Constrained Learning

## Abstract
As constrained learning becomes increasingly common, models are trained under explicit feasibility requirements to enforce fairness, safety, robustness, regulariza- tion, and physics or logic constraints. Understanding how training samples in- fluence the model solution (e.g., learned parameters) is crucial for interpretability and robustness. The classical influence function (IF) estimates sample contribu- tions via local sensitivity analysis, measuring how the solution changes when a specific training sample is perturbed or removed. However, IF becomes unreli- able in constrained settings: data perturbations can reshape both the objective and the feasible region, leading to estimates that violate feasibility. In response, we propose the Directional Influence Function (DIF), a novel estimator that explicitly incorporates these constraints into influence estimation. DIF formulates the opti- mality conditions of constrained learning as a variational inequality (VI) and ana- lyzes how perturbing training data affects this VI. We validate DIF on constrained linear regression and demonstrate that it recovers leave-one-out retraining results, whereas IF and penalty-based IF exhibit significant bias. We further apply DIF to fairness-constrained CNNs, where DIF accurately predicts test loss changes under data removal and aligns closely with actual retraining. Our results establish DIF as an efficient and reliable tool for data attribution in constrained learning.

## Metadata
- **Published**: 2026-07-25T22:50:09Z
- **Authors**: Xin Wang, R. Tyrrell Rockafellar,  Xuegang,  Ban
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23388v1)