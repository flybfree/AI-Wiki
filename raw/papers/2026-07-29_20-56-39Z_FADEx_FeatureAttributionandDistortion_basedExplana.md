---
title: FADEx: Feature Attribution and Distortion-based Explanation of Dimensionality Reduction
published: 2026-07-29T20:56:39Z
authors: Lucas Greff Meneses, Evandro S. Ortigossa, Claudio Silva, Luis Gustavo Nonato
url: http://arxiv.org/abs/2607.27463v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FADEx: Feature Attribution and Distortion-based Explanation of Dimensionality Reduction

## Abstract
Dimensionality Reduction (DR) is a fundamental tool for high-dimensional data exploration, reducing the complexity of latent spaces of machine learning models, and assisting in the explanation of complex opaque models. However, non-linear DR techniques often function as opaque transformations themselves, making it challenging to understand how individual features influence instance positioning in the reduced space. This lack of transparency complicates the analysis and interpretation of structural patterns, hindering the ability to reason about the organization of high-dimensional data based on the projected layout. In order to address this challenge, dimensionality reduction explanation methods have shown promise in improving the understanding of the observed groups and cluster structures. Unfortunately, existing DR explanation approaches tend to suffer from limitations such as multiple attributions per feature and restricted applicability to specific dimensionality reduction methods, which hinder their use. In this work, we propose FADEx, a novel local per-instance feature attribution method that leverages local linear approximation via first-order Taylor expansion and Singular Value Decomposition to provide explanations. FADEx computes the local linear models via weighted least squares, eliminating the need for out-of-sample data mapping, making it agnostic to the DR method, while simultaneously providing local feature attributions and distortion analysis. Through qualitative and quantitative evaluations, comparisons with existing methods, and case studies, we demonstrate FADEx's effectiveness and versatility in providing explanations and analytical resources for analyzing the behavior of DR methods. The results indicate FADEx yields robust and reliable explanations, outperforming existing approaches in several aspects.

## Metadata
- **Published**: 2026-07-29T20:56:39Z
- **Authors**: Lucas Greff Meneses, Evandro S. Ortigossa, Claudio Silva, Luis Gustavo Nonato
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27463v1)