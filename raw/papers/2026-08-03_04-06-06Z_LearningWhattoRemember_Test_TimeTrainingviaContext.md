---
title: Learning What to Remember: Test-Time Training via Context Distillation
published: 2026-08-03T04:06:06Z
authors: Zixuan Wang, Xingyu Dang, Rui-Jie Zhu, Zixin Wen, Hengyu Fu, Wenhao Chai, Jason D. Lee
url: http://arxiv.org/abs/2608.01672v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning What to Remember: Test-Time Training via Context Distillation

## Abstract
Effective long-context modeling is not merely about retaining more of the past, but about preserving the information that may prove relevant later. Test-time training (TTT) is an appealing approach that performs online parameter updates for long-context modeling, yet existing TTT methods only optimize either reconstruction or online adaptation objectives without considering the future utility of retained information. In this work, we propose \textbf{T}est-\textbf{T}ime \textbf{C}ontext \textbf{D}istillation (TTCD), a TTT framework that introduces a self-supervised objective for allocating limited memory capacity for future use. Specifically, TTCD uses a long-window teacher to supervise the fast weights of a short-window student, where the hidden-state discrepancy between them offers a dense, self-supervised signal guiding the model to memorize the contextual information crucial for future token predictions. We focus on an in-place variant: In-Place TTCD (IP-TTCD), which uses the existing MLP parameters as the fast weights. Experiments on long-context language modeling tasks show IP-TTCD consistently outperforms DeltaNet, Gated DeltaNet, sliding-window attention, and TTT when pre-trained from scratch. Furthermore, IP-TTCD allows pre-trained transformer models to adapt their parameters during inference through continual pre-training, gaining long-context capabilities with only a lightweight architectural augmentation. Our results position TTCD as a step toward architectural continual learning.

## Metadata
- **Published**: 2026-08-03T04:06:06Z
- **Authors**: Zixuan Wang, Xingyu Dang, Rui-Jie Zhu, Zixin Wen, Hengyu Fu, Wenhao Chai, Jason D. Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01672v1)