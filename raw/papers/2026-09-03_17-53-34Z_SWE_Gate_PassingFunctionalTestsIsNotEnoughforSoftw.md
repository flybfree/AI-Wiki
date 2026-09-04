---
title: SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents
published: 2026-09-03T17:53:34Z
authors: Xin He, Yanlin Wang, Mingwei Liu, Jiachi Chen, Hongyu Zhang, Guanbin Li
url: http://arxiv.org/abs/2609.04167v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents

## Abstract
Repository-level software engineering benchmarks have significantly advanced the evaluation of coding agents, but existing benchmarks primarily measure whether generated patches pass functional tests and overlook review-derived acceptance constraints (review constraints) that often influence whether a patch is acceptable in real-world software development. We introduce SWE-Gate, a repository-level benchmark for software engineering agents that explicitly evaluates review constraint compliance alongside functional correctness. SWE-Gate derives review constraints from real pull request review comments and synthesizes repository-level repair instances around these constraints. Each instance provides separate functional and constraint tests, together with non-compliant and gold patches, enabling explicit separation between issue resolution capability and review constraint compliance. We construct SWE-Gate with 303 repository-level repair instances spanning 75 open-source Python repositories across diverse software domains. Experiments with four LLM backends spanning different capability levels under a common coding-agent scaffold reveal a substantial gap between functional success and success under the complete repair specification: among 644 repairs that pass the functional tests, 221 fail to satisfy the provided review constraints. These findings show that functional-only evaluation overestimates agents' ability to satisfy the full requirements of repository-level repair tasks. The replication package including code, data, and experimental results is available at https://github.com/DeepSoftwareAnalytics/SWE-Gate.

## Metadata
- **Published**: 2026-09-03T17:53:34Z
- **Authors**: Xin He, Yanlin Wang, Mingwei Liu, Jiachi Chen, Hongyu Zhang, Guanbin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04167v1)