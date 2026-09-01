---
title: MedCache: Efficient and Temporally Valid Memory for Longitudinal Clinical Agents
published: 2026-08-30T03:28:56Z
authors: Hei Ting,  Chan, Chenwei Wu, Xueshen Liu, Boyuan Zheng, Liyue Shen, Jiasi Chen, Z. Morley Mao
url: http://arxiv.org/abs/2608.29528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedCache: Efficient and Temporally Valid Memory for Longitudinal Clinical Agents

## Abstract
Longitudinal clinical agents must maintain an evolving patient state from evidence distributed across visits, time points, and specialties. However, how agent memory should be designed for this setting remains unclear. We introduce a benchmark of multi-visit, multi-specialty patient records that evaluates long-context evidence retrieval, cross-time evidence aggregation, and cross-specialty clinical reasoning. Using this benchmark, we systematically study four memory design choices: curation, organization, retrieval, and memory-augmented reasoning. We find that temporal validity is more important than simply retaining more history; specialty-factorized memory reduces context but can hide shared evidence; and multiple agents help when specialists must reason together, not merely when evidence comes from multiple memories. Guided by these findings, we propose \textit{MedCache}, a hybrid framework that constructs temporally valid patient memory, organizes evidence into overlapping specialty views, routes each query to relevant memories, and adaptively invokes one or multiple specialists. Experiments show that MedCache improves reasoning accuracy and memory efficiency over strong single-agent and multi-agent baselines, while generalizing across model backbones and external datasets.

## Metadata
- **Published**: 2026-08-30T03:28:56Z
- **Authors**: Hei Ting,  Chan, Chenwei Wu, Xueshen Liu, Boyuan Zheng, Liyue Shen, Jiasi Chen, Z. Morley Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29528v1)