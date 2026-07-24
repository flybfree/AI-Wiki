---
title: Auto-Fill: Learning to Predict Missing Values Accurately with Specialist Language Models
published: 2026-07-22T07:32:09Z
authors: Yurong Liu, Yeye He, Haoyu Dong, Junjie Xing, Shi Han, Dongmei Zhang, Surajit Chaudhuri
url: http://arxiv.org/abs/2607.19847v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auto-Fill: Learning to Predict Missing Values Accurately with Specialist Language Models

## Abstract
Predicting missing cell values in tabular data is a fundamental problem in data cleaning. While state-of-the-art reasoning models show great promise in predicting missing values in tables, by reasoning holistically across rows and columns, they are costly to deploy at scale and tend to be overconfident, often generating hallucinated or false-positive predictions.   In this paper, we observe that achieving high-precision missing-value prediction in tables requires a distinct combination of three capabilities: (1) world knowledge, (2) text-based reasoning, and (3) code-based reasoning. We systematically explore design choices for combining these capabilities, and propose an Auto-Fill approach that post-trains three specialist small language models (SLMs), each optimized for one capability. We develop a calibrated ensemble mechanism that either dynamically selects the most confident specialist or abstains, ensuring high accuracy.   Extensive experiments on 11 benchmarks with 2200 real tables drawn from diverse domains show that Auto-Fill achieves superior accuracy compared to state-of-the-art reasoning models (e.g., o3-pro, Gemini 3 Pro, and DeepSeek R1), while operating at a fraction (less than 1%) of the cost of these frontier models. Our results highlight the effectiveness of specialization and calibrated abstention in the important domain of tabular data. Auto-Fill is publicly available at https://github.com/lyrain2001/auto-fill.

## Metadata
- **Published**: 2026-07-22T07:32:09Z
- **Authors**: Yurong Liu, Yeye He, Haoyu Dong, Junjie Xing, Shi Han, Dongmei Zhang, Surajit Chaudhuri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19847v1)