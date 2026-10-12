---
title: Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction
published: 2026-10-09T04:32:02Z
authors: Yuqi Huang, Hui Li, Yifei Cao, Zikun Cai, Tianci Xie, Yangfan Gao, Pinxue Guo, Chaoyun Zhang, Bingxuan Li, Rui Zheng, Hang Yan, Ning Liao
url: http://arxiv.org/abs/2610.12984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction

## Abstract
Computer-use agents can perform increasingly complex GUI tasks, yet unfamiliar software and workflows requiring human domain knowledge remain challenging. Human demonstrations convey procedural knowledge through the same GUI interaction space, but reuse requires interpreting actions in context and separating workflow rules from task-specific details. We thus introduce Work2Skill, a framework that captures human GUI experience for reusable agent skill induction. WorkRecorder provides the framework's infrastructure for collecting this experience, aligning screen recordings, mouse and keyboard events, and available accessibility-tree information. Using WorkRecorder, we construct WorkDemo-350, the first synchronized multimodal dataset of human desktop GUI demonstrations for reusable agent skill induction and downstream evaluation. Its 350 demonstrations are screened for completeness and task success. We then propose an agentic skill-induction method that inspects evidence on demand to produce reusable skills capturing workflow rules, step dependencies, and completion checks. When the same four execution models are equipped with skills induced by each method under shared execution settings, Work2Skill achieves the highest scores and success rates. Mean score improvements over the corresponding No Skill baseline are 4.67--10.54 points on MyPCBench Bounded Action and 3.11--7.50 points on a 286-task subset of OSWorld-Verified. Our code and data are available at https://github.com/china-qijizhifeng/Work2Skill.

## Metadata
- **Published**: 2026-10-09T04:32:02Z
- **Authors**: Yuqi Huang, Hui Li, Yifei Cao, Zikun Cai, Tianci Xie, Yangfan Gao, Pinxue Guo, Chaoyun Zhang, Bingxuan Li, Rui Zheng, Hang Yan, Ning Liao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12984v1)