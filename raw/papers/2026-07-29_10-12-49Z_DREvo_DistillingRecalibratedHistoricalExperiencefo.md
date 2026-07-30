---
title: DREvo: Distilling Recalibrated Historical Experience for Harness Self-Evolution
published: 2026-07-29T10:12:49Z
authors: Hanghui Guo, Weijie Shi, Zhangze Chen, Shengxiang Xu, Yishu Wang, Yimei Zhang, Wangze Ni, Jia Zhu, Shimin Di
url: http://arxiv.org/abs/2607.26722v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DREvo: Distilling Recalibrated Historical Experience for Harness Self-Evolution

## Abstract
Harness plays a critical role in large language model agent performance, and building a high-performing harness requires substantial expert effort. Therefore, recent research has increasingly explored harness self-evolution, which iteratively proposes, evaluates, and improves harnesses using historical trial experience. However, accumulated historical experience does not always translate into stable search guidance, and performance often fluctuates substantially across evolution iterations, making it difficult to reliably discover high-performing harnesses under a limited evolution budget. We identify two limitations in how existing harness self-evolution methods leverage historical experience: (1) Lack of dynamic reassessment of whether historical experience remains valid for the current harness, and (2) Lack of explicit mechanisms for translating valid historical experience into actionable search directions. To address these limitations, we propose a new harness self-evolution method, named DREvo, which integrates function-level evidence anchoring, state-dependent evidence recalibration, and role-conditioned search intent distillation to determine which historical evidence remains valid and where the harness should evolve next. Under limited evolution budgets, DREvo exhibits smoother evolution trajectories, achieves the highest accuracy on all five benchmarks, and delivers average gains of 16.2% and 14.2% over the evaluated baselines on domain reasoning and agentic tasks, respectively.

## Metadata
- **Published**: 2026-07-29T10:12:49Z
- **Authors**: Hanghui Guo, Weijie Shi, Zhangze Chen, Shengxiang Xu, Yishu Wang, Yimei Zhang, Wangze Ni, Jia Zhu, Shimin Di
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26722v1)