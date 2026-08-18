---
title: FETERS: Few-Shot Early Time-Series Classification via Effective Ratio Selection
published: 2026-08-17T10:38:31Z
authors: Chen-An Tai, Yujia Wu, Vincent S. Tseng
url: http://arxiv.org/abs/2608.16385v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FETERS: Few-Shot Early Time-Series Classification via Effective Ratio Selection

## Abstract
Early time-series classification (ETSC) aims to make accurate predictions from partially observed time series as early as possible. Although various stopping mechanisms and feature learning strategies have been developed for ETSC, most existing methods assume access to sufficient labeled training data, which may be unrealistic in applications with limited annotation. Under limited supervision, learning an additional sample-level stopping module and extracting effective classification features can both become challenging. In this paper, we propose FETERS, a few-shot ETSC framework that selects a dataset-level stopping ratio through class-wise leave-one-out (LOO) evaluation on the support set and uses a penalty-based reward function to manage the accuracy-earliness trade-off, thereby avoiding the need to train an additional stopping module. FETERS further combines Rocket-based features with frozen Chronos representations for classification. Extensive experiments on 69 public datasets spanning 14 domains show that FETERS achieves state-of-the-art (SOTA) performance in the 5-shot setting, with the highest average harmonic mean (HM) and the best HM on 38 datasets, while outperforming the current SOTA method on 44 datasets. FETERS also remains competitive in the full-shot setting, demonstrating its effectiveness in managing the accuracy-earliness trade-off.

## Metadata
- **Published**: 2026-08-17T10:38:31Z
- **Authors**: Chen-An Tai, Yujia Wu, Vincent S. Tseng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16385v1)