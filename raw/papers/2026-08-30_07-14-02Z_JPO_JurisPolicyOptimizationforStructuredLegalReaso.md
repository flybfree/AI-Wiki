---
title: JPO: Juris Policy Optimization for Structured Legal Reasoning in Criminal Judgment Prediction
published: 2026-08-30T07:14:02Z
authors: Zhaolu Kang, Yantao Liu, Tailong Luo, Leqi Zheng, Lei Wei, Chenghua Zhu, Junhao Gong, Jiachen Qian, Eric Hanchen Jiang, Jiaxin Liu, Yuan Wang, Hao Zhang, Zixia Wang, Rong Fu, Zheng Lin, Richeng Xuan, Zhichao Hu
url: http://arxiv.org/abs/2608.29616v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JPO: Juris Policy Optimization for Structured Legal Reasoning in Criminal Judgment Prediction

## Abstract
Criminal judgment prediction requires models to infer statutory articles, charges, and sentencing outcomes from case facts. Unlike standard classification tasks, it involves a structured reasoning process in which statutes should be matched with facts, charges should be justified by statutes, and sentencing outcomes should remain consistent with charges. Existing approaches optimize final labels, and while some have attempted to evaluate reasoning quality, their evaluations are indirect, often relying on LLM-generated rubrics that reflect model-internal preferences rather than the inherent logical structure of legal adjudication. We propose Juris Policy Optimization (JPO), a post-training framework for structured legal reasoning in Chinese criminal judgment prediction. JPO first uses teacher-generated rationales to supervise a standardized four-step reasoning process, and then applies reinforcement learning with a composite reward over legal prediction quality, reasoning structure completeness, and cross-step consistency. JPO further introduces token-level advantage reweighting and adaptive clipping for legally salient reasoning segments. Experiments on multiple open-source language models and three Chinese legal benchmarks show that JPO consistently improves both judgment prediction and reasoning quality over supervised fine-tuning and reinforcement learning baselines.

## Metadata
- **Published**: 2026-08-30T07:14:02Z
- **Authors**: Zhaolu Kang, Yantao Liu, Tailong Luo, Leqi Zheng, Lei Wei, Chenghua Zhu, Junhao Gong, Jiachen Qian, Eric Hanchen Jiang, Jiaxin Liu, Yuan Wang, Hao Zhang, Zixia Wang, Rong Fu, Zheng Lin, Richeng Xuan, Zhichao Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29616v1)