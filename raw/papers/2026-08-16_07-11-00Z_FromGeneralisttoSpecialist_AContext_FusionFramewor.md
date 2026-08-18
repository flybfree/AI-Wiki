---
title: From Generalist to Specialist: A Context-Fusion Framework for Endoscopic Polyp Reporting with a Frozen VLM
published: 2026-08-16T07:11:00Z
authors: Ruijie Yang, Yan Zhu, Peiyao Fu, Siyuan Li, Te Luo, Zhihua Wang, Quanlin Li, Pinghong Zhou, Xian Yang, Shuo Wang
url: http://arxiv.org/abs/2608.15580v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Generalist to Specialist: A Context-Fusion Framework for Endoscopic Polyp Reporting with a Frozen VLM

## Abstract
Reliable endoscopic polyp reporting requires integrating quantitative lesion sizing, standardized Paris classification, and clinically meaningful morphological description within a single record. General-purpose vision-language models (VLMs) offer a unified interface for image understanding and report generation. Existing specialization strategies, however, typically rely on task-specific models or model-weight adaptation, leaving unresolved how to introduce reliable specialist knowledge while preserving both this unified interface and the VLM's pretrained capabilities. We introduce a context-fusion framework that specializes a frozen general-purpose VLM through both implicit instruction context and explicit transduction context without modifying its pretrained weights. Specifically, a self-supervised polyp encoder retrieves related image-report pairs as explicit, query-specific evidence, while learned continuous specialist tokens provide implicit instruction context shared across cases. Experiments were conducted on 2,056 expert-annotated public endoscopic images. We compared the framework with general-purpose VLMs, task-specific predictors, and weight-adaptation methods to assess specialist performance, unified reporting, and adaptation efficiency. Across numerical, categorical, and report-generation metrics, the proposed framework substantially improved direct frozen-VLM inference and achieved the strongest overall performance among the evaluated methods. It added trainable parameters equal to only 0.006% of the frozen VLM's parameter count. When the top-1 retrieved case carried the correct target category, our framework corrected 70.5% of the errors made by a weight-adaptation baseline. These findings support the context-fusion framework as a lightweight and effective strategy for specialist adaptation of a frozen VLM.

## Metadata
- **Published**: 2026-08-16T07:11:00Z
- **Authors**: Ruijie Yang, Yan Zhu, Peiyao Fu, Siyuan Li, Te Luo, Zhihua Wang, Quanlin Li, Pinghong Zhou, Xian Yang, Shuo Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15580v1)