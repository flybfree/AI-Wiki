---
title: MERID: Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis
published: 2026-09-28T20:29:26Z
authors: Lei Liu, Zhaokang Liang, Qingcheng Zeng, Chenda Duan, Lu Mi, Zhen Tan, Tianyu Liu
url: http://arxiv.org/abs/2609.36235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MERID: Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis

## Abstract
Major depressive disorder (MDD) severely impacts daily activities and quality of life. Detecting MDD involves multimodal data, such as interview recordings and sensor measurements. This is particularly challenging, as these heterogeneous modalities often demand distinct, customized prediction pipelines. Existing efforts to address this challenge have explored both manually engineered multimodal architectures and agent-assisted pipeline development. Despite their progress, it remains challenging to autonomously revise pipelines based on experimental feedback and carry verified improvements forward into subsequent designs. To this end, we propose Multimodal Exploration via Recursive Self-Improvement Agents for Major Depression Analysis (MERID). The framework develops depression pipelines through experience-based recursive self-improvement (RSI). Grounded State Construction (GSC) grounds experience by aligning multimodal records with subject-level depression targets. Coupled Pipeline Exploration (CPE) jointly modifies representations, fusion, and predictors to build successor pipelines for classification and severity estimation. Evidence-Guided Evolution (EGE) guides revisions through feedback and verifies gains under uncertainty in small depression cohorts before inheritance. Extensive experiments on depression benchmarks show that MERID achieves the best results on multiple tasks compared with multimodal and agent-based baselines. Further analysis highlights the value of acoustic and linguistic cues for depression detection. Our code is available at https://github.com/DiscoAILab/MERID

## Metadata
- **Published**: 2026-09-28T20:29:26Z
- **Authors**: Lei Liu, Zhaokang Liang, Qingcheng Zeng, Chenda Duan, Lu Mi, Zhen Tan, Tianyu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36235v1)