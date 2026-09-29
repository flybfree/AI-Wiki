---
title: COUNTERMEM: World-Model Verified Counter-Factual Memory for Language Agents
published: 2026-09-25T18:12:38Z
authors: Hongji Pu, Ruixiang Tang, Yongfeng Zhang
url: http://arxiv.org/abs/2609.31874v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# COUNTERMEM: World-Model Verified Counter-Factual Memory for Language Agents

## Abstract
Existing agent memory frameworks mainly create memory through an agent's interaction with the factual world, e.g., remembering feedback from actions taken to improve performance on future tasks. However, these frameworks seldom ask the "what if" question during memory construction: what if a different action had been taken, would the feedback have changed, and how could this feedback become useful memory? Obtaining such feedback directly in an active environment can be expensive and can alter the state needed for comparison. In this work, we introduce COUNTERMEM, a reinforcement-learning framework for constructing and using verified counterfactual memory across tasks. After a failed action, COUNTERMEM evaluates local alternatives from a copy or reset of the original state using executable world models, such as tests, proof checkers, and solvers. It stores improvements with the original and corrected actions, checked outcomes, and conditions for reuse. A learned memory-use policy selects a retrieved record or skips memory to balance task success and interaction cost, while the base LLM remains fixed. Both memory and policy are frozen during held-out evaluation. We evaluate COUNTERMEM on 12 benchmark settings across six domains. With gpt-oss-120b, COUNTERMEM improves both ReAct and Reflexion on all 12 benchmarks across six domains, averaging a gain of 12.6 percentage points over their unaugmented versions. In the four-domain comparison across two backbones, task-run tokens decrease by 7.7-42.0%, excluding offline selector-training costs. Further analyses show that removing verification or persistent storage weakens the gains, while applying verified corrections to unsuitable decisions can reverse them. Code will be released upon acceptance.

## Metadata
- **Published**: 2026-09-25T18:12:38Z
- **Authors**: Hongji Pu, Ruixiang Tang, Yongfeng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31874v1)