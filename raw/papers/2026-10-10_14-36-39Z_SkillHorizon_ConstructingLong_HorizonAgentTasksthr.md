---
title: SkillHorizon: Constructing Long-Horizon Agent Tasks through Skill Composition
published: 2026-10-10T14:36:39Z
authors: Yuxuan Liu, Zhaochen Su, Hangyu Guo, Shijue Huang, Zhixiong Zhang, Kawai Chung, Zhongwei Xie, Tianshi Zheng, Wei Fan, Qing Zong, Haochen Shi, Baixuan Xu, Haoran Li, Yangqiu Song
url: http://arxiv.org/abs/2610.14966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillHorizon: Constructing Long-Horizon Agent Tasks through Skill Composition

## Abstract
Long-horizon agents must complete workflows in which later activities depend on earlier outputs and changes to shared state. A key challenge for evaluation is to expand task requirements and their dependencies while keeping tasks executable and outcomes verifiable. We introduce SkillHorizon, a benchmark that constructs long-horizon tasks through skill composition in seven business environments. Its generators use domain-specific rules to turn reusable skill procedures into concrete business activities. These activities are connected through input-output dependencies, shared resources, and state updates, allowing workload and coordination demands to grow together. Successful reference executions validate task feasibility and measure interaction workload, while programmatic evaluators assess local completion and whole-task success. We evaluate five language models on 1,050 tasks with reference interaction workloads ranging from 64K to 1M tokens. Across these scales, mean local-goal completion falls from 90.4% to 46.8%, as completed work fails to keep pace with growing requirements. At larger workloads, agents more often submit unsuccessful final answers with substantial work unfinished and tool-call allowance remaining. Trace analysis also identifies cases where scripts execute successfully but their outputs fail downstream business checks. SkillHorizon provides a configurable testbed for studying sustained progress, dependency coordination, and complete task delivery in growing workflows. Our code is available at https://github.com/KnowComp/SkillHorizon.

## Metadata
- **Published**: 2026-10-10T14:36:39Z
- **Authors**: Yuxuan Liu, Zhaochen Su, Hangyu Guo, Shijue Huang, Zhixiong Zhang, Kawai Chung, Zhongwei Xie, Tianshi Zheng, Wei Fan, Qing Zong, Haochen Shi, Baixuan Xu, Haoran Li, Yangqiu Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14966v1)