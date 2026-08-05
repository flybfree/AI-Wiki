---
title: "Summary: TSN-Affinity: Similarity-Driven Parameter Reuse for Continual Offline Reinforcement Learning"
date: 2026-04-28
tags: ['paper', 'research', 'ai']
---
# Summary: TSN-Affinity: Similarity-Driven Parameter Reuse for Continual Offline Reinforcement Learning


**Source**: [Original Paper](http://arxiv.org/abs/2604.25898v1)
Saved: 2026-05-08 03:29
Source: 2026-04-28_17-41-04Z_TSN_Affinity_Similarity_DrivenParameterReuseforCon.md

---

## Summary
Introduces TSN-Affinity, a continual offline reinforcement learning method that uses TinySubNetworks and Decision Transformer with similarity- and action-compatibility-based routing for task-specific parameter reuse. On Atari and Panda manipulation benchmarks, it preserves prior tasks and improves multi-task performance, offering a replay-free alternative.

## Semantic links
- [[concepts/papers/2026-06-18_17-50-10Z_Multi_TaskBayesianIn_ContextLearning_summary.md|Summary: 2026-06-18_17-50-10Z_Multi_TaskBayesianIn_ContextLearning.md]] — 2 title terms overlap; shared tags: ai, paper, research; 9 summary/topic terms overlap
- [[concepts/papers/2026-06-17_17-54-32Z_UBP2_Uncertainty_BalancedPreferencePlanning_summary.md|Summary: 2026-06-17_17-54-32Z_UBP2_Uncertainty_BalancedPreferencePlanningforEffi.md]] — 1 title term overlap; shared tags: ai, paper, research; 11 summary/topic terms overlap
- [[concepts/papers/2026-06-10_17-59-35Z_FACTR2_LearningExternalForceSensingforCommo_summary.md|Summary: 2026-06-10_17-59-35Z_FACTR2_LearningExternalForceSensingforCommodityRob.md]] — 1 title term overlap; shared tags: ai, paper, research; 8 summary/topic terms overlap

## Key Takeaways
- Combines architectural reuse with RL-aware task routing.
- Targets continual offline RL where replay is costly or mismatched.
- Shows strong retention on both discrete and continuous-control benchmarks.

## Context
The paper tackles continual learning in offline RL, where adapting without live interaction is hard.

## Implications
Similarity-guided parameter reuse may be a viable alternative to replay-based CORL methods.

## Original Reference
- Title: TSN-Affinity: Similarity-Driven Parameter Reuse for Continual Offline Reinforcement Learning
- Authors: Dominik Żurek, Kamil Faber, Marcin Pietron, Paweł Gajewski, Roberto Corizzo
- Published: 2026-04-28T17:41:04Z
- URL: http://arxiv.org/abs/2604.25898v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-04-28_17-41-04Z_TSN_Affinity_Similarity_DrivenParameterReuseforCon.md

## Related Concepts

- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/search-retrieval/search-retrieval-hub.md|Search Retrieval Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]
