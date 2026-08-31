---
title: PersonaForge: Realistic Multi-Turn User Simulation for Agentic Systems
published: 2026-08-28T14:33:19Z
authors: Hanglong Lv, Dawei Zhu, Lei Li, Bowen Ye, Huaqiu Liu, Yifan Song, Bofei Gao, Weimin Xiong, Jinhao Dong, Chenhong He, Lingpeng Kong, Qi Liu, Tong Yang, Fuli Luo
url: http://arxiv.org/abs/2608.28378v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PersonaForge: Realistic Multi-Turn User Simulation for Agentic Systems

## Abstract
Large language models are increasingly used as agentic workflow executors, yet existing training data and benchmarks largely assume informationally complete, single-turn queries. Our analysis of 16K real-world sessions shows that 75.9% of interactions are multi-turn, revealing a substantial gap between how users interact with agents and how such systems are trained and evaluated. We introduce \textbf{PersonaForge}, a user simulation framework for synthesizing realistic multi-turn user--agent interactions. PersonaForge combines a four-dimensional persona space, SOUL-driven behavioral control calibrated to real-user statistics, and Reverse Deep Construction grounded in authentic seed queries. Using PersonaForge, we construct a 6.3K-record training dataset and \textbf{PersonaForge-Bench}, a manually annotated 138-task benchmark spanning over 20 professional domains with four-dimensional scoring. Experiments on Qwen3.5-27B show that PersonaForge training improves the composite score by +4.1%, with gains across all four dimensions and the largest improvements in Task Completion (+6.0%) and Response Quality (+6.8%). Further analyses show that PersonaForge-trained agents use fewer turns and tool calls, suggesting improved interaction efficiency, while ablations confirm the contribution of SOUL components and adaptive simulation. Together, PersonaForge and PersonaForge-Bench establish a foundation for training and evaluating agents under realistic multi-turn user interaction.

## Metadata
- **Published**: 2026-08-28T14:33:19Z
- **Authors**: Hanglong Lv, Dawei Zhu, Lei Li, Bowen Ye, Huaqiu Liu, Yifan Song, Bofei Gao, Weimin Xiong, Jinhao Dong, Chenhong He, Lingpeng Kong, Qi Liu, Tong Yang, Fuli Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28378v1)