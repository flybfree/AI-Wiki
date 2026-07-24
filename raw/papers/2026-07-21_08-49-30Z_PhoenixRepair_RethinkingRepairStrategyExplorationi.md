---
title: PhoenixRepair: Rethinking Repair Strategy Exploration in Software Agents
published: 2026-07-21T08:49:30Z
authors: Tianyue Jiang, Yanlin Wang, Xin He, Daya Guo, Jiachi Chen, Ming Wen, Ensheng Shi, Xilin Liu, Yuchi Ma, Guanbin Li
url: http://arxiv.org/abs/2607.18859v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PhoenixRepair: Rethinking Repair Strategy Exploration in Software Agents

## Abstract
While Large Language Models have greatly advanced automated issue resolution, existing agent-based methods exhibit a fundamental limitation in their insufficient exploration of repair strategies. This insufficiency manifests in two key aspects. First, the exploration of multiple potential edit locations is limited. Second, the exploration of repair attempts at each location is also insufficient. To address these challenges, we present PhoenixRepair, a multi-agent framework that systematically explores multiple candidate edit locations and performs iterative reflection and refinement on patch generation, thereby expanding the search space of repair strategies. Our framework begins with multi-location sampling, optionally augmented with graph-based localization information for difficult tasks, followed by iterative reflection and refinement to generate better patches, culminating in final-round generation guided by distilled insights from all historical attempts. Experiments on SWE-bench-Verified demonstrate that PhoenixRepair achieves the largest relative improvement of 7.8\% over SWE-agent under DeepSeek-V3.1, and attains the highest resolved rate of 76.0\% Pass@1 under MiniMax-M2.5. Meanwhile, it achieves higher fault localization accuracy than existing approaches. Our code is available at https://github.com/DeepSoftwareAnalytics/PhoenixRepair.

## Metadata
- **Published**: 2026-07-21T08:49:30Z
- **Authors**: Tianyue Jiang, Yanlin Wang, Xin He, Daya Guo, Jiachi Chen, Ming Wen, Ensheng Shi, Xilin Liu, Yuchi Ma, Guanbin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18859v1)