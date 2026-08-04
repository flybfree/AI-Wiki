---
title: SERL-SQL: Selective Hindsight Distillation for Text-to-SQL Reinforcement Agentic Learning
published: 2026-08-01T07:24:12Z
authors: Tao Liu, Tao Feng, Xiangheng Li, Jinwang Song, Yifan Li, Xiaoqing Cheng, Dixuan Zhang, Siquan Li, Lin Lan, Hongying Zan, Kunli Zhang, Chao Wu
url: http://arxiv.org/abs/2608.00485v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SERL-SQL: Selective Hindsight Distillation for Text-to-SQL Reinforcement Agentic Learning

## Abstract
Recent Text-to-SQL systems increasingly rely on multi-turn interaction, execution feedback, and reinforcement learning. However, most existing methods use execution correctness only as a trajectory-level reward, which provides limited guidance for identifying the SQL decisions responsible for success or failure. We propose SERL-SQL, a selective execution-grounded reinforcement learning framework for multi-turn Text-to-SQL agents. SERL-SQL samples on-policy SQL interaction trajectories and uses a training-only teacher to re-score student actions with execution feedback. The resulting teacher--student likelihood gap is converted into bounded, masked weights that reweight GRPO advantages only on SQL and tool-action tokens. In this way, task rewards preserve the optimization direction, while execution hindsight provides localized credit assignment. Experiments on BIRD, Spider, and cross-domain benchmarks show that SERL-SQL achieves competitive performance, reaching 76.56% execution accuracy on BIRD-Dev and 89.92% on Spider-Test. Moreover, our reward-based selection strategy closely approaches the oracle Best-of-N upper bound and consistently outperforms consistency-based selection, showing that SERL-SQL produces high-quality candidates that can be reliably identified by lightweight execution-grounded rewards. Our code will be released at https://github.com/Ffunkytao/SERL-SQL.

## Metadata
- **Published**: 2026-08-01T07:24:12Z
- **Authors**: Tao Liu, Tao Feng, Xiangheng Li, Jinwang Song, Yifan Li, Xiaoqing Cheng, Dixuan Zhang, Siquan Li, Lin Lan, Hongying Zan, Kunli Zhang, Chao Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00485v1)