---
title: Rubric-as-Experts: Case-Specific MQM Rubrics for Translation Quality Evaluation
published: 2026-06-19T15:56:16Z
authors: Weilu Xu, Yunzhi Shen, Xinye Wang, Ranfei Dang, Shujian Huang
url: http://arxiv.org/abs/2606.21559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rubric-as-Experts: Case-Specific MQM Rubrics for Translation Quality Evaluation

## Abstract
Large language models (LLMs) have shown strong potential in fine-grained translation quality evaluation (QE), yet existing MQM-based approaches typically rely on fixed rubric configurations shared across all translation samples. However, translation instances often differ substantially in error complexity, ambiguity, and required evaluation granularity, making static rubric allocation suboptimal for span-level error detection. We find that larger MQM subtype spaces improve error coverage but also introduce more false positives, while different translation instances prefer different rubric granularities, suggesting that evaluation spaces should be allocated dynamically for each case. Motivated by these observations, we propose a case-specific dynamic rubric framework that adaptively constructs MQM evaluation spaces for individual translation instances. Unlike fully free-form rubric generation methods, our framework remains grounded in the predefined MQM taxonomy while dynamically selecting suitable subtype spaces and evaluation granularity for different cases. Experiments on WMT span-level QE benchmarks across multiple model scales demonstrate that the proposed framework consistently improves MCC and produces cleaner span-level error localization compared with static rubric settings. Our results suggest that combining structured MQM rubrics with case-specific adaptive allocation is an effective strategy for fine-grained LLM-based translation evaluation.

## Metadata
- **Published**: 2026-06-19T15:56:16Z
- **Authors**: Weilu Xu, Yunzhi Shen, Xinye Wang, Ranfei Dang, Shujian Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.21559v1)