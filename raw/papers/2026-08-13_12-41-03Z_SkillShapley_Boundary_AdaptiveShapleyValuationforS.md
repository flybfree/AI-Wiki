---
title: SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents
published: 2026-08-13T12:41:03Z
authors: Chang Liu, Yuqi Zhang, Yiman Zhong, Boyi Liu, Hengjun Wang, Shuyue Wei
url: http://arxiv.org/abs/2608.13173v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents

## Abstract
Agent skills are crucial external instructions that enable language agents to execute long procedural tasks such as coding or document processing. Existing agent skills are primarily created through human manual crafting or agent execution traces, with limited understanding of how each step contributes to overall skill performance on specific tasks; i.e., there remains an open problem in quantifying the contribution of individual steps within an agent skill. To address this issue, we first model skill-step attribution as a Shapley value-based contribution estimation problem, and then propose SkillShapley, a step-level attribution framework for agent skills. Notably, SkillShapley operates in two phases, motivated by key empirical insights, i.e., discretized benchmark rewards that create sharp performance cliffs, and step interactions that are largely additive rather than synergistic. Specifically, it first identifies informative coalitional regions, and then adaptively samples new coalitions that can yield reusable marginal evidence. Experiments on skills from the widely adopted SkillsBench demonstrate that our SkillShapley can effectively and efficiently identify high- or low-value skill steps, providing several key takeaways for agent skill creation.

## Metadata
- **Published**: 2026-08-13T12:41:03Z
- **Authors**: Chang Liu, Yuqi Zhang, Yiman Zhong, Boyi Liu, Hengjun Wang, Shuyue Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13173v1)