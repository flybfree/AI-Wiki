---
title: Cost-Effective Repository Exploration for Agentic Issue Localization
published: 2026-08-30T09:16:33Z
authors: Mohammad Nour Al Awad, Sergey Ivanov
url: http://arxiv.org/abs/2608.29675v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cost-Effective Repository Exploration for Agentic Issue Localization

## Abstract
Repository exploration is a distinct and costly stage of coding-agent pipelines: before generating a patch, an agent must identify which repository files are likely to matter. We study whether this stage can be delegated to lower-cost models while retaining useful localization quality. Using our IssueLoc-Bench, we evaluate five explorer models under the same read-only interactive interface on 499 SWE-bench Verified-derived tasks and 500 tasks from 153 additional repositories. We measure early candidate discovery, top-three gold-file coverage, strict file-set recovery, agent time, and token usage, with paired instance-level uncertainty and repository-clustered sensitivity analysis. The highest-quality explorer leads across localization metrics, but substantially cheaper operating points emerge: depending on the model and evaluation arm, lower-cost explorers retain approximately 78-94% of the reference Hit@3 and 73-92% of its F1 while reducing mean agent time by 41-88% and token usage by 84-95%. The preferred operating point depends on how localization is consumed downstream: ranking and coverage metrics characterize recoverable candidate handoffs, whereas F1 and exact match characterize restrictive file gates. These results support treating repository exploration as an independently measurable and budgetable stage of modular coding agents, with explorer selection guided by the downstream handoff contract.

## Metadata
- **Published**: 2026-08-30T09:16:33Z
- **Authors**: Mohammad Nour Al Awad, Sergey Ivanov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29675v1)