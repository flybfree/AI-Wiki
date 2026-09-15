---
title: GeoSkill:Experience-Driven Hierarchical Skill Learning with Collaborative Revision forGeospatialAgents
published: 2026-09-12T02:50:52Z
authors: Han Luo, Xian Xu, Yinhe Liu, Yanfei Zhong
url: http://arxiv.org/abs/2609.13667v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GeoSkill:Experience-Driven Hierarchical Skill Learning with Collaborative Revision forGeospatialAgents

## Abstract
Geospatial agents are increasingly expected to support recurring and evolving analytical tasks rather than execute isolated workflows. In such settings, effective agents must distill prior execution experience into reusable geospatial procedural knowledge to guide future planning and tool use. However, existing memory-augmented paradigms struggle to summarize both long-horizon tool-chain orchestration experience and tool-level invocation constraints in geospatial analysis, while directly relying on LLM self-reflection to update experience often leads to misattribution and unreliable revisions. To address these challenges, we propose GeoSkill, an experience-driven hierarchical skill learning framework for geospatial agents. GeoSkill comprises two core components: (i) a Hierarchical Skill Bank (HSB), consisting of a Planning Skill Bank and a Tool Skill Bank, which respectively distill high-level task-planning experience and tool usage constraints, enabling structured representation and cross-task reuse of historical execution experience; and (ii) a Collaborative Trace-driven Skill Revision (CTSR) mechanism, where Judge, Critic, and Refiner collaboratively perform error identification, skill-level defect localization, and targeted modification, preventing misattributed and unreliable revisions from polluting the skill bank. GeoSkill learns and validates skills from historical executions during development, and freezes the skill bank for retrieval-only guidance on unseen tasks during deployment. Extensive experiments on EarthBench and ThinkGeo demonstrate that GeoSkill effectively transforms historical execution experience into reusable hierarchical skills, improving both end-to-end task accuracy and tool-execution reliability in geospatial tasks.

## Metadata
- **Published**: 2026-09-12T02:50:52Z
- **Authors**: Han Luo, Xian Xu, Yinhe Liu, Yanfei Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13667v1)