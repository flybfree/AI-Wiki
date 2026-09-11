---
title: COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization
published: 2026-09-10T15:12:24Z
authors: Pingchen Lu, Xiangyi Wang, Xiang Li, Jie Mao, Zikun Qu, Junfeng Luo, Yao Shu, Bryan Kian Hsiang Low, Zhongxiang Dai
url: http://arxiv.org/abs/2609.11682v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization

## Abstract
Large language model (LLM) agents can benefit from reusable skills distilled from prior task experience, yet existing skill optimization methods often rely on costly execution-based evaluation and substantial task data. We introduce \textbf{COBRA-Skills}, an efficient framework that formulates skill optimization as budgeted sequential optimization over a dynamically evolving candidate space. COBRA-Skills couples contextual-bandit-guided prioritization with evidence-grounded skill evolution, selectively allocating evaluations to promising or informative candidates while continually refining the skill population from execution feedback. Across six heterogeneous agent benchmarks and three target models, COBRA-Skills consistently achieves the strongest average performance among compared methods, while reducing optimization cost by 55--58\% relative to SkillOpt and using only 50 unique optimization examples per benchmark. Further analyses show that COBRA-Skills remains robust to changes in the agent harness and performs effectively when the target model itself is used for skill generation and refinement.

## Metadata
- **Published**: 2026-09-10T15:12:24Z
- **Authors**: Pingchen Lu, Xiangyi Wang, Xiang Li, Jie Mao, Zikun Qu, Junfeng Luo, Yao Shu, Bryan Kian Hsiang Low, Zhongxiang Dai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11682v1)