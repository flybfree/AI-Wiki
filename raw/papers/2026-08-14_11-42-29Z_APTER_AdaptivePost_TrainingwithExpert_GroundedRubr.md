---
title: APTER: Adaptive Post-Training with Expert-Grounded Rubrics
published: 2026-08-14T11:42:29Z
authors: Xukai Wang, Liangqi Li, Zhiyue Xu, Jingang Zhou, Xiaoyu Shi, Jiansheng Cai, Bo Zhang, Zhe Li, Xu-Yao Zhang
url: http://arxiv.org/abs/2608.14212v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APTER: Adaptive Post-Training with Expert-Grounded Rubrics

## Abstract
As large language models enter professional domains, they must satisfy domain constraints, include critical evidence, and provide complete reasoning rather than merely produce fluent responses. Existing post-training methods often rely on holistic preferences or outcome-level verification, while recent rubric-based methods usually generate rubrics independently for each query. In specialized domains, such unconstrained rubrics may omit critical requirements and vary across samples, hindering the diagnosis and targeted repair of persistent capability deficiencies. We propose APTER (Adaptive Post-Training with Expert-Grounded Rubrics), a framework that integrates structured domain knowledge into fine-grained evaluation, optimization, and diagnosis for specialized complex reasoning. First, expert-grounded rubric construction starts from an expert criteria framework built by domain experts, where each criterion represents a stable professional capability. For each query, APTER selects relevant criteria and instantiates them into query-level rubrics linked to their source criteria, turning reusable expert criteria into executable query-level supervision without reference answers. Second, adaptive post-training uses rubric verdicts as both optimization and criterion-level diagnostic signals. Aggregating low-scoring verdicts by criterion ID reveals persistent deficiencies and triggers targeted supervised fine-tuning updates during reinforcement learning. Experiments on mathematical reasoning and medical question answering show consistent gains across both domains. Across three model generations, APTER improves the mathematics and medical averages over the corresponding base models by up to 15.86 and 8.04 points, respectively. Code and rubric datasets are available at https://github.com/AntDT-APTER/APTER.

## Metadata
- **Published**: 2026-08-14T11:42:29Z
- **Authors**: Xukai Wang, Liangqi Li, Zhiyue Xu, Jingang Zhou, Xiaoyu Shi, Jiansheng Cai, Bo Zhang, Zhe Li, Xu-Yao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14212v1)