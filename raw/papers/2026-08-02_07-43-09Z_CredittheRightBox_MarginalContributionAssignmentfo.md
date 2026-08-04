---
title: Credit the Right Box: Marginal Contribution Assignment for Structured Visual Perception
published: 2026-08-02T07:43:09Z
authors: Xinheng Han, Jianfei Wang, Yu Chen, Xiang Wang, Shuai Li, Weixing Li, Feng Pan
url: http://arxiv.org/abs/2608.01055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Credit the Right Box: Marginal Contribution Assignment for Structured Visual Perception

## Abstract
Multimodal Large Language Models (MLLMs) are increasingly expected to solve structured perception tasks that require visual recognition, language-to-object binding, object cardinality preservation, and precisely localized grounding and segmentation outputs. However, existing group-relative reinforcement learning methods provide only response-level supervision, creating a granularity mismatch for structured multi-object prediction: a single advantage is broadcast to all tokens in a response, without distinguishing individual box contributions. To address this mismatch, we propose MCR-GRPO, a marginal contribution assignment framework that derives box-level credit directly from each sampled response. Specifically, Marginal Contribution Reward (MCR) estimates each predicted box's contribution through a leave-one-out comparison, measuring how the matched set value changes when the box is removed from the response. After within-response normalization, records that improve the set value receive positive credit, while redundant or harmful ones are suppressed. To make marginal attribution stable and informative, we further introduce a Continuous Matched Set Value Evaluator that integrates permutation-invariant matching, count-aware normalization, and graded localization. MCR-GRPO maps normalized box-level marginal advantages to the token spans that generated each box, preserving GRPO's response-level comparison while enabling box-aware optimization of structured multi-object grounding. Experiments across REC, DOD, segmentation, and counting benchmarks show state-of-the-art performance over prior GRPO-based baselines.

## Metadata
- **Published**: 2026-08-02T07:43:09Z
- **Authors**: Xinheng Han, Jianfei Wang, Yu Chen, Xiang Wang, Shuai Li, Weixing Li, Feng Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01055v1)