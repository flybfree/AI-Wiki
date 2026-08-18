---
title: Learning Auditable Classifier Models: Source-Disjoint Tree Ensembles
published: 2026-08-16T12:56:49Z
authors: Srikumar Krishnamoorthy
url: http://arxiv.org/abs/2608.15725v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Auditable Classifier Models: Source-Disjoint Tree Ensembles

## Abstract
Predictive models in clinical and regulated settings must be accurate and fully auditable. Tree ensembles deliver strong accuracy on tabular data, but their sequential boosting couples structure discovery with coefficient estimation, making compact per-prediction auditing difficult. Interpretable alternatives impose structural constraints that limit expressiveness: generalized additive models typically restrict interactions to pairwise terms and post-hoc rule extractors produce overlapping rules that hinder compact interpretation. We introduce Residual Pattern Tree Ensemble (RPTE), a three-stage learning approach, that is built on three key principles: bounded feature budget, source disjointness, and separate coefficient estimation. Stage~1 builds a supervised symbolic feature vocabulary. Stage~2 grows shallow trees under a source-disjointness constraint, where each raw variable is allocated to at most one tree, and retains only the discovered tree structures. Stage~3 solves a single $\ell_1$-regularized logistic regression over leaf-region indicators, yielding jointly optimal sparse coefficients. This learning approach ensures that every prediction decomposes into an algebraic sum of named, non-overlapping rule contributions, enabling full auditability by design. Empirical evaluation on twelve clinical-domain binary classification benchmarks using repeated stratified 5-fold cross-validation shows that RPTE performs competitively against tuned opaque ensembles and interpretable baselines. RPTE reduces model inspection units by 9$\times$ to 87$\times$ relative to XGBoost and maintains lower audit complexity than EBM on all 12 datasets. RuleFit requires comparable or fewer inspection units on three datasets where its rule count is small, but without source-disjointness guarantees. The source code is available at \href{https://github.com/srikumar2050/hugiml-core}{this https URL}.

## Metadata
- **Published**: 2026-08-16T12:56:49Z
- **Authors**: Srikumar Krishnamoorthy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15725v1)