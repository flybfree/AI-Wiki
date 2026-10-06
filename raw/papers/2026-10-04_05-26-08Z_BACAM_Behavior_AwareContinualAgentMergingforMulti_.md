---
title: BACAM: Behavior-Aware Continual Agent Merging for Multi-Turn Interaction
published: 2026-10-04T05:26:08Z
authors: Shuaitong Li, Baochen Xiong, Xiaoshan Yang, Xizhe Zheng, Yifan Xu, Jianhao Huang, Changsheng Xu
url: http://arxiv.org/abs/2610.04966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BACAM: Behavior-Aware Continual Agent Merging for Multi-Turn Interaction

## Abstract
Model merging offers a way to integrate the capabilities of specialized experts, but existing agent merging methods typically require all of them to be available at once. We study continual agent merging, which integrates incoming experts sequentially without retaining previously merged experts. Yet merging in parameter space or feature subspaces does not ensure that the merged model acquires an incoming expert's behavior on interaction trajectories. Moreover, updates toward a new expert can disrupt the merged model's previously integrated interactive behavior. Therefore, we propose Behavior-Aware Continual Agent Merging (BACAM), which learns parameter-wise merging gates from candidate-generated trajectories using expert-guided behavioral supervision. Task-level stability-plasticity control and tensor-level conflict-aware update budgets limit interference with existing capabilities while allowing new ones to be acquired. The learned gates are folded into the model weights without additional inference-time parameters. Across four interactive tasks - web shopping, tool use, information retrieval, and embodied interaction - BACAM achieves an average success rate of 62.82%, exceeding the strongest evaluated merging baseline by 21.69 percentage points. Our code is publicly available at https://github.com/shuaitongli/BACAM.

## Metadata
- **Published**: 2026-10-04T05:26:08Z
- **Authors**: Shuaitong Li, Baochen Xiong, Xiaoshan Yang, Xizhe Zheng, Yifan Xu, Jianhao Huang, Changsheng Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04966v1)