---
title: Benchmarking Language Models for Statistical Problem Formulation
published: 2026-09-02T01:37:17Z
authors: Chen Wang, Junzhe Zhao, Xin Cong, Wanlu Deng, Ke Deng
url: http://arxiv.org/abs/2609.01982v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking Language Models for Statistical Problem Formulation

## Abstract
Large language models (LLMs) are increasingly used as assistants for statistical and data science work, yet existing evaluations largely assume the analysis target is already specified. In practice, users arrive with informal goals and heterogeneous data, leaving the model to decide what statistical task is implied and which data are relevant. We first formalize this upstream step as Statistical Problem Formulation and decompose it into two subtasks: (1) Statistical Problem Classification and (2) Variable Identification & Role Assignment. We then introduce StatFormBench, a benchmark built from five cross-domain statistics textbooks and a data science case library, covering diverse problem types, data representations, and scenario styles. It contains 1,013 samples spanning 20 coarse-grained and 85 fine-grained statistical problem categories. Across 14 open- and closed-source LLMs, the best zero-shot models reach only 72.0 fine-grained classification accuracy and 63.2 variable set overlap. No model performs consistently best across the two subtasks, while enhanced prompting strategies yield only limited or inconsistent gains. We release the benchmark data on Hugging Face at https://huggingface.co/datasets/THU-CongLab/StatFormBench and the evaluation code on GitHub at https://github.com/THU-CongLab/StatFormBench.

## Metadata
- **Published**: 2026-09-02T01:37:17Z
- **Authors**: Chen Wang, Junzhe Zhao, Xin Cong, Wanlu Deng, Ke Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01982v1)