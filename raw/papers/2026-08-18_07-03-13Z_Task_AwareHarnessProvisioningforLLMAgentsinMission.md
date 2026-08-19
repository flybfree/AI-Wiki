---
title: Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations
published: 2026-08-18T07:03:13Z
authors: Liangtao Lin, Qingang Zhang, Zhaomeng Zhu, Tianwei Zhang, Yonggang Wen
url: http://arxiv.org/abs/2608.17433v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations

## Abstract
LLM agents have been widely adopted to operate mission-critical infrastructure (MCI). These agents normally rely on a harness that determines what information they can access, which tools they can use, and what actions they can take. Existing systems often expose the same comprehensive harness to every task, which may not be necessary and cause resource wastes. In this paper, we focus on the identification of optimal harness configurations, and view it as a resource-matching problem between what each task requires and what the harness provides. To measure this match, we classify MCI tasks based on the mathematical representation of the underlying system and rank harness configurations by the amount and type of information they provide. We then construct task-to-harness mappings from two sources: mining research literature and measuring controlled agent execution. Leveraging the measured mapping, we propose a new harness provisioning algorithm: map-guided escalation. It begins with a task-specific harness and expands to full provision only after a failed self-check. We evaluate our method in two representative MCI tasks: in liquid cooling, it improves the agent accuracy from 0.652 under full provision to 0.715 and achieves accuracy comparable to Reflexion with 48% fewer tokens; In power grids, full provision remains accuracy-optimal, while map-based provisioning offers lower-cost alternatives. These findings show that harness provisioning follows a domain-dependent accuracy-cost Pareto frontier rather than a universal optimum.

## Metadata
- **Published**: 2026-08-18T07:03:13Z
- **Authors**: Liangtao Lin, Qingang Zhang, Zhaomeng Zhu, Tianwei Zhang, Yonggang Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17433v1)