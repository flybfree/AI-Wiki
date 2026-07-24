---
title: When Does Machine Learning Beat Value Sorting? A Three-Dataset Diagnostic of Exposure-Weighted Shipment Prioritization
url: http://arxiv.org/abs/2607.18573v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_23-11-18Z_WhenDoesMachineLearningBeatValueSorting_AThree_Dat.md
generated_at: 2026-07-23 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates when machine‑learning models outperform simple value‑only sorting in selecting shipments for managerial review, using three real supply‑chain datasets. Across SCMS procurement, DataCo logistics, and Olist e‑commerce, the model that combines predicted delay severity with shipment value (M1) beats a baseline that only uses value but does not consistently beat pure value sorting. The study reports mixed performance gains across contexts.

## Key Takeaways
- M1 minus VALUE_ONLY yields -5.5 percentage points for SCMS, +10.1 pp for DataCo, and -4.9 pp for Olist at a 10% review budget.  
- Model performance is tied to learnability of severity: DataCo shows moderate R² (0.27) but slight calibration bias (+0.01 days), while SCMS and Olist have near‑zero or negative R² and negative calibration bias.  
- Nested‑CV cost‑sensitive retraining does not provide a stable improvement over M1, indicating that algorithmic tweaks are less effective than assessing model quality.

## Context
The work addresses a common AI deployment dilemma: whether complex models truly add value when resources for review are limited. By applying leakage‑controlled rolling‑origin evaluation and paired bootstrap confidence intervals, the authors create a rigorous diagnostic that can be replicated in other domains where prioritization matters more than overall accuracy.

## Implications
Practitioners should treat value sorting as a baseline benchmark and only deploy ML after confirming that severity prediction is learnable and well calibrated. This protocol helps avoid over‑fitting to noisy data and ensures decisions are grounded in reliable risk estimates rather than speculative model outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18573v1)
