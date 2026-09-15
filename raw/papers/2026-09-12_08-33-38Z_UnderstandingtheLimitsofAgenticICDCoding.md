---
title: Understanding the Limits of Agentic ICD Coding
published: 2026-09-12T08:33:38Z
authors: Chong Yock Eng, Yushi Cao, Yiming Chen, Kezhi Mao, Hongchao Jiang
url: http://arxiv.org/abs/2609.13806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding the Limits of Agentic ICD Coding

## Abstract
ICD-10-CM codes are alphanumeric codes used in the US to classify diagnoses and injuries for medical billing and epidemiological reporting. Standard ICD-10-CM benchmarks report aggregate metrics that obscure performance on complex coding scenarios. We evaluate neural, workflow, and agentic systems on a rarity-stratified set of MIMIC-IV discharge summaries and identify two orthogonal failure modes. Neural classifiers exhibit a 0.43 micro-F1 gap between rare and common codes. Workflow systems handle rare codes well but score near zero on injury and external cause codes that require multi-step guideline following. A tool-augmented agentic configuration with structured access to official ICD-10-CM reference materials recovers up to 0.34 micro-F1 on this subset. No single system dominates across all conditions.

## Metadata
- **Published**: 2026-09-12T08:33:38Z
- **Authors**: Chong Yock Eng, Yushi Cao, Yiming Chen, Kezhi Mao, Hongchao Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13806v1)