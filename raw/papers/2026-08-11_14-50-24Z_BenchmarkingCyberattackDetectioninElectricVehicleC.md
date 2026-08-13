---
title: Benchmarking Cyberattack Detection in Electric Vehicle Charging Infrastructure with Benign User Updates
published: 2026-08-11T14:50:24Z
authors: Hannan Chen, Roshni Anna Jacob, Jie Zhang
url: http://arxiv.org/abs/2608.11286v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking Cyberattack Detection in Electric Vehicle Charging Infrastructure with Benign User Updates

## Abstract
Cyberattack detection in electric vehicle charging infrastructure is complicated by legitimate post-activation revisions to requested energy and departure time. Charging manipulation attacks can exploit the same interface and variables; therefore, detecting a request change alone does not establish malicious intent. This paper develops a leakage-controlled session-level benchmark that preserves the ordered inputs of real Adaptive Charging Network (ACN) sessions and models legitimate revisions as normal behavior. A fixed pool keeps each generated attack in its source session's split and contains six physically motivated attacks and their coordinated variants. We compare 22 profile-only, transition-aware, and context-stratified model families under common source-grouped folds, attack data, and operating constraints. The proposed Dual-Branch Masked-Autoencoder (Masked-AE) Transition Boost model evaluates whether the current request is normal and whether its producing transition resembles an observed benign update. Its state branch combines masked reconstruction with a radial-basis-function one-class support boundary, while its transition branch combines masked reconstruction with shrinkage covariance distance. Source-grouped five-fold cross-validation selects complete configurations under explicit overall-normal and benign-update acceptance constraints; disjoint normal data then calibrate the final threshold before one test evaluation. The developed dual-branch model provides the strongest robust validation performance while detecting malicious request manipulations without learning to reject legitimate user choices.

## Metadata
- **Published**: 2026-08-11T14:50:24Z
- **Authors**: Hannan Chen, Roshni Anna Jacob, Jie Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11286v1)