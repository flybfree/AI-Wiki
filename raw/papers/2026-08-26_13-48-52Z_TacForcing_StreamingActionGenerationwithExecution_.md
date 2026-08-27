---
title: TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback
published: 2026-08-26T13:48:52Z
authors: Jianbo Zhou, Boyuan Zhao, Yuzheng Zhang, Yiyang Chen, Wenxin Chen, Qiuyue Li, Xiangyang Gu, Yuhan Cao, Xiao Xia, Yanzhe Hu, Zhijie Deng
url: http://arxiv.org/abs/2608.25798v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback

## Abstract
Contact-rich manipulation requires adapting to contact states that can evolve substantially within an action horizon. However, chunk-based vision-language-action models predict complete action chunks from observations collected before execution, leaving tactile conditioning stale during execution. Existing tactile-reactive approaches typically rely on separate high-frequency controllers, which increase both architectural and training complexity. In this paper, we introduce TacForcing, a streaming action-generation framework that effectively incorporates execution-time tactile feedback. Instead of employing a separate reactive controller, TacForcing replaces the standard action expert with a streaming action expert to generate actions conditioned on the evolving tactile observations acquired during execution. TacForcing also introduces Execution-Aware Tactile Attention (EATA), which restricts tactile conditioning to actions nearing execution, thereby reducing the temporal mismatch between tactile acquisition and action execution. Across six simulated UniVTAC tasks and three real-world contact-rich manipulation tasks, TacForcing achieves average success rates of 65% and 69%, respectively, outperforming strong baselines in both settings.

## Metadata
- **Published**: 2026-08-26T13:48:52Z
- **Authors**: Jianbo Zhou, Boyuan Zhao, Yuzheng Zhang, Yiyang Chen, Wenxin Chen, Qiuyue Li, Xiangyang Gu, Yuhan Cao, Xiao Xia, Yanzhe Hu, Zhijie Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25798v1)