---
title: CoSec: Benchmarking Agent Security in Communities
published: 2026-09-28T10:00:05Z
authors: Hao Chen, Wenhui Dong, Ye Chen, Jiezhi Yao, Chenbo Xia, Yuwen Qu, Renxiang Wang, Fudong Yuan, Camil Hamami, Chenglong Pan, Xinquan Yue, Ziyu Wang, Fengyu Ye, Chenyang Si, Caifeng Shan
url: http://arxiv.org/abs/2609.34790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoSec: Benchmarking Agent Security in Communities

## Abstract
LLM agents operate in persistent collaborative environments involving multiple users, communities, memories, files, and tools. Community boundaries may remain fixed or evolve with changes in membership, roles, composition, and relationships. Agents must complete legitimate tasks and prevent unauthorized disclosure of protected information. Existing evaluations do not fully examine these risks in agent systems. We introduce \textbf{CoSec}, an executable benchmark for evaluating privacy and authorization enforcement in LLM agent systems operating within and across communities. CoSec contains 208 canonical scenarios spanning fixed and evolving boundaries, protected information belonging to the agent owner or other participants, and attacks through dialogue, environmental content, persistent memory, and composed workflows. CoSec executes complete agent systems with persistent sessions, memory, files and tools. It verifies information flows against the active authorization state using execution traces and artifacts. Across harness and model configurations, agents frequently complete benign tasks but violate privacy and authorization boundaries. Privacy behavior varies across harnesses, attack surfaces, and community states, revealing how memory, files, tools, and workflows can carry protected information beyond its authorized scope. These findings show that task utility does not imply privacy or authorization compliance and that authorization in community settings remains an unresolved security challenge for persistent LLM agents.

## Metadata
- **Published**: 2026-09-28T10:00:05Z
- **Authors**: Hao Chen, Wenhui Dong, Ye Chen, Jiezhi Yao, Chenbo Xia, Yuwen Qu, Renxiang Wang, Fudong Yuan, Camil Hamami, Chenglong Pan, Xinquan Yue, Ziyu Wang, Fengyu Ye, Chenyang Si, Caifeng Shan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34790v1)