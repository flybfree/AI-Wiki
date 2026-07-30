---
title: DIRECT: Direct Decoding for Efficient and Aligned Sequence Labeling with Large Language Models
published: 2026-07-29T13:23:30Z
authors: Yilei Wang, Jiaxin Gan, Kexuan Zhang, Ling Li, Wentao Zhang, Peichao Lai
url: http://arxiv.org/abs/2607.26891v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DIRECT: Direct Decoding for Efficient and Aligned Sequence Labeling with Large Language Models

## Abstract
Sequence labeling is a fine-grained information extraction task, yet existing large language model-based approaches suffer from insufficient domain alignment and low inference efficiency. To address these issues, we propose DIRECT, a framework that addresses these issues through training-time optimization and inference-time rectification. Specifically, DIRECT performs Direct Preference Optimization (DPO) after supervised fine-tuning to strengthen task alignment with human preferences, and introduces a controlled decoding process that enforces fixed output formats and restricts predictions to candidate sets. To further improve efficiency, a template-filling mechanism requires the model to generate only label tokens while reusing prefixed content through the KV Cache, thus reducing redundant computation. Experimental results on eight datasets demonstrate that DIRECT achieves significant improvements in both performance and efficiency compared to existing methods.

## Metadata
- **Published**: 2026-07-29T13:23:30Z
- **Authors**: Yilei Wang, Jiaxin Gan, Kexuan Zhang, Ling Li, Wentao Zhang, Peichao Lai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26891v1)