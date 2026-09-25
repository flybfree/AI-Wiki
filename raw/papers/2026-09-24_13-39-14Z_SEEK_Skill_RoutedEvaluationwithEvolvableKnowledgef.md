---
title: SEEK: Skill-Routed Evaluation with Evolvable Knowledge for Industrial Search
published: 2026-09-24T13:39:14Z
authors: Zhongxin Huang, Songyang Li, Renzhe Zhou, Feiran Zhu, Chenglei Dai, Zhen Xiao, Xuanping Li, Jingwei Zhuo
url: http://arxiv.org/abs/2609.29803v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SEEK: Skill-Routed Evaluation with Evolvable Knowledge for Industrial Search

## Abstract
Search quality evaluation provides essential supervision and diagnostic signals for the development and iteration of industrial search systems. Although large language models (LLMs) offer a scalable alternative to manual assessment, reliable automatic evaluation remains challenging: users experience search results at the page level, while the applicable evaluation criteria are multi-dimensional and continuously evolving. Packing all evaluation criteria into a unified prompt introduces irrelevant context and potential criterion interference, whereas internalizing them through post-training tightly couples rule updates with costly model retraining cycles.   To address these issues, we propose Skill-routed Evaluation with Evolvable Knowledge (SEEK). Specifically, SEEK externalizes specific search evaluation criteria into a skill bank, dynamically routes relevant skills for each query-result list pair, and employs a task-adapted listwise evaluator to produce page-level judgments and failure mode attribution. A two-stage training pipeline teaches the evaluator to align evaluation criteria with human preferences, while a replay-gated skill bank allows recurring evaluation knowledge gaps to be incorporated without model retraining. Experiments on industrial short-video search show that SEEK improves listwise quality evaluation accuracy and achieves significant progress in attribution diagnosis. SEEK has been deployed at Kuaishou, a short-video platform with over 400 million daily active users, significantly improving the scale and quality of online search evaluation.

## Metadata
- **Published**: 2026-09-24T13:39:14Z
- **Authors**: Zhongxin Huang, Songyang Li, Renzhe Zhou, Feiran Zhu, Chenglei Dai, Zhen Xiao, Xuanping Li, Jingwei Zhuo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29803v1)