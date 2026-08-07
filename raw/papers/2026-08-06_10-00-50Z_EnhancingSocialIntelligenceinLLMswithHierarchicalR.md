---
title: Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level Goal Rewarding
published: 2026-08-06T10:00:50Z
authors: Xiaofeng Wang, Kakam Chong, Shuai Xiao, DeXin Kong, Qingyuan Tian, Chen Ju, Xu Yan, Shuai Zhao, Fei Huang, Rui Wang, Shuguang Han, jufeng chen
url: http://arxiv.org/abs/2608.05832v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Social Intelligence in LLMs with Hierarchical Reasoning and Utterance-Level Goal Rewarding

## Abstract
Large language models (LLMs) excel in structured tasks but struggle with dynamic social interactions, where success requires long-term goal coordination and rapid adaptation. Current methods often apply uniform goal-based rewards to every utterance, overlooking the specificity of objectives at each dialogue turn and failing to account for the rationale of potential strategies. Inspired by the Theory of Planned Behavior, we propose the Think-Strategy-Response (TSR) framework, which decomposes social dialogue into two hierarchical stages: high-level strategic planning and low-level linguistic execution. To optimize TSR, we introduce Linearized Hierarchical Reinforcement Learning with Variance-Gated Rewards (LHRL-VGR), a novel algorithm that dynamically routes rewards - balancing goal completion and strategy adherence - based on the variance of goal achievement scores. Experiments on the SOTOPIA benchmark show that our approach fine-tunes a Qwen2.5-7B agent to surpass the GPT-4o baseline by 7.32% in goal completion success, demonstrating state-of-the-art performance in multi-agent social negotiation tasks.

## Metadata
- **Published**: 2026-08-06T10:00:50Z
- **Authors**: Xiaofeng Wang, Kakam Chong, Shuai Xiao, DeXin Kong, Qingyuan Tian, Chen Ju, Xu Yan, Shuai Zhao, Fei Huang, Rui Wang, Shuguang Han, jufeng chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05832v1)