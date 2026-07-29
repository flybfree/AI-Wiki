---
title: Beyond Counts: A Distributional Robustness Margin For Pathology Foundation Models
published: 2026-07-28T09:34:30Z
authors: Clément Grisi, Jeroen van der Laak, Geert Litjens
url: http://arxiv.org/abs/2607.25497v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Counts: A Distributional Robustness Margin For Pathology Foundation Models

## Abstract
Pathology foundation models are approaching clinical deployment, yet remain vulnerable to systematic non-biological variation across centres. Differences in tissue preparation, staining and scanning are strongly encoded in their representations, enabling shortcut learning and weakening generalisation across cohorts and institutions. The Robustness Index (RI) quantifies whether local representation geometry is dominated by biology or by non-biological variation, but its count-based formulation discards distance information. We show that adding distance weights changes little because the deeper limitation lies in RI's pooled, fixed-neighbourhood design, which obscures sample-level heterogeneity and effectively evaluates only a model-dependent subset of samples. We introduce the Cross-confounder Robustness Margin (CRoMa), a sample-resolved measure that directly compares distances to cross-confounder biological matches and same-confounder biological distractors. CRoMa recasts robustness as a cohort-wide margin distribution rather than a single pooled score. We evaluated frozen representations from 20 tile-level encoders across three benchmarks and 4 slide-level encoders on a fourth. Rankings by median CRoMa were broadly consistent across datasets, while the underlying distributions revealed substantial within-model heterogeneity. Every tile encoder retained a confounder-dominated lower tail, whose prevalence and severity varied markedly across models. These distinct robustness profiles frame model selection as a Pareto trade-off between typical and lower-tail robustness. Higher CRoMa was also associated with smaller shortcut-induced performance drops after supervised adaptation. By turning representation geometry into a distributional robustness readout that anticipates downstream shortcut susceptibility, CRoMa provides a principled basis for robustness assessment and model selection.

## Metadata
- **Published**: 2026-07-28T09:34:30Z
- **Authors**: Clément Grisi, Jeroen van der Laak, Geert Litjens
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25497v1)