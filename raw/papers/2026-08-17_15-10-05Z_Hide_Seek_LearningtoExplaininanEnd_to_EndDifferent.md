---
title: Hide&Seek: Learning to Explain in an End-to-End Differentiable Network
published: 2026-08-17T15:10:05Z
authors: Tal Ellinson, Hadi Mohasel Afshar, Sally Cripps
url: http://arxiv.org/abs/2608.16689v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hide&Seek: Learning to Explain in an End-to-End Differentiable Network

## Abstract
Instance-wise feature selection is a valuable tool for interpreting labeled data and the predictions of black-box models. In contrast to global feature selection techniques, instance-wise methods dynamically identify important features for each instance. A growing number of methods learn a selector, which identifies important features, and a predictor, which uses these to make predictions. However, these pioneering methods face challenges including information leakage and lack of differentiability, which can slow training. In this paper, we present Hide&Seek, an end-to-end differentiable model for instance-wise feature selection. We jointly learn feature selection and prediction under a single objective without information leakage. Hide&Seek outperforms existing state-of-the-art models across a range of experiments and is fast to train. We achieve this by reformulating feature removal as a differentiable operation where instead of discretely removing features, we replace a proportion of each feature. Training is further stabilized via a parsimony-weight annealing framework.

## Metadata
- **Published**: 2026-08-17T15:10:05Z
- **Authors**: Tal Ellinson, Hadi Mohasel Afshar, Sally Cripps
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16689v1)