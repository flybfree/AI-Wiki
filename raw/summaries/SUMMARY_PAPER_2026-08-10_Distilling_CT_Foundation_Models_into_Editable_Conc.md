---
title: Distilling CT Foundation Models into Editable Concept Bottlenecks for Lung Nodule Malignancy Prediction
url: http://arxiv.org/abs/2608.07857v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_01-54-03Z_DistillingCTFoundationModelsintoEditableConceptBot.md
generated_at: 2026-08-10 22:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces concept bottleneck models that translate frozen CT foundation‑model embeddings into eight radiologist‑defined pulmonary‑nodule attributes to predict malignancy. By training ridge‑regression heads on LIDC‑IDRI nodules and evaluating both internal and external cohorts, the authors show that these interpretable concepts achieve AUROC comparable to nodule size alone while offering transparent predictions.

## Key Takeaways
- Concept fidelity is modest but higher for FMCIB than CT-FM across subtlety, spiculation, texture, and lobulation (R² values 0.24 vs 0.11 etc.), indicating that concept recovery depends on the underlying foundation‑model representation.
- The additive nature of concept+size predictions allows controlled interventions to modify malignancy risk by altering specific concepts while keeping size constant.
- Internally, both models reach AUROC ≈ 0.86 (95% CI 0.79–0.92), and externally they outperform nodule‑size only probes (AUROC ≈ 0.73) with confidence intervals of 0.68–0.75.

## Context
Foundation models provide high‑level, transferable representations for medical imaging but are often black‑boxed, limiting clinical interpretability. This work bridges that gap by distilling those embeddings into human‑readable concepts, a strategy aligned with the broader trend of explainable AI in radiology.

## Implications
Clinicians can use concept bottlenecks to gain insight into why a nodule is predicted as malignant or benign, supporting informed decision‑making. The approach also offers a scalable pathway for integrating foundational representations into diagnostic tools without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07857v1)
