---
title: Analyzing and Mitigating Cross-Lingual Degradation in Multilingual Medical VQA
published: 2026-08-23T11:04:45Z
authors: Jingbo Wang, Sendong Zhao, Haochun Wang, Bing Qin, Ting Liu
url: http://arxiv.org/abs/2608.22363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Analyzing and Mitigating Cross-Lingual Degradation in Multilingual Medical VQA

## Abstract
Medical visual question answering (VQA) is a crucial task in clinical AI, yet its evaluation has so far centered almost exclusively on English, limiting its relevance to linguistically diverse patients and clinicians. Recent multilingual medical VQA benchmarks show that large vision-language models (LVLMs) degrade in non-English languages, but lack a fine-grained analysis of how cross-lingual variation affects the distinct capabilities that medical VQA requires. To this end, we construct a multilingual medical VQA benchmark over eight languages, organized into four representative scenarios that isolate the core capabilities medical VQA requires. Evaluating five open- and closed-source LVLMs, we find that cross-lingual degradation is not uniform but highly scenario-dependent. We therefore propose MedVL-XLRepE, a training-free scenario-aware representation engineering method, leveraging LVLMs' superior English medical VQA capability to steer non-English representations toward their English counterparts at inference time. Across three LVLMs and eight languages, MedVL-XLRepE consistently mitigates cross-lingual degradation, with gains of up to 6.33\%.

## Metadata
- **Published**: 2026-08-23T11:04:45Z
- **Authors**: Jingbo Wang, Sendong Zhao, Haochun Wang, Bing Qin, Ting Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22363v1)