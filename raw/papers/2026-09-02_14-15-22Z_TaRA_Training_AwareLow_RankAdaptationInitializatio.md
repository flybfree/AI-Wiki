---
title: TaRA: Training-Aware Low-Rank Adaptation Initialization
published: 2026-09-02T14:15:22Z
authors: Taehyeon Kim, Eunhyeok Park
url: http://arxiv.org/abs/2609.02639v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TaRA: Training-Aware Low-Rank Adaptation Initialization

## Abstract
Low-Rank Adaptation (LoRA) has become a de facto standard for parameter-efficient fine-tuning (PEFT), yet its performance is highly sensitive to initialization due to the information bottleneck imposed by low-rank decomposition. Existing approaches attempt to construct high-quality LoRA initializations by exploiting principal components of pretrained weights, activations, or gradients. However, these methods do not directly account for the training dynamics of the full-rank model. In this paper, we propose Training-aware Low-Rank Adaptation Initialization (TaRA), a method that initializes LoRA such that the gradients induced by the low-rank factors closely approximate the gradient of the corresponding full-rank weight matrix. Derived from a mathematical formulation, TaRA improves gradient fidelity at the start of training while introducing negligible computational overhead. Across diverse and challenging fine-tuning tasks, TaRA consistently outperforms prior state-of-the-art methods, establishing a simple, robust, and scalable solution for effective LoRA initialization.

## Metadata
- **Published**: 2026-09-02T14:15:22Z
- **Authors**: Taehyeon Kim, Eunhyeok Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02639v1)