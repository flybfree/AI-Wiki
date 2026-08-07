---
title: CohortHijack: Robustness of Single Cell Annotation to Companion Cell Removal
published: 2026-08-06T11:29:48Z
authors: Arash Vashagh, Yasmin Vashagh
url: http://arxiv.org/abs/2608.05900v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CohortHijack: Robustness of Single Cell Annotation to Companion Cell Removal

## Abstract
Many single-cell annotation tools refine an initial cell label using nearby cells or cluster-level voting. We study whether this refinement can be manipulated without changing the target cell. We introduce CohortHijack, a robustness audit that removes selected non-target cells from the query cohort while preserving the target expression profile, base prediction, and trained model. We evaluate random and structured removal methods, together with greedy, multi-start, and beam search, on PBMC3K and Paul15 using logistic regression and calibrated linear SVM classifiers. Structured removal was consistently stronger than random removal on Paul15. Multi-start search changed 24.33% of linear-SVM targets and 19.67% of logistic-regression targets while removing a small fraction of the cohort and keeping mean collateral changes below 0.4%. Ablations confirmed that the effect disappeared when neighborhood refinement was disabled. We also evaluated CellTypist majority voting, where independent predictions remained unchanged across all evaluations, but refined labels changed after small companion-cell removals. These findings identify query cohort composition as a target-preserving attack surface in single-cell annotation.

## Metadata
- **Published**: 2026-08-06T11:29:48Z
- **Authors**: Arash Vashagh, Yasmin Vashagh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05900v1)