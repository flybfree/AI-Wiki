---
title: SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents
published: 2026-10-19T08:46:15Z
authors: Ran Zhou, Zehui Kong, Fanyu Lin, Jiaheng Liu, Zhen Zhang, Yuxiang Ren
url: http://arxiv.org/abs/2610.26995v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPEM: Structure-Aware Procedural Memory for Efficient Skill Use in LLM Agents

## Abstract
LLM-based agents increasingly rely on reusable skills. However, scaling skill libraries makes efficient and accurate skill use difficult. Full skill loading incurs high token and runtime overhead. In contrast, flat semantic retrieval treats skills as independent text entries, ignoring dependencies, execution order, state transitions, and data flow constraints. We propose SPEM, a lightweight structure-aware procedural memory framework for efficient skill use in LLM-based agents. SPEM maintains Atomic Skill Memory for individual skills and Skill-DAG Memory for reusable compositions derived from successful executions. For a new task, SPEM reuses high-confidence Skill-DAG templates when available. Otherwise, it retrieves atomic skills and invokes Skill-GNN for state- and structure-aware skill selection. Successful executions are written back as new Skill-DAGs, allowing procedural memory to accumulate over time. Experiments on ALFWorld and SkillsBench show that SPEM achieves the best overall effectiveness--efficiency trade-off, reaching 87.1% ALFWorld success and 38.38% SkillsBench reward while reducing token and runtime costs against strong baselines.

## Metadata
- **Published**: 2026-10-19T08:46:15Z
- **Authors**: Ran Zhou, Zehui Kong, Fanyu Lin, Jiaheng Liu, Zhen Zhang, Yuxiang Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26995v1)