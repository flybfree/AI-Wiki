---
title: Conditional-Independence-Regularized Distributional Autoencoders for Mixed-Type Data
published: 2026-08-20T20:52:46Z
authors: Siyuan Tang, Gongjun Xu, Ji Zhu
url: http://arxiv.org/abs/2608.20562v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conditional-Independence-Regularized Distributional Autoencoders for Mixed-Type Data

## Abstract
Mixed-type data containing both numerical and categorical variables arise in many scientific and real-world applications. Existing representation learning and generative modeling approaches typically focus either on reconstruction accuracy or unconditional data generation, but often fail to recover the full conditional distribution of the data while preserving interpretable structural relationships between heterogeneous variable types. In this work, we introduce Conditional-Independence-Regularized Distributional Autoencoders, a framework for learning low-dimensional representations of mixed-type data through conditional distribution matching and structural regularization. Our method combines an energy-score-based objective for numerical variables, a likelihood-based objective for categorical variables, and an auxiliary conditional independence regularization term encouraging the learned representation to capture the dependence between numerical and categorical components. We provide theoretical analysis showing that the optimal representation balances unexplained numerical variability, conditional entropy of categorical variables, and residual conditional dependence. Empirically, the proposed method achieves strong performance on both synthetic and real-world datasets, substantially improving categorical distribution recovery, achieving competitive overall conditional distribution recovery, and preserving mixed-type dependence structure. The code has been made available at GitHub.

## Metadata
- **Published**: 2026-08-20T20:52:46Z
- **Authors**: Siyuan Tang, Gongjun Xu, Ji Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20562v1)