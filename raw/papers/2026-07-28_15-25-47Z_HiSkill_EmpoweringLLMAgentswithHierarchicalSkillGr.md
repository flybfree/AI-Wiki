---
title: HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs
published: 2026-07-28T15:25:47Z
authors: Yu Hao, Jinxuan Cai, Qi Zhang, Yawen Li, Zhiqiang Zhang, Chuan Shi, Cheng Yang
url: http://arxiv.org/abs/2607.25853v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs

## Abstract
Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks. However, existing trajectory-to-skill methods often produce flat collections of high-level textual skills that are stored and retrieved independently, leaving skill relations underutilized and maintaining a gap between high-level skills and executable actions. In this paper, we propose HiSkill, a hierarchical skill graph framework that organizes interaction trajectories into a directed graph with skill nodes, AtomicOp nodes, and typed edges. Specifically, the graph connects reusable high-level skills with executable action templates, while also capturing decomposition, temporal transition, compatibility, support, and recovery relations among them. At inference time, HiSkill retrieves a compact task-relevant subgraph and performs subgraph-guided task execution, where a symbolic task state, an active skill, and the retrieved subgraph guide the LLM agent to switch skills, select AtomicOps, and ground executable actions iteratively. Experiments on three interactive environments show that HiSkill outperforms state-of-the-art baselines while reducing inference token consumption, demonstrating the effectiveness of bridging high-level skills and executable action grounding through a hierarchical skill graph. Our data and code is available at https://github.com/BUPT-GAMMA/HiSkill.

## Metadata
- **Published**: 2026-07-28T15:25:47Z
- **Authors**: Yu Hao, Jinxuan Cai, Qi Zhang, Yawen Li, Zhiqiang Zhang, Chuan Shi, Cheng Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25853v1)