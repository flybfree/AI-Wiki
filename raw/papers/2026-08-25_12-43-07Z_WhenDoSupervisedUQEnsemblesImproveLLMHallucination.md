---
title: When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness Study
published: 2026-08-25T12:43:07Z
authors: Mohit Singh Chauhan, Vipin Gyanchandani, Dylan Bouchard
url: http://arxiv.org/abs/2608.24492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness Study

## Abstract
Uncertainty quantification (UQ) methods are widely used for hallucination detection in large language models (LLMs) in closed-book settings where ground-truth evidence is unavailable at inference time. Prior work has proposed combining UQ signals via learned ensembles, but empirical investigations into the robustness of these ensembles are limited. We study a supervised ensembling framework that trains a classifier over heterogeneous UQ-based scorer outputs on a small, domain-specific dataset of labeled LLM responses, then applies it to out-of-sample hallucination classification without retrieval, tools, or reference documents. Across four LLMs, nine datasets, and three generation regimes (short-form QA, long-form generation, and code generation), we provide a systematic robustness analysis along three axes: sample efficiency, in-domain dataset transfer, and generation regime dependence. We find that supervised ensembles outperform the best individual scorer in 30 of 32 settings, with gains realized from as few as 100 labeled instances. Ensembles retain most of their advantage in cases of in-domain transfer under distribution shift, outperforming the best non-ensemble scorer in 23 of 28 transfer settings. Sampling-based black-box ensembles are nearly as effective as full ensembles, while single-generation white-box ensembles offer limited benefit.

## Metadata
- **Published**: 2026-08-25T12:43:07Z
- **Authors**: Mohit Singh Chauhan, Vipin Gyanchandani, Dylan Bouchard
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24492v1)