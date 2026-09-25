---
title: Breaking the Environment Wall: Evolving LLM Agent Environments for Recursive Self-Improvement
published: 2026-09-24T13:17:57Z
authors: Yukai Wu, Yuanjing Yang, Le Zhou, Shaokun Han, Haoyu Wang, Zirui Tang, Weihuang Zheng, Maxm Pan, Xuanhe Zhou, Fan Wu
url: http://arxiv.org/abs/2609.29773v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breaking the Environment Wall: Evolving LLM Agent Environments for Recursive Self-Improvement

## Abstract
Many real-world tasks (e.g., office workflows, scientific experimentation) require LLM agents to interact repeatedly with their environments for context-dependent operations. However, such environments are often not agent-ready. First, information is often scattered and fragmented across the environment. Second, relevant evidence in the environment is often mixed with misleading information and conflicting versions. Third, environments evolve over time, introducing new noise and more challenging tasks. These challenges can substantially degrade performance for state-of-the-art AI agents (e.g., from 83.9% to 57.6%). To address these challenges, we propose Env-Rethink (a system with 27B post-trained model) that supports three main capabilities: (1) It adaptively builds Collection Maps (for organizing related files) and Event Logs (for contextualizing cross-data relationships) to supplement necessary context; (2) It further leverages the post-trained model (through offline trajectory learning) to identify underlying noise issues in the environment; (3) It ultimately evolves environments through virtual event histories that alter environmental states and evidence relationships, producing more tricky ones for further agent improvement. Experiments show that Env-Rethink can effectively improve downstream task performance (with over 15.1% rubric pass rate improvement across nine models on 30 tasks).

## Metadata
- **Published**: 2026-09-24T13:17:57Z
- **Authors**: Yukai Wu, Yuanjing Yang, Le Zhou, Shaokun Han, Haoyu Wang, Zirui Tang, Weihuang Zheng, Maxm Pan, Xuanhe Zhou, Fan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.29773v1)