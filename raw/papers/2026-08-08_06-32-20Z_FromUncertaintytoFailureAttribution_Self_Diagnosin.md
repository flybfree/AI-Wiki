---
title: From Uncertainty to Failure Attribution: Self-Diagnosing Models for Failure Attribution under Distribution Shift
published: 2026-08-08T06:32:20Z
authors: Yiyao Yang
url: http://arxiv.org/abs/2608.07953v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Uncertainty to Failure Attribution: Self-Diagnosing Models for Failure Attribution under Distribution Shift

## Abstract
Distribution shift poses a significant challenge to the robustness of machine learning models, but the current solutions only aim to detect out-of-distribution (OOD) samples and predict uncertainty levels. We introduce a problem setting for failure attribution under distribution shift, which enables the models not only to detect OOD samples, but also to find out the reason for their failure. The solution we propose is called self-diagnosing models, which are capable of jointly learning predictive output, predictive uncertainty, and a failure attribution signal. In particular, we use the failure attribution vector, produced by a neural network, which provides a structured representation of predictive unreliability by distinguishing four different types of failures: covariance shift, semantic shift, noise corruption, and adversarial perturbation. In other words, we move from scalar uncertainty towards failure identification. For training the model, we introduce a consistency regularizer that encourages consistency between uncertainty and failure attribution predictions. Moreover, to be able to evaluate the model on its ability to find the reasons for failure, we construct several distribution shift benchmarks with predefined mechanisms for generating distribution shifts.

## Metadata
- **Published**: 2026-08-08T06:32:20Z
- **Authors**: Yiyao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07953v1)