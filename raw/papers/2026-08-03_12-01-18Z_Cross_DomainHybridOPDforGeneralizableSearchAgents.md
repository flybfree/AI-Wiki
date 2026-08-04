---
title: Cross-Domain Hybrid OPD for Generalizable Search Agents
published: 2026-08-03T12:01:18Z
authors: Hongzhan Chen, Xiaoyu Liu, Dengming Zhang, Minzhou Huang, Dongliang Xu, Jingcheng Xie, Dongxiang Fang, Bowen Qin, Minsheng Hao, Yaozong Shen, Xiaojun Quan, Mona Zhou, Haosheng Zou, Jeff Chen
url: http://arxiv.org/abs/2608.02101v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Domain Hybrid OPD for Generalizable Search Agents

## Abstract
Recent advances in Reinforcement Learning (RL) have substantially improved the capabilities of autonomous search agents, enabling sophisticated planning, and iterative retrieval over dynamic information sources. However, optimizing language models for specialized search behaviors often incurs an alignment tax, where gains in search performance come at the expense of general-purpose capabilities, limiting their effectiveness as universal assistants. In this technical report, we present the training framework behind the Yuanbao search agent, designed to achieve search specialization without sacrificing general intelligence. Built upon the Hunyuan3 architecture, our framework combines agentic reinforcement learning for autonomous search with a cross-domain expert On-Policy Distillation (OPD) pipeline. Experts specializing in complementary general-purpose domains are distilled into the search-specialized student, restoring and further enhancing its broad capabilities. Rather than treating specialization and general capability as competing objectives, our hybrid training strategy jointly optimizes both, effectively mitigating the alignment tax. Extensive experiments demonstrate that the resulting model achieves competitive search performance while consistently improving its general-purpose capabilities, providing a favorable balance between specialized execution and broad generalization in real-world search scenarios.

## Metadata
- **Published**: 2026-08-03T12:01:18Z
- **Authors**: Hongzhan Chen, Xiaoyu Liu, Dengming Zhang, Minzhou Huang, Dongliang Xu, Jingcheng Xie, Dongxiang Fang, Bowen Qin, Minsheng Hao, Yaozong Shen, Xiaojun Quan, Mona Zhou, Haosheng Zou, Jeff Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02101v1)