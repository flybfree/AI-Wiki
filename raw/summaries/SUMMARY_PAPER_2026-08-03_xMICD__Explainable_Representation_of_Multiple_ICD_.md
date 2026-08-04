---
title: xMICD: Explainable Representation of Multiple ICD Codes
url: http://arxiv.org/abs/2608.00935v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_02-24-57Z_xMICD_ExplainableRepresentationofMultipleICDCodes.md
generated_at: 2026-08-03 23:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces xMICD, a method that creates low-dimensional patient representations from multiple ICD codes by combining clinically meaningful diagnostic groups with similarity in a pre-trained embedding space. Instead of binary group membership, it assigns codes to groups via similarity-based relative assignments, producing features that reflect how closely a patient’s diagnoses align with each clinical group. Experiments show xMICD matches predictive performance of embedding‑based models like ICD2Vec while remaining interpretable.

## Key Takeaways
- xMICD replaces binary group labels with similarity‑based relative assignments to diagnostic groups, yielding continuous features that capture alignment rather than mere membership.
- The method achieves predictive performance comparable to state‑of‑the‑art embedding representations such as ICD2Vec across various clinical prediction tasks.
- Each output dimension corresponds to a recognizable clinical group, preserving interpretability of the representation.

## Context
Current machine learning models for EHR risk prediction rely heavily on high‑dimensional embeddings that are hard for clinicians to understand. While these embeddings improve accuracy, they lack clinical insight and hinder adoption in real‑world settings where explainability is crucial.

## Implications
xMICD bridges the gap between performance and interpretability by embedding semantic similarity into a clinically meaningful space. Practitioners can use the resulting features to build models that are both accurate and understandable, supporting regulatory compliance and trust in AI‑driven clinical tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00935v1)
