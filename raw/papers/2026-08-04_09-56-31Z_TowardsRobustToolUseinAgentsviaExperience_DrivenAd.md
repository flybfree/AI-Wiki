---
title: Towards Robust Tool Use in Agents via Experience-Driven Adaptive Guidance
published: 2026-08-04T09:56:31Z
authors: Can Wang, Haoran Chen, Li Yu, Ding Hao, Bohai Zhao, Zhaoyang Liu, Zhiying Tu
url: http://arxiv.org/abs/2608.03403v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Robust Tool Use in Agents via Experience-Driven Adaptive Guidance

## Abstract
The performance bottleneck of agents is increasingly shifting from model capability to the robustness of their execution processes. Tools play a central role as the primary interface through which agents interact with external environments, yet existing methods rarely focus on ensuring robust tool use across diverse runtime conditions. To address this problem, we propose ExpG, a mechanism that builds and refines adaptive guidance capturing each tool's capability boundaries and best practices, thereby enabling agents to use tools more robustly and effectively. ExpG consists of three phases: (1) experience acquisition, which analyzes tool invocation quality from historical execution trajectories, producing structured learnable experiences through multi-aspect attribution; (2) experience distillation, which keeps the experience pool effective by filtering unhelpful experiences, selecting representative ones with an equivalence-class-based method, and summarizing them into generalizable guidance; and (3) experience reuse, which applies the guidance adaptively during future task solving. Extensive experiments show that ExpG brings consistent improvements across the tool selection, tool calling, and response generation tasks, enabling smaller agents to outperform larger ones that do not use ExpG. Moreover, ExpG achieves particularly strong gains in challenging settings, suggesting a promising path toward more robust tool use. Our code, experiments, and results are available.

## Metadata
- **Published**: 2026-08-04T09:56:31Z
- **Authors**: Can Wang, Haoran Chen, Li Yu, Ding Hao, Bohai Zhao, Zhaoyang Liu, Zhiying Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03403v1)