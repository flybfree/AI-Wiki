---
title: DE-Venus: A Data-Efficient RLVR Framework for Large Language Models
published: 2026-09-03T03:23:24Z
authors: Shenzhi Yang, Guangcheng Zhu, Kai Tang, Zhengqing Zang, Xing Zheng, Haobo Wang, Yingfan Ma, Bowen Song, Bo Han, Bo An, Lei Feng, Weiqiang Wang, Junbo Zhao, Gang Chen
url: http://arxiv.org/abs/2609.03324v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DE-Venus: A Data-Efficient RLVR Framework for Large Language Models

## Abstract
Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-policy rollouts and the cost of obtaining reliable targets at scale. Existing methods address sample selection, incomplete supervision, or noisy labels separately, often entangling supervision logic with distributed training and hindering controlled comparison and reuse. We present DE-Venus, a unified framework for data-efficient RLVR that treats supervision as evolving state across data preparation and policy optimization. It organizes this lifecycle into three modules: Active Data Selection allocates training and annotation budgets; Weak Supervision Construction derives learning signals from unlabeled examples; and Training-Time Supervision Refinement filters or corrects unreliable supervision. DE-Venus supports seven representative methods and a data-selection pipeline by expressing method-specific decisions as offline dataset transitions or online transformations of targets, rewards, batches, and advantages while preserving verl's distributed execution contracts. Across public benchmarks and three business scenarios, separate configurations preserve or improve model quality with only 10% of labels or as little as 13% of relevant data; selected business configurations also reduce observed convergence steps by 63%--75%. DE-Venus thus reduces annotation and training costs without sacrificing scalable RL execution.

## Metadata
- **Published**: 2026-09-03T03:23:24Z
- **Authors**: Shenzhi Yang, Guangcheng Zhu, Kai Tang, Zhengqing Zang, Xing Zheng, Haobo Wang, Yingfan Ma, Bowen Song, Bo Han, Bo An, Lei Feng, Weiqiang Wang, Junbo Zhao, Gang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03324v1)