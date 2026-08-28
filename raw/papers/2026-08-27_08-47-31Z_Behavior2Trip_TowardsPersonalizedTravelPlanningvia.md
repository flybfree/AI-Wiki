---
title: Behavior2Trip: Towards Personalized Travel Planning via User Behavior Trajectory
published: 2026-08-27T08:47:31Z
authors: Zihao Cheng, Yingyu Shan, Hongru Wang, Zeming Liu, Xinyi Wang, Xiangrong Zhu, Yuhang Guo, Wei Lin, Yunhong Wang
url: http://arxiv.org/abs/2608.26807v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Behavior2Trip: Towards Personalized Travel Planning via User Behavior Trajectory

## Abstract
Travel planning agents assist users in generating personalized travel plans by modeling their individual preferences. Existing agents either rely on explicit user instructions or engage in multi-turn clarification to elicit user preferences. However, both approaches overlook the rich behavioral signals latent in users' past behaviors, which implicitly encode their preferences. This over-reliance on active user input increases interaction burden and limits plan personalization. To bridge this gap, we introduce a new task, Behavior-Aware Travel Planning, which infers user preferences directly from past behaviors and generates personalized travel plans. To facilitate research on this task, we introduce Behavior2Trip, a benchmark constructed from one of the largest Chinese online travel platforms, comprising 11,400 instances. Each instance represents an average of 39.8 past user behaviors spanning 14 attributes across 5 preference dimensions. We further propose B2T-Agent, a reinforcement learning-based agent that leverages user behavior trajectories, interacts with external tools for preference-aligned retrieval, and maintains an internal memory module. Experiments on Behavior2Trip show that GPT-4.1 achieves a full-constraint pass rate of only 0.5\% on the hardest tasks, while B2T-Agent built upon Qwen3-8B outperforms all baselines, highlighting the substantial challenge of this task. Moreover, Qwen3-8B trained with B2T-Agent also outperforms GPT-4.1 on the TravelPlanner benchmark, demonstrating strong generalization. Code and data are available at https://github.com/BUAA-IRIP-LLM/Behavior2Trip

## Metadata
- **Published**: 2026-08-27T08:47:31Z
- **Authors**: Zihao Cheng, Yingyu Shan, Hongru Wang, Zeming Liu, Xinyi Wang, Xiangrong Zhu, Yuhang Guo, Wei Lin, Yunhong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26807v1)