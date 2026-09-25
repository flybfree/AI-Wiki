---
title: Rufus-Air: An Open LLM Post-Training Recipe
published: 2026-09-24T11:45:03Z
authors: Chia-Yuan Chang, Renyuan Cheng, Rui Feng, Xiaotian Han, Yuan He, Hongye Jin, Linwei Li, Shiyang Li, Fenglin Liu, Xin Liu, Priyanka Nigam, Haoyang Wen, Zhenghao Xu, Zhuocheng Xu, Bing Yin, Qingyu Yin, Chao Zhang, Rongzhi Zhang, Zhihan Zhang, Zixuan Zhang, Zixuan Zhang, Tuo Zhao
url: http://arxiv.org/abs/2609.29421v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rufus-Air: An Open LLM Post-Training Recipe

## Abstract
Rufus-Air is an open and reproducible post-training recipe on GLM-4.5-Air-Base (106B-A12B), organized as a serial pipeline of eight stages: SFT, Reasoning RL, Coding RL, Instruction-Following RL, General Agent, Coding Agent, Search Agent, and RLHF. We document the data, reward design, infrastructure, stage order, and stagewise results needed to reproduce the recipe. Stages progress from basic to advanced capabilities and from hard, verifiable rewards to softer judge-based signals. Training builds on open-source components and public data, much of it used as released, without new human annotation or an in-house distillation teacher. Our main findings are that (i) diverse, high-quality SFT establishes a strong capability floor; (ii) difficulty filtering keeps RL prompts within a productive learning range; (iii) reward reliability provides a practical principle for ordering stages; and (iv) infrastructure and engineering choices are part of the recipe, not just an implementation detail. Rufus-Air improves over the official GLM-4.5-Air post-trained release and is competitive with similarly sized open models.

## Metadata
- **Published**: 2026-09-24T11:45:03Z
- **Authors**: Chia-Yuan Chang, Renyuan Cheng, Rui Feng, Xiaotian Han, Yuan He, Hongye Jin, Linwei Li, Shiyang Li, Fenglin Liu, Xin Liu, Priyanka Nigam, Haoyang Wen, Zhenghao Xu, Zhuocheng Xu, Bing Yin, Qingyu Yin, Chao Zhang, Rongzhi Zhang, Zhihan Zhang, Zixuan Zhang, Zixuan Zhang, Tuo Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29421v1)