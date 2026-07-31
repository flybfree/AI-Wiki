---
title: ReDiPPO: Reference-Guided Value Calibration and Discrepancy-Aware Token Reweighting for Mathematical Reasoning
published: 2026-07-30T03:42:52Z
authors: Zhenrong Zhang, Fei Wu, Jun Du, Jianshu Zhang, Si Wei
url: http://arxiv.org/abs/2607.27631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReDiPPO: Reference-Guided Value Calibration and Discrepancy-Aware Token Reweighting for Mathematical Reasoning

## Abstract
Reinforcement learning has emerged as an effective paradigm for enhancing the mathematical reasoning capabilities of large language models. Among existing policy optimization methods, Proximal Policy Optimization (PPO) remains particularly appealing because its learned critic can, in principle, provide token-level credit assignment. However, in mathematical reasoning tasks characterized by long reasoning horizons and sparse outcome rewards, reliable token-level credit assignment remains challenging. The standard critic often fails to accurately evaluate intermediate reasoning states, resulting in noisy advantage estimates and suboptimal policy updates. In this paper, we propose ReDiPPO, a Reference-guided and Discrepancy-aware PPO framework for mathematical reasoning. ReDiPPO introduces a reference-guided critic that uses reference answers as training-time privileged signals to provide more accurate value estimation. Meanwhile, it retains a standard critic and quantifies the token-level reference-standard discrepancy between the standard value estimate and the reference-guided value estimate. This discrepancy serves as an indicator of difficult reasoning states and is used to reweight the corresponding token-level advantages during PPO optimization. Extensive experiments on diverse mathematical reasoning benchmarks demonstrate that ReDiPPO improves value-estimation accuracy and consistently outperforms strong policy optimization baselines, including PPO, DAPO, and GSPO, in final reasoning performance. Our code is available on https://github.com/cii030/ReDiPPO.

## Metadata
- **Published**: 2026-07-30T03:42:52Z
- **Authors**: Zhenrong Zhang, Fei Wu, Jun Du, Jianshu Zhang, Si Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27631v1)