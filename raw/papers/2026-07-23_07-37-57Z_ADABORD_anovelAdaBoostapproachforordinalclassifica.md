---
title: ADABORD: a novel AdaBoost approach for ordinal classification
published: 2026-07-23T07:37:57Z
authors: Rafael Ayllón-Gavilán, Francisco José Martínez-Estudillo, David Guijo-Rubio, César Hervás-Martínez, Pedro A. Gutiérrez
url: http://arxiv.org/abs/2607.21003v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ADABORD: a novel AdaBoost approach for ordinal classification

## Abstract
Ordinal Classification (OC) deals with classification tasks where the classes follow a natural order. Despite the progress in OC, many existing approaches fail to fully leverage the ordinal information, treating the problem as nominal classification and thereby losing performance potential. In this work, ADABORD, an AdaBoost framework specifically designed for ordinal classification problems, is introduced. The ordinal nature of the classes is incorporated into two key components of the well-known AdaBoost algorithm: 1) the base estimator, where decision trees with the ordinal Gini splitting criterion are proposed; 2) the error function used to update sample weights at each stage and the weights of the classifier in the final ensemble model, given by the absolute ranked probability score, a measure that accounts for both the ordering and the distance between classes. ADABORD is extensively compared against seven state-of-the-art methods on the TOC-UCO repository, the largest benchmark collection for OC to date. The experimental results, supported by statistical analysis, show that ADABORD significantly outperforms competing methods, particularly on datasets with five or more classes, where the ordinal structure becomes more pronounced. Source code, along with all experimental protocols, is publicly available to ensure reproducibility and facilitate future research in OC.

## Metadata
- **Published**: 2026-07-23T07:37:57Z
- **Authors**: Rafael Ayllón-Gavilán, Francisco José Martínez-Estudillo, David Guijo-Rubio, César Hervás-Martínez, Pedro A. Gutiérrez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21003v1)