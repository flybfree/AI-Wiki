---
title: Model-Agnostic FDR Control via Group Gaussian Mirror and Permutation SHAP
url: http://arxiv.org/abs/2608.00989v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_04-39-27Z_Model_AgnosticFDRControlviaGroupGaussianMirrorandP.md
generated_at: 2026-08-03 23:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a grouped-feature FDR control framework for sequential and grouped models. It constructs null-symmetric block-level mirror statistics with matrix perturbations for linear models and combines Permutation SHAP derivatives with kernel dependence measures for neural models, offering a model-agnostic approach that does not rely on covariate distribution assumptions.

## Key Takeaways
- The framework constructs null-symmetric block-level mirror statistics using matrix-valued perturbations to control false discovery rates in grouped linear models.
- It integrates Permutation SHAP derivatives with a kernel-based dependence measure to produce model-agnostic importance scores for sequential neural models.
- The method reduces to familiar Gaussian Mirror or Neural Gaussian Mirror when each group contains a single feature, preserving existing methods while extending to larger blocks.

## Context
Feature selection in deep learning often involves correlated sub‑features such as lags or attention interactions, making standard coordinate‑wise controls inadequate. Existing methods either ignore grouping or require explicit distributional assumptions, limiting their applicability across architectures.

## Implications
This approach enables reliable false discovery rate control without specifying covariate distributions, supporting more robust model interpretation and selection in high‑dimensional AI pipelines where grouped signals are common.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00989v1)
