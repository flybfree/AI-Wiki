---
title: From Detrimental to Beneficial: Dynamic Influence-based Valuation and Editing
published: 2026-08-23T17:46:18Z
authors: Adrian Nyakairu, Hongfu Liu
url: http://arxiv.org/abs/2608.22522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Detrimental to Beneficial: Dynamic Influence-based Valuation and Editing

## Abstract
Data valuation is a cornerstone of data-centric learning, where prior efforts primarily focus on designing algorithms to classify training samples as either beneficial or detrimental for the learning task. However, leveraging these valuation estimates for subsequent data intervention remains underexplored; conventional approaches typically discard or downweight harmful samples, thereby underutilizing available data resources. In this paper, we present Dynamic Influence-based Valuation and Editing (DIVE), a novel and efficient framework that dynamically estimates sample values at the batch level and transforms detrimental data into beneficial contributions. Rather than altering the raw data, DIVE operates at the optimization level by strategically reversing the gradient directions of harmful samples during training, ensuring seamless integration with standard learning procedures with minimal overhead. Extensive empirical evaluations demonstrate that DIVE consistently improves classification performance, maximizes data efficiency, stabilizes optimization, and effectively generalizes to large language model fine-tuning.

## Metadata
- **Published**: 2026-08-23T17:46:18Z
- **Authors**: Adrian Nyakairu, Hongfu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22522v1)