---
title: Designing Reliable LLM-as-a-Judge Measurement Systems for Multi-Turn Business Agents
published: 2026-09-27T21:52:05Z
authors: Kaiwen Luo, Ming Gao
url: http://arxiv.org/abs/2609.33955v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Designing Reliable LLM-as-a-Judge Measurement Systems for Multi-Turn Business Agents

## Abstract
Many LLM-as-a-judge evaluations score fixed outputs under a fixed task definition. Production multi-turn business agents instead require a maintained measurement system: correctness depends on business-specific facts and procedures, outcomes emerge across turns, and failures must be attributed to either agent capability or missing business knowledge before they are actionable. We present an integrated methodology spanning evaluation specification, modular LLM judges, intent-preserving user simulation, and human-in-the-loop governance. The specification defines conversation-level end states and actionable failure ownership. Atomic judges share versioned evidence and feed an explicit aggregation graph. The simulator is released only after task-preservation and stability checks. Independent human audits estimate measurement fidelity, renew tiered reference sets, and route disagreements to label correction, guideline revision, or judge improvement. Production studies show that system-level fidelity improved across repeated audits, that human reviewers and automated judges improved together under the shared feedback loop, and that their combined workflow had the strongest descriptive performance in both reported task-completion settings. Because the studies are observational and the human reference itself required revision, these findings demonstrate operational usefulness rather than causal or universal superiority. The contribution is a practical framework for making multi-turn agent measurement reliable, actionable, and maintainable as the evaluated system and its evidence evolve.

## Metadata
- **Published**: 2026-09-27T21:52:05Z
- **Authors**: Kaiwen Luo, Ming Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33955v1)