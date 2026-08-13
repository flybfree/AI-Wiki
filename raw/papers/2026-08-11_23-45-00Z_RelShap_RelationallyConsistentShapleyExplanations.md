---
title: RelShap: Relationally Consistent Shapley Explanations
published: 2026-08-11T23:45:00Z
authors: Seungeun Lee, Joao Fonseca, Julia Stoyanovich
url: http://arxiv.org/abs/2608.11508v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RelShap: Relationally Consistent Shapley Explanations

## Abstract
Machine learning pipelines commonly flatten relational data into single-table representations, discarding structural constraints. Widely used Shapley value-based feature attributions then rely on feature independence, evaluating the model on combinations that could never arise in the underlying data, producing misleading explanations. We propose RelShap, a framework that incorporates relational constraints and data provenance into Shapley value computation, restricting both background data and coalition evaluation to relationally valid configurations. The framework is estimator-agnostic and composes with Kernel SHAP, Monte Carlo, and Leverage SHAP without altering their sampling or weighting properties. Functional dependencies further induce equivalence classes over feature coalitions, which RelShap exploits to reduce runtime without changing Shapley values; we provide a combinatorial characterization of the expected speedup. Experiments across multiple datasets, models, and estimators show that RelShap produces explanations that are more faithful to the data-generating process, correctly identifying the dominant feature in controlled settings where existing methods, including Conditional SHAP and ManifoldShap, do not. Our code is available at: https://github.com/duneag2/relshap.

## Metadata
- **Published**: 2026-08-11T23:45:00Z
- **Authors**: Seungeun Lee, Joao Fonseca, Julia Stoyanovich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11508v1)