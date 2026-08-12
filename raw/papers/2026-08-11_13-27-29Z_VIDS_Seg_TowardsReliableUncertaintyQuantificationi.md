---
title: VIDS-Seg: Towards Reliable Uncertainty Quantification in Pediatric Cardiac Ultrasound Segmentation
published: 2026-08-11T13:27:29Z
authors: Paul Fischer, Ece Ozkan
url: http://arxiv.org/abs/2608.10903v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VIDS-Seg: Towards Reliable Uncertainty Quantification in Pediatric Cardiac Ultrasound Segmentation

## Abstract
Reliable clinical deployment of machine learning requires models that know when they are likely to fail, particularly for subgroups underrepresented in training data. A common case is pediatric care, where models trained on adult cohorts can silently under-perform on children with no indication that something has gone wrong. As retraining with labeled pediatric data is often infeasible, detecting such failures at inference time is a critical clinical need. Building on the VIDS (Variational Inference under Distribution Shifts) framework, we introduce VIDS-Seg, which applies amortized variational inference over a lightweight prediction head to make this adaptive, OOD-aware prior tractable for dense image segmentation. We evaluate VIDS-Seg on left ventricular segmentation in echocardiography, a setting where pediatric anatomy differs systematically from the adult population most segmentation models are trained on, training on an adult cohort (EchoNet-Dynamic) and evaluating zero-shot on a pediatric cohort (EchoNet-Pediatric). Across all age strata, VIDS-Seg matches competitive baselines in segmentation accuracy while producing substantially higher spatial correspondence between predicted uncertainty and segmentation error, an advantage that persists even after applying temperature scaling to all baselines. Downstream, it yields more accurate and stable ejection fraction estimates and more reliable detection of cardiac malfunction in the infant subgroup. Our results indicate that OOD-aware uncertainty quantification can serve as a practical safety layer for deployed segmentation models, enabling detection of silent failures in underrepresented subgroups without retraining or additional labeled data.

## Metadata
- **Published**: 2026-08-11T13:27:29Z
- **Authors**: Paul Fischer, Ece Ozkan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10903v1)