---
title: APPSim-Bench: Bridging Real-world Apps and Reproducible Evaluation for Mobile GUI Agents
published: 2026-09-07T16:25:13Z
authors: Jintian Feng, Long Chen, Xiao Yu, Jiayi Dai, Chenglong Liu, Haoru Wang, Zizhen Xue, Yuxuan Shi, Ziyang Wang, Yichen Gong
url: http://arxiv.org/abs/2609.07712v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APPSim-Bench: Bridging Real-world Apps and Reproducible Evaluation for Mobile GUI Agents

## Abstract
Mobile GUI agents can execute tasks from natural-language instructions, but their evaluation remains difficult to make both realistic and reproducible. Existing benchmarks typically trade off these goals: simplified apps lack real-world mobile complexity, whereas live commercial apps introduce uncontrolled variation from recommendations, advertisements, accounts, and changing content. We propose AppSim-Bench, which addresses this trade-off through controllable simulated apps that preserve task-relevant interaction logic while supporting deterministic evaluation. Built through a coding-agent-assisted and human-verified workflow, it contains 557 tasks across 17 high-frequency Chinese and English apps. Its controllable backend data and outcome-based verification remove major sources of environmental stochasticity, enabling reproducible cross-model comparison. Evaluating 19 GUI agents, spanning general-purpose and GUI-specialized systems, we find that autonomous mobile execution remains far from solved. The best model completes only 50.27% of tasks, and 28.55% of tasks are not solved by any agent. Further analysis shows that failures concentrate in longer workflows, numerical reasoning tasks, and inefficient trajectories marked by high action overhead and budget exhaustion. Our project is available at https://github.com/Acrab-Agentic-Labs/AppSim.

## Metadata
- **Published**: 2026-09-07T16:25:13Z
- **Authors**: Jintian Feng, Long Chen, Xiao Yu, Jiayi Dai, Chenglong Liu, Haoru Wang, Zizhen Xue, Yuxuan Shi, Ziyang Wang, Yichen Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07712v1)