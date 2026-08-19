---
title: Picture the Epsilon: Pursuing Identity-Level Privacy Guarantees for Images
published: 2026-08-17T21:30:06Z
authors: Arman Zareian Jahromi, Vishnu Bondalakunta, Mohammad Akbar Bin Shah, Naimul Haque, Shuangqing Wei, George T. Amariucai
url: http://arxiv.org/abs/2608.17147v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Picture the Epsilon: Pursuing Identity-Level Privacy Guarantees for Images

## Abstract
Image-to-image face generators are widely used, and visual dissimilarity between their outputs and source images is sometimes treated as evidence of privacy. Auditing whether these systems satisfy formal identity-level (epsilon, delta)-differential privacy requires choosing among several distinct routes for converting embedding-space observations into estimates or bounds on the differential privacy parameter epsilon. We present a comparative study of four such audits applicable to pre-trained, black-box face generators: a Gaussian-mechanism reading of per-identity sensitivity (GaussMech); a per-dimension kernel-density log-ratio aggregated by basic composition (KDE-LR); an analytical population-level lower bound on pure-DP epsilon derived from the maximum mean discrepancy via the total variation distance (MMD-TV); and a hypothesis-testing evaluation of a cross-validated classifier's out-of-fold ROC (ROC-HT). For each method we make explicit its assumptions, hyperparameter dependence, finite-sample limitations, and the regime in which its epsilon estimate is informative. Applied to FaceFusion and InstantID across multiple identity encoders and reference datasets, the audits consistently reveal substantial identity distinguishability while reporting markedly different epsilon estimates that reflect each method's distinct assumptions and finite-sample treatment. In this high-distinguishability regime, the experiments do not support a reliable ranking of the four methods. Their relative trade-offs should be evaluated on partially private mechanisms, which we identify as the natural next study. The resulting framework places these audits in a shared identity-level audit setting and clarifies how their assumptions and finite-sample treatments shape the resulting differential privacy estimates.

## Metadata
- **Published**: 2026-08-17T21:30:06Z
- **Authors**: Arman Zareian Jahromi, Vishnu Bondalakunta, Mohammad Akbar Bin Shah, Naimul Haque, Shuangqing Wei, George T. Amariucai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17147v1)