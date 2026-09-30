---
title: VACE: Validation-Gated Alternating Co-Evolution of Agent Models and Harnesses
published: 2026-09-29T09:24:39Z
authors: Jiexing Qi, Yu He, Jun Liu, Qichen Huang, Shaohua Hu, Zhan Dang, Guohua Chen, Rui Yang, Wen Jiang, Yang Liu, Tao Lyu, Fangming Li
url: http://arxiv.org/abs/2609.37105v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VACE: Validation-Gated Alternating Co-Evolution of Agent Models and Harnesses

## Abstract
Language model agents can be improved by updating their model weights or refining the harness that guides task execution. These components are coupled: weight updates change how the model uses the harness, while harness updates change the trajectories used for training. We propose VACE, Validation-Gated Alternating CoEvolution, which alternates agentic reinforcement learning with trajectory-driven harness refinement. After each RL stage, VACE reuses the collected trajectories to propose a harness revision and evaluates the incumbent and candidate with the updated model held fixed. The candidate guides subsequent training only if it improves validation performance. With Qwen3.5-9B, VACE achieves 45.26% test accuracy on OfficeQA and a mean partial-credit score of 75.19% on AutomationBench, exceeding weight-only RL by 6.43 and 9.09 percentage points and ungated alternation by 4.59 and 6.95 points, respectively. Across 44 harness proposals, 17 reduce validation performance at the updated checkpoint and are rejected before subsequent RL training, highlighting the importance of validation gating.

## Metadata
- **Published**: 2026-09-29T09:24:39Z
- **Authors**: Jiexing Qi, Yu He, Jun Liu, Qichen Huang, Shaohua Hu, Zhan Dang, Guohua Chen, Rui Yang, Wen Jiang, Yang Liu, Tao Lyu, Fangming Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37105v1)