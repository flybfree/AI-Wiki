---
title: Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach
published: 2026-05-13T17:52:19Z
authors: S. Akshay, Chaitanya Garg, Ashutosh Gupta, Kuldeep S. Meel, Ajinkya Naik
url: http://arxiv.org/abs/2605.13830v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantifying Sensitivity for Tree Ensembles: A symbolic and compositional approach

## Abstract
Decision tree ensembles (DTE) are a popular model for a wide range of AI classification tasks, used in multiple safety critical domains, and hence verifying properties on these models has been an active topic of study over the last decade. One such verification question is the problem of sensitivity, which asks, given a DTE, whether a small change in subset of features can lead to misclassification of the input. In this work, our focus is to build a quantitative notion of sensitivity, tailored to DTEs, by discretizing the input space of the model and enumerating the regions which are susceptible to sensitivity. We propose a novel algorithmic technique that can perform this computation efficiently, within a certified error and confidence bound. Our approach is based on encoding the problem as an algebraic decision diagram (ADD), and further splitting it into subproblems that can be solved efficiently and make the computation compositional and scalable. We evaluate the performance of our technique over benchmarks of varying size in terms of number of trees and depth, comparing it against the performance of model counters over the same problem encoding. Experimental results show that our tool XCount achieves significant speedup over other approaches and can scale well with the increasing sizes of the ensembles.

## Metadata
- **Published**: 2026-05-13T17:52:19Z
- **Authors**: S. Akshay, Chaitanya Garg, Ashutosh Gupta, Kuldeep S. Meel, Ajinkya Naik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.13830v1)