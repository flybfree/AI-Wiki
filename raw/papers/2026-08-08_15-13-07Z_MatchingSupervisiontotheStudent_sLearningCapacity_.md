---
title: Matching Supervision to the Student's Learning Capacity: A Unified Framework for On-Policy Self-Distillation
published: 2026-08-08T15:13:07Z
authors: Yongkang Yang, Zhezheng Hao, Hong Zhang, Yi Liu, Xiankun Lin, Wence Ji, Fanjunduo Wei, Jiarui Yu, Qiang Lin, Xiaoyun Liang, Hande Dong
url: http://arxiv.org/abs/2608.08176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Matching Supervision to the Student's Learning Capacity: A Unified Framework for On-Policy Self-Distillation

## Abstract
On-policy self-distillation (OPSD) improves the reasoning abilities of LLMs by internalizing privileged context into model parameters through self-distillation.   Two recent research lines promote vanilla OPSD by choosing which tokens to learn from and by controlling how much privileged information the teacher receives, respectively.   However, we show that each line optimizes one variable while holding the other fixed, which leads to a suboptimal solution.   We argue that the two variables are coupled through the student's learning capacity: the privileged information sets the per-token divergence the teacher prescribes, while token weighting selects which of these the student must absorb.   We formalize the two lines of work into a unified optimization framework, which maximizes the aggregate teacher--student divergence, subject to a budget on the aggregate learning difficulty the student can absorb.   Under this modelling, we propose Unified On-Policy Self-Distillation (USD), a lightweight online algorithm to solve the Lagrangian.   USD reveals that a single dual variable governs both decisions: at one price for learning difficulty, it simultaneously sets the token-selection threshold and the direction of privileged-information adjustment, keeping supervision matched to the student's evolving capacity.   Through extensive experiments, USD consistently demonstrates superior performance over OPSD and token- and PI-side baselines across various model scales on various reasoning benchmarks. Code is available at https://github.com/lauvlalala/USD.

## Metadata
- **Published**: 2026-08-08T15:13:07Z
- **Authors**: Yongkang Yang, Zhezheng Hao, Hong Zhang, Yi Liu, Xiankun Lin, Wence Ji, Fanjunduo Wei, Jiarui Yu, Qiang Lin, Xiaoyun Liang, Hande Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08176v1)