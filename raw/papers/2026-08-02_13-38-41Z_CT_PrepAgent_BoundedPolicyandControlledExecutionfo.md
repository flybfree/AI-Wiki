---
title: CT-PrepAgent: Bounded Policy and Controlled Execution for Adaptive CT Data Preparation
published: 2026-08-02T13:38:41Z
authors: Xiaolin Fan, Yue Pei, Yingying Zhang, Haogang Zhu
url: http://arxiv.org/abs/2608.01233v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CT-PrepAgent: Bounded Policy and Controlled Execution for Adaptive CT Data Preparation

## Abstract
Heterogeneous computed tomography (CT) acquisitions and diverse downstream task requirements limit the transferability of fixed data preparation workflows across data sources and tasks. Existing approaches typically rely on manually designed or dataset-specific rules, making it difficult to accommodate changes in acquisition conditions and analytical objectives without manual intervention. Large language model (LLM)-based agents have shown promise for automating medical workflows, yet their potential for adaptive CT data preparation remains largely unexplored. To bridge this gap, we propose CT-PrepAgent, which enables adaptive CT data preparation through a bounded policy and controlled deterministic execution. Deterministic inspection constructs structured data--task profiles, from which a policy decides an eligible DICOM series or predefined preprocessing profile, while the controlled execution flow guards, resolves, executes, and verifies the decision with bounded recovery when enabled and safe quarantine otherwise. Across three public CT segmentation tasks, CT-PrepAgent derived data-task adaptive preprocessing decisions and achieved the highest macro-average Dice. On two private raw-DICOM cohorts, CT-PrepAgent increased verified output yield from 61.7\% to 70.0\% and yielded similar registration metrics on common verified outputs. Controlled fault and replay tests validate bounded recovery, safe quarantine, and policy-free replay under tested fault and drift settings.

## Metadata
- **Published**: 2026-08-02T13:38:41Z
- **Authors**: Xiaolin Fan, Yue Pei, Yingying Zhang, Haogang Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01233v1)