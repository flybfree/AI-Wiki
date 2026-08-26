---
title: Scalable Question-Centric Text-to-Image Evaluation: Reliable Ranking, Fine-Grained Diagnosis, and Cost-Aware Routing
published: 2026-08-25T06:20:18Z
authors: Shaoan Zhao, Fang Zhao, Xueqiang Guo, Xinpei Su, Huanlin Gao, Qiang Hui, Ting Lu, Fuyuan Shi, Chao Tan, Bikun Yang, Kai Wang, Shiguo Lian
url: http://arxiv.org/abs/2608.24112v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scalable Question-Centric Text-to-Image Evaluation: Reliable Ranking, Fine-Grained Diagnosis, and Cost-Aware Routing

## Abstract
Modern text-to-image (T2I) models often have similar total scores but different strengths, making practical selection difficult. Fine-grained benchmarks decompose prompts into questions, yet often return them to prompt scores and fixed categories, weakening attribution and ignoring complexity. Related requirements are also scored separately or as one total, obscuring basic versus compositional failure. We present QC-T2I-Bench, a question-centric framework that converts open prompts into attributed atomic questions and organizes their dependencies with Davidsonian Scene Graphs (DSGs). We use hierarchy-constrained question aggregation to exclude downstream questions after a prerequisite fails and to prevent simple and complex prompts from receiving the same total weight. We then use the DSG structure to measure joint success within prompts and compare repeated entities across prompts, separating basic realization failures from failures under additional requirements. We evaluate multiple open-source T2I models on English and Chinese prompts. The resulting question-level evidence supports reliable ranking and fine-grained diagnosis: joint completion falls from 80.7\% for components with two capabilities to 37.2\% for those with seven or more. Finally, we reuse the same records for training-free routing; our cost-aware router matches ERNIE's 89.51-point estimate with 21.3\% less GPU-s/MP.

## Metadata
- **Published**: 2026-08-25T06:20:18Z
- **Authors**: Shaoan Zhao, Fang Zhao, Xueqiang Guo, Xinpei Su, Huanlin Gao, Qiang Hui, Ting Lu, Fuyuan Shi, Chao Tan, Bikun Yang, Kai Wang, Shiguo Lian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24112v1)