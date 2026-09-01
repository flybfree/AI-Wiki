---
title: PAC: Progress-Augmented Advantage Curriculum for Multi-Task Reinforcement Learning of LLMs
published: 2026-08-31T09:59:07Z
authors: Yuanqiang Yu, Yanzhao Zheng, Zhentao Zhang, Tianze Xu, Chao Ma, Jihuai Zhu, Jiashun Liu, Xinle Deng, Baohua Dong, Hangcheng Zhu, Ruohui Huang
url: http://arxiv.org/abs/2608.30528v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PAC: Progress-Augmented Advantage Curriculum for Multi-Task Reinforcement Learning of LLMs

## Abstract
Reinforcement learning (RL) is used to improve the reasoning abilities of LLMs, while training data span heterogeneous tasks. However, most RL post-training pipelines rely on fixed or manually designed task mixtures, even though task usefulness changes as training progresses. Online curriculum methods often define learnability by update magnitude, ignoring whether the update translates into reward gains, which can misallocate rollout budget toward tasks with large but ineffective updates. We propose PAC, a Progress-Augmented Advantage Curriculum for multi-task RL of LLMs that combines two task-level signals: advantage-derived learnability, which measures the magnitude of the policy update a task can induce, and recent reward gains, which show whether those updates have improved task performance. A Bayesian Thompson Sampling controller uses these signals to allocate rollouts across tasks during GRPO training. We evaluate PAC under two settings: a multi-level reasoning setting and a multi-domain reasoning setting. PAC improves sample efficiency and final performance: it reaches comparable validation scores with fewer rollout steps and achieves higher final averages than random sampling and advantage-based curriculum baselines in both settings. These results show that jointly tracking advantage signals and actual reward gains yields an effective online curriculum for LLM post-training.

## Metadata
- **Published**: 2026-08-31T09:59:07Z
- **Authors**: Yuanqiang Yu, Yanzhao Zheng, Zhentao Zhang, Tianze Xu, Chao Ma, Jihuai Zhu, Jiashun Liu, Xinle Deng, Baohua Dong, Hangcheng Zhu, Ruohui Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30528v1)