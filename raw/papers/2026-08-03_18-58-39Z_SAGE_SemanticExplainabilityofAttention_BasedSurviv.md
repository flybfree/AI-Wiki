---
title: SAGE: Semantic Explainability of Attention-Based Survival Models in Computational Pathology
published: 2026-08-03T18:58:39Z
authors: Abdallah Lamane, Abdul Rahman Diab, Ren-Chin Wu, William Lotter
url: http://arxiv.org/abs/2608.02803v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGE: Semantic Explainability of Attention-Based Survival Models in Computational Pathology

## Abstract
Attention-based multiple instance learning (ABMIL) is the predominant approach for slide-level prediction in computational pathology, yet its attention maps provide only local explanations: they indicate where a model focuses but not which histological features drive its predictions or how the model behaves across a patient cohort. We present Semantic Attention Global Explanations (SAGE), a post-hoc framework that extracts global, language-grounded explanations from a frozen ABMIL model. Using a pathology vision-language model, SAGE scores image patches against a dictionary of 25 histological concepts, aggregates these scores according to the model's learned attention, and quantifies how each concept relates to prediction risk across a cohort. Applied to survival prediction using seven TCGA cancer cohorts and three foundation models, SAGE recovered established prognostic features, such as the adverse association of necrosis, while revealing cancer-specific biology, including a favorable angiogenic signature in renal cell carcinoma consistent with known molecular subtypes. Ablation studies demonstrated that these associations depend on the model's learned attention rather than concept prevalence alone, and that the concept dictionary captures much of the prognostic information encoded by the foundation model features. Through semantically-grounded explanations, SAGE provides a scalable, model-agnostic framework for understanding what ABMIL survival models learn, enabling pathologists to interpret model behavior at the cohort level and offering the potential for biomarker identification.

## Metadata
- **Published**: 2026-08-03T18:58:39Z
- **Authors**: Abdallah Lamane, Abdul Rahman Diab, Ren-Chin Wu, William Lotter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02803v1)