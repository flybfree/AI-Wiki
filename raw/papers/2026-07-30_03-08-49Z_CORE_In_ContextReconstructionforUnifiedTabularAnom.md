---
title: CORE: In-Context Reconstruction for Unified Tabular Anomaly Detection
published: 2026-07-30T03:08:49Z
authors: Yunfeng Zhao, Qingfeng Chen, Yue Tan, Shiyuan Li, Yili Wang, Yixin Liu, Shirui Pan
url: http://arxiv.org/abs/2607.27615v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CORE: In-Context Reconstruction for Unified Tabular Anomaly Detection

## Abstract
Tabular anomaly detection (TAD), which focuses on identifying abnormal samples that deviate from the majority in tabular data, has received growing attention. Recently, there has been an emerging trend towards unified TAD, which seeks to detect anomalies across different datasets using a single generalizable model. In unified TAD, aligning heterogeneous data remains challenging. While existing methods often rely on distance-based unified feature construction, they may obscure the semantics of the original features. Moreover, existing approaches typically formulate anomaly detection as a binary classification task, which may overlook diverse anomaly patterns from various datasets and be misled by unrepresentative synthetic anomalies. To address these challenges, we propose an in-COntext REconstruction approach for unified TAD (CORE for short). It introduces a decorrelated feature alignment module to directly align heterogeneous features into a unified representation space, which retains their semantic information. Meanwhile, CORE formulates unified TAD as an in-context reconstruction problem, eliminating the need for labeled or synthesized anomalies. Specifically, the in-context reconstruction module reconstructs each sample by leveraging contextual normal samples to capture dataset-specific distributions, such that reconstruction errors reflect its deviation from normality, facilitating unified TAD on arbitrary unseen datasets.

## Metadata
- **Published**: 2026-07-30T03:08:49Z
- **Authors**: Yunfeng Zhao, Qingfeng Chen, Yue Tan, Shiyuan Li, Yili Wang, Yixin Liu, Shirui Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27615v1)