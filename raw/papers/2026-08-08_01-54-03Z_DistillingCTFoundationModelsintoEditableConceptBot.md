---
title: Distilling CT Foundation Models into Editable Concept Bottlenecks for Lung Nodule Malignancy Prediction
published: 2026-08-08T01:54:03Z
authors: Fakrul Islam Tushar, Stephen Adamo, Geoffrey D. Rubin
url: http://arxiv.org/abs/2608.07857v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distilling CT Foundation Models into Editable Concept Bottlenecks for Lung Nodule Malignancy Prediction

## Abstract
Foundation models provide transferable CT representations, but predictions based directly on these embeddings are difficult to interpret. We developed concept bottleneck models that map two frozen CT foundation-model representations to eight radiologist-defined pulmonary-nodule attributes and predict malignancy from the estimated concepts and nodule size. The models included CT-FM, a whole-CT self-supervised encoder using a 96^3-voxel nodule-centered patch, and FMCIB, a nodule-focused contrastive encoder using a 50-mm crop. Eight ridge-regression concept heads were trained on 2,610 LIDC-IDRI nodules. Malignancy models were trained on LUNA25 and evaluated on a held-out internal test set and the external DLCS cohort. Concept fidelity was assessed using five-fold cross-validated R^2, and malignancy discrimination was assessed using AUROC with 95% confidence intervals estimated by patient-grouped bootstrap resampling. Concept fidelity was modest but higher for FMCIB than CT-FM for subtlety (R2, 0.24 vs. 0.11), spiculation (0.17 vs. 0.08), texture (0.17 vs. 0.07), and lobulation (0.15 vs. 0.05). Internally, the CT-FM and FMCIB concept+size models achieved AUROCs of 0.86 (95% CI, 0.80-0.92) and 0.86 (0.79-0.92), respectively. Externally, AUROCs were 0.72 (0.68-0.75) and 0.73 (0.70-0.76), compared with 0.73 for nodule size alone and 0.60 and 0.67 for the corresponding embedding only probes. Additive predictions could be decomposed into feature-level contributions and modified through controlled concept interventions. Concept bottlenecks provided transparent malignancy predictions with discrimination similar to nodule size alone, while differences in concept fidelity suggest that concept recovery depends on the underlying foundation-model representation.

## Metadata
- **Published**: 2026-08-08T01:54:03Z
- **Authors**: Fakrul Islam Tushar, Stephen Adamo, Geoffrey D. Rubin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07857v1)