---
title: You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs
published: 2026-09-22T07:39:35Z
authors: Yuanteng Chen, Qiwei Lai, Chen Tianqi, Peisong Wang, Yuantian Shao, Nanxin Zeng, Zhilei Liu, Chuangyi Li, Jing Liu, Jian Cheng
url: http://arxiv.org/abs/2609.25809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs

## Abstract
Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token. This shift makes dynamic expert pruning an attractive route to cheaper inference. Yet existing evidence comes largely from coarser architectures and likelihood-scored multiple-choice benchmarks, leaving three central questions open in the fine-grained regime: how redundant per-token expert selection is, how effectively existing pruning methods exploit that redundancy, and what governs a model's sensitivity to pruning. We fill this gap with a systematic empirical study of twelve fine-grained MoE checkpoints spanning nine architecture families, with a core suite of eleven benchmarks covering knowledge QA, mathematics, code generation, and general reasoning. We find that expert selection is far more redundant than the field's operating points assume: uniformly retaining about two thirds of the selected experts preserves 98.8% of unpruned performance on average, requiring only a one-integer change and delivering 1.2-1.7x measured speedup across two serving backends. This simple baseline leaves little room for dynamic allocation at conservative budgets: even the best published rules differ from it by under 1% at matched expert budgets. Their value emerges under aggressive pruning, where the best rules recover up to 3.0% over uniform truncation, with gains concentrated in the generative tasks that suffer the sharpest degradation. Sensitivity to aggressive pruning also depends on the model: larger and thinking models are more resilient, whereas multimodal models are more vulnerable. Together, these findings reveal how much expert computation fine-grained MoEs can dispense with, and establish when dynamic allocation earns its complexity, informing both practical deployment and future pruning methods.

## Metadata
- **Published**: 2026-09-22T07:39:35Z
- **Authors**: Yuanteng Chen, Qiwei Lai, Chen Tianqi, Peisong Wang, Yuantian Shao, Nanxin Zeng, Zhilei Liu, Chuangyi Li, Jing Liu, Jian Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25809v1)