---
title: EMIR$^2$: Evolution-Aware Memory with Intent-Guided Multi-Round Retrieval
published: 2026-09-26T12:58:06Z
authors: Jinlan Liu, Hongliang Sun, Yong Wang, Bolin Zhang, Dinabo Sui, Dianhui Chu, Zhiying Tu
url: http://arxiv.org/abs/2609.32584v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EMIR$^2$: Evolution-Aware Memory with Intent-Guided Multi-Round Retrieval

## Abstract
Long-term memory enables large language model (LLM) agents to leverage historical interactions for future tasks. However, existing memory systems struggle to utilize continuously evolving historical information, as they often rely on static memory representations and single-round retrieval strategies, failing to track factual changes or integrate distributed evidence across long-term interactions. To address these challenges, we propose \textsc{EMIR}$^{2}$, an \textbf{E}volution-Aware \textbf{M}emory framework with \textbf{I}ntent-Guided Multi-\textbf{R}ound \textbf{R}etrieval, enabling LLM agents to maintain evolving historical knowledge and adaptively retrieve relevant evidence. Specifically, \textsc{EMIR}$^{2}$ constructs a State-Evolving Memory Graph (SEMG) that represents long-term memory as evolving knowledge states supported by temporal event trajectories and evidential associations. By maintaining semantic states through evidence-based updates, SEMG preserves historical evolution and enables evidence tracing under complex and conflicting scenarios. Building upon this, we introduce an intent-guided multi-round retrieval mechanism that iteratively identifies missing evidence and expands retrieval based on accumulated information. Experiments on LoCoMo and MemConflict demonstrate that \textsc{EMIR}$^{2}$ improves long-term memory utilization, dynamic and static conflict handling, and complex retrieval performance, achieving relative improvements of more than 12\% in certain categories. These results highlight the effectiveness of jointly modeling memory evolution and adaptive evidence acquisition for long-term agent interactions.

## Metadata
- **Published**: 2026-09-26T12:58:06Z
- **Authors**: Jinlan Liu, Hongliang Sun, Yong Wang, Bolin Zhang, Dinabo Sui, Dianhui Chu, Zhiying Tu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32584v1)