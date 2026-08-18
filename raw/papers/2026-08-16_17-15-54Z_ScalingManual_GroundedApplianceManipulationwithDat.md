---
title: Scaling Manual-Grounded Appliance Manipulation with Data Synthesis and Unified Planning
published: 2026-08-16T17:15:54Z
authors: Yuxing Long, Lei Kang, Ziyan Yu, Yuzheng Gao, Bin Cheng, Jiyao Zhang, Xiaoqi Li, Haolin Yang, Dongjiang Li, Hui Shen, Hao Dong
url: http://arxiv.org/abs/2608.15863v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scaling Manual-Grounded Appliance Manipulation with Data Synthesis and Unified Planning

## Abstract
Operating household appliances requires long-horizon planning that is state-dependent and robust to disturbances, yet existing large models fall short, as no sufficiently diverse, task-oriented dataset exists to support such planning. To bridge this gap, we propose MAGE, a scalable data synthesis pipeline that introduces a novel Hierarchical Appliance Graph (HAG) to automatically generate part grounding, long-horizon planning, and closed-loop recovery data from appliance manuals. With MAGE, we build UseAppliance, the first large-scale dataset for manual-grounded appliance manipulation planning, spanning 22 appliance categories with 89K+ part annotations, 53K+ manipulation tasks, and 33K+ closed-loop adjustment steps. Built on UseAppliance, we develop AppliancePlan, an end-to-end model for manual-grounded appliance manipulation planning. On RealAppliance-Bench, AppliancePlan with only 7B parameters achieves over 10x the best baseline on open-loop planning and consistently outperforms state-of-the-art models across all tasks. Real-robot experiments on six household appliances further confirm effective sim-to-real transfer, marking an important step toward general-purpose household robotics.

## Metadata
- **Published**: 2026-08-16T17:15:54Z
- **Authors**: Yuxing Long, Lei Kang, Ziyan Yu, Yuzheng Gao, Bin Cheng, Jiyao Zhang, Xiaoqi Li, Haolin Yang, Dongjiang Li, Hui Shen, Hao Dong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15863v1)