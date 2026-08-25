---
title: Diversity-Based Active Learning: An Evaluation of Metric Spaces for Active Learning Selection
published: 2026-08-24T16:30:10Z
authors: Siddharth Chilamkur, Dorit S. Hochbaum
url: http://arxiv.org/abs/2608.23461v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diversity-Based Active Learning: An Evaluation of Metric Spaces for Active Learning Selection

## Abstract
With rapid advancement over the last few years, many different methods are now widely used for classification. However, training these models requires substantial labeled data. Active Learning is a potential solution to this problem. Pool-based active learning minimizes costs by querying only the most informative samples from an unlabeled dataset. Diversity-based approaches, on the other hand, attempt to select a representative subset of the data. There are many different objectives for determining the selection process, including exact K-center, exact K-median, and Greedy K-center. In this paper, we will focus on evaluating the performance of Greedy K-center across a variety of metric spaces: the raw feature space, a Linear Discriminant Analysis (LDA) space, and a model-derived probability space (with and without entropy-based weighting). Using Random Forest classifiers as a baseline evaluator, our empirical results on synthetic and real-world datasets demonstrate that mapping unlabeled instances into a predictive probability space and weighting the result by entropy often dominates the other options for active learning selection with Greedy K-center.

## Metadata
- **Published**: 2026-08-24T16:30:10Z
- **Authors**: Siddharth Chilamkur, Dorit S. Hochbaum
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23461v1)