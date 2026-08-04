---
title: Progressive Agent Skill Generation via Reinforcement Learning
published: 2026-08-03T04:14:59Z
authors: Junhao Shen, Zhanqiu Zhang, Yiwen Guo, Hong Cheng
url: http://arxiv.org/abs/2608.01678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Progressive Agent Skill Generation via Reinforcement Learning

## Abstract
Existing skill generation methods largely rely on heuristics or pipeline-style consolidation, which must be specially designed for different evidence sources. In contrast, learning-based approaches offer a more unified way to model skill generation across heterogeneous sources. However, learning-based skill generation remains challenging because skills lack a natural supervision signal based on relevance or correctness; their value can largely be determined only by whether they improve the behavior of the agent on downstream tasks. To address this challenge, we propose Skill-$α$, a reinforcement learning method for progressively generating high-quality agent skills. Specifically, we formulate skill generation as a sequential editing process that decomposes skill construction into individually evaluable edits, and introduce a novel rollback reward that evaluates each edit by comparing downstream execution under the original and edited skills on an anchored query. Extensive experiments show that Skill-$α$ generates more effective skills than methods based on heuristics or pipelines in both document-to-skill and experience-to-skill settings. Under the main GPT-4o worker, Skill-$α$ improves average downstream success rates over the strongest skill-generation baseline by 3.3 points on CL-Bench and 6.7 points on tau2-bench. Further ablations validate the importance of rollback reward and progressive generation.

## Metadata
- **Published**: 2026-08-03T04:14:59Z
- **Authors**: Junhao Shen, Zhanqiu Zhang, Yiwen Guo, Hong Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01678v1)