---
title: Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System
published: 2026-09-10T00:09:18Z
authors: Ming Li, Dai Li, Xuying Ning, Bo Sun, Rui Li, Yi Zhang, Silvia Gong, Xuan Cao, Rui Li, Cornelia Carapcea, Qunshu Zhang, Zhigang Wang, Yinglong Xia, Andy Wang
url: http://arxiv.org/abs/2609.10922v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender System

## Abstract
Auto-research agents have shown the potential to automate hypothesis generation, experiment execution, and iterative refinement. However, scaling this paradigm to industry-scale recommendation models introduces two challenges: (1) long feedback loops, where model training can take days, making serial iteration prohibitively slow and requiring parallel exploration across multiple research directions; and (2) system complexity, where large configurations, fragile infrastructure dependencies, and multi-day GPU jobs require robust and recoverable execution. We present Auto-RecSys, an autonomous research system for long-horizon experimentation on industry-scale recommendation models. Auto-RecSys addresses these challenges through three harness designs: (1) distributed asynchronous execution for running multiple experiments in parallel across servers, (2) centralized cross-server memory for persistent and recoverable execution across sessions and failures, and (3) cognitive-procedural separation, where natural-language skill files guide LLM reasoning while deterministic scripts enforce operational correctness. Auto-RecSys further employs a dual-loop self-evolving architecture: an Execution Evolution Loop in which model-specific playbooks accumulate operational knowledge by recording failed attempts and crystallizing successful pipelines, and an Idea Evolution Loop in which experimental outcomes inform subsequent ideation. Evaluated on recommendation models, Auto-RecSys significantly reduces the human time required per experiment cycle and improves execution reliability as its playbooks mature.

## Metadata
- **Published**: 2026-09-10T00:09:18Z
- **Authors**: Ming Li, Dai Li, Xuying Ning, Bo Sun, Rui Li, Yi Zhang, Silvia Gong, Xuan Cao, Rui Li, Cornelia Carapcea, Qunshu Zhang, Zhigang Wang, Yinglong Xia, Andy Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.10922v1)