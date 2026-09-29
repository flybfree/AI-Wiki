---
title: ARSM: Auto-Regressive State Machine for Agentic Reasoning Compression
published: 2026-09-26T18:26:49Z
authors: Xiafeng Man, Siyuan Ye, Xiaosong Ma
url: http://arxiv.org/abs/2609.32852v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ARSM: Auto-Regressive State Machine for Agentic Reasoning Compression

## Abstract
While Large Language Model (LLM)-based agents demonstrate strong capabilities in long-horizon tasks by interleaving reasoning with external environment interactions, the continuous accumulation of context rapidly creates a critical memory bottleneck. Existing memory compression methods rely on task-specific optimization or external auxiliary models, introducing significant computational overhead. Furthermore, the resulting compressed representations tend to lose structured relationships, leading to information dilution, attention collapse, and degraded decision consistency.   To address these limitations, we propose Auto-Regressive State Machine (ARSM), a lightweight training-free framework that enables in-situ reasoning compression through structured state evolution. ARSM introduces two key components: (i) a trajectory abstraction mechanism that reorganizes interaction histories into compact Hypothesis-Action-Result (HAR) micro-chains; (ii) a dynamic state machine that regulates hierarchical memory through atomic operations and a compression-control parameter. These components are unified within an auto-regressive, self-compressive generation space, where each model output jointly performs external action execution and internal state updates.   We evaluate ARSM on Webshop, Multi-Objective Multi-Hop QA, and SWE-Bench Lite datasets. Experimental results show that ARSM maintains the task performance while simultaneously reducing token consumption, offering a practical, cost-effective route toward scalable autonomous agents for long-horizon tasks.

## Metadata
- **Published**: 2026-09-26T18:26:49Z
- **Authors**: Xiafeng Man, Siyuan Ye, Xiaosong Ma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32852v1)