---
title: SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time
published: 2026-08-07T07:05:53Z
authors: Qinfeng Li, Dalin He, Yuntai Bao, Ying Yang, Ruoxi Chen, Xinyan Yu, Lizhou Liang, Ge Su, Wenqi Zhang, Xuhong Zhang
url: http://arxiv.org/abs/2608.06880v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time

## Abstract
General-purpose skills promise reusable procedural knowledge for language agents, yet semantic relevance does not guarantee execution utility: a retrieved skill may encode assumptions that conflict with the current task, execution environment, or other retrieved skills. We formalize this problem as the skill--execution misfit. To address it, we propose SkillAligner, a training-free execution-time skill adaptation framework that treats retrieved skills as adaptable drafts rather than fixed instructions. Before execution, SkillAligner performs a one-time joint adaptation that specializes useful skill fragments to task requirements, aligns their procedural assumptions with the available execution interface, and composes the resulting guidance by resolving dependencies, conflicts, and redundancy across skills. The adapted content is consolidated into a compact execution guide and reused throughout the subsequent trajectory. Extensive experiments across diverse agent benchmarks and model backbones show that SkillAligner substantially improves task performance over existing skill-use baselines, reduces skill-induced regressions at the instance level, and lowers total inference cost.

## Metadata
- **Published**: 2026-08-07T07:05:53Z
- **Authors**: Qinfeng Li, Dalin He, Yuntai Bao, Ying Yang, Ruoxi Chen, Xinyan Yu, Lizhou Liang, Ge Su, Wenqi Zhang, Xuhong Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06880v1)