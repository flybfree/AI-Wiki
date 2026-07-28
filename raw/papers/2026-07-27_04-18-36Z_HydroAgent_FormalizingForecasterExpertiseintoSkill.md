---
title: HydroAgent: Formalizing Forecaster Expertise into Skill-Orchestrated Flood Forecasting Workflows
published: 2026-07-27T04:18:36Z
authors: Qingyi Yang, Siqian Qiu, Bing Li, Xu Shan, Jia Feng, Shunan Zhou, Xudong Zhou, Tiantian Xing, Jiale Guo, Xiaoyi Dong, Gaoyu Liu, Xiaohuan Liu, Haiqing Pu, Qingwen Deng, Xun Zhang, Zhongrun Xiang, Haiyang Qian, Ying Yan, Yongkang Xu, Nuo Lei, Tianlong Jia, Baoying Shan, Carlo De Michele
url: http://arxiv.org/abs/2607.23983v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HydroAgent: Formalizing Forecaster Expertise into Skill-Orchestrated Flood Forecasting Workflows

## Abstract
Operational flood forecasting depends on tacit forecaster expertise that is difficult to formalize, audit, and transfer. Although artificial intelligence methods have advanced flood prediction and model-error correction, most existing studies have not explicitly represented the tacit expert rules, review checkpoints, and workflow constraints that connect model outputs to operational warning decisions. To address this issue, we propose HydroAgent, a skill-orchestrated agent framework that embeds Large Language Models (LLMs) into a model-driven flood forecasting workflow, where each skill encodes explicit rules to bound LLM reasoning. We validated its effectiveness using five state-of-the-art LLMs in the South Yamhill River basin. Our results demonstrate that prior judgment captures observed peak flow and flood volume within 5% tolerance in 10 and 11 out of 14 events, with 5-fold cross-validation over 129 events yielding Pearson correlations of 0.62 and 0.84. Building on a high-baseline scheme library (average KGE 0.890), the guided scheme selection further improves KGE by 0.023-0.154, with simulated peak flow and flood volume falling within the prior judgment ranges for 14 and 13 out of 14 events. All five tested LLMs successfully execute the HydroAgent workflow with comparable judgment accuracy (40%-80%), while showing moderate performance variation and substantial cost differences. HydroAgent does not aim to replace human forecasters; instead, it translates their tacit expertise into an auditable and reproducible workflow, streamlining analytical steps and supporting more informed decision-making. This skill-orchestrated paradigm demonstrates how explicit rule boundaries can guide language model reasoning to complement physically based simulation in next-generation flood forecasting.

## Metadata
- **Published**: 2026-07-27T04:18:36Z
- **Authors**: Qingyi Yang, Siqian Qiu, Bing Li, Xu Shan, Jia Feng, Shunan Zhou, Xudong Zhou, Tiantian Xing, Jiale Guo, Xiaoyi Dong, Gaoyu Liu, Xiaohuan Liu, Haiqing Pu, Qingwen Deng, Xun Zhang, Zhongrun Xiang, Haiyang Qian, Ying Yan, Yongkang Xu, Nuo Lei, Tianlong Jia, Baoying Shan, Carlo De Michele
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23983v1)