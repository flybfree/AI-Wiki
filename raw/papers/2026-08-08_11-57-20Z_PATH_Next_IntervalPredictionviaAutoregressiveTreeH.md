---
title: PATH: Next-Interval Prediction via Autoregressive Tree Hierarchy on Tabular Data
published: 2026-08-08T11:57:20Z
authors: Pengxiang Cai, Wanchen Lian, Chenyang Liu, Xiaohan Li, Qingyuan Zeng, Jinhong Wang, Jintai Chen
url: http://arxiv.org/abs/2608.08078v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PATH: Next-Interval Prediction via Autoregressive Tree Hierarchy on Tabular Data

## Abstract
Interval prediction aims to achieve a target coverage level while producing intervals that are as short as possible. Many conformal regression pipelines first predict an uncertainty surrogate and then convert it into an interval through calibration or selection. This separation supports coverage calibration, but post hoc rules largely determine the final interval and do not fully use the learned output distribution. We observe that the resulting intervals have inherently hierarchical geometry: an interval can be recursively refined into nested subintervals, and binary trees naturally represent this structure. We formulate this hierarchy as next-interval prediction and propose PATH, which learns how probability mass flows from each interval to its next nested subintervals. PATH predicts a base leaf distribution and uses an autoregressive decoder to refine branch probabilities. Matching the distribution to the interval hierarchy aligns learning with extraction: PATH accumulates probability over adjacent output intervals and returns the shortest contiguous range reaching a selected mass. We compare PATH with 24 baselines for interval prediction on PATHBench, comprising 56 OpenML regression datasets. PATH substantially shortens the resulting intervals, achieving the lowest mean normalized length, 0.1473, while maintaining mean coverage of 0.9144. These results establish hierarchical output modeling as an effective approach for compact interval prediction on tabular data. Code is publicly available at https://github.com/pxcai/PATH.

## Metadata
- **Published**: 2026-08-08T11:57:20Z
- **Authors**: Pengxiang Cai, Wanchen Lian, Chenyang Liu, Xiaohan Li, Qingyuan Zeng, Jinhong Wang, Jintai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08078v1)