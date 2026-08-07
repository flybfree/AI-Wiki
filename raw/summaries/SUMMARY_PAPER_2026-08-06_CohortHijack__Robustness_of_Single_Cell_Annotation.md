---
title: CohortHijack: Robustness of Single Cell Annotation to Companion Cell Removal
url: http://arxiv.org/abs/2608.05900v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_11-29-48Z_CohortHijack_RobustnessofSingleCellAnnotationtoCom.md
generated_at: 2026-08-06 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CohortHijack, a robustness audit that tests whether single‑cell annotation tools can be manipulated by removing non‑target cells without altering the target cell’s expression profile or model predictions. Experiments on PBMC3K and Paul15 with logistic regression and linear SVM classifiers show that structured removal consistently outperforms random removal, while multi‑start search alters many targets yet keeps collateral changes modest. Ablations confirm the effect depends on neighborhood refinement.

## Key Takeaways
- Structured removal of companion cells can systematically change annotation results even when the target cell’s expression remains unchanged.  
- Multi‑start beam search introduces a high proportion of altered linear‑SVM and logistic‑regression targets while limiting overall cohort impact to under 0.4% per run.  
- The robustness failure is tied specifically to neighborhood refinement mechanisms, which disappear when disabled.

## Context
Single‑cell annotation relies on local cell neighborhoods to refine labels, a technique common in AI pipelines that combine spatial data with classification models. This paper highlights a vulnerability: the same mechanism that improves accuracy can be exploited to produce misleading results without affecting the original target. Understanding this trade‑off is crucial for trustworthy machine learning systems.

## Implications
For researchers and practitioners, CohortHijack underscores the need for rigorous robustness testing of annotation tools in multi‑cell datasets. It suggests that future models should incorporate safeguards against neighbor‑based attacks to preserve label integrity across diverse biological contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05900v1)
