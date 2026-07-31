---
title: A Fuzzy Rule-based Neuro-Symbolic Approach for Pipe Severity Prediction in Sewer Networks
published: 2026-07-30T16:33:26Z
authors: Ngoc Thai Le, Thanh Ma, Umberto Straccia
url: http://arxiv.org/abs/2607.28481v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Fuzzy Rule-based Neuro-Symbolic Approach for Pipe Severity Prediction in Sewer Networks

## Abstract
Standard automated sewer pipe severity assessment relies on direct image classification, creating a "black box" where the link between visual defects and final severity scores remains implicit. This study introduces a modular, fuzzy rule-based neuro-symbolic framework that bridges this gap by decoupling neural perception from symbolic reasoning. The perception module utilizes a Swin Transformer to predict 14 multilabel inspection CODE degrees directly from images. For reasoning, a DT, specifically Weka's J48, algorithm is trained on ground-truth CODEs and severity labels, and its paths are converted into 19 fixed IF--THEN rules. Inference operates via fuzzy logic: t-norm activations from CODE conditions are weighted by rule confidence and combined with corresponding s-norms to produce interpretable class evidence. We assessed Product, Łukasiewicz, and Hamacher operator pairs using a dataset of 3,244 images spanning five highly imbalanced severity classes. Ground-truth labels were robustly generated via consensus from five independent large language models analyzing original inspector notes. Our results show an improvement of accuracy, balanced accuracy, Macro F1 and MCC by 17.9%, 12.2%, 23.0%, and 17.3%, respectively, over image-only based classification.   Overall, the framework combines competitive class-balanced performance with traceable reasoning from predicted CODE degrees to rule supports and severity evidence.

## Metadata
- **Published**: 2026-07-30T16:33:26Z
- **Authors**: Ngoc Thai Le, Thanh Ma, Umberto Straccia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28481v1)