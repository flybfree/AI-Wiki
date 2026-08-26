---
title: CAFE: Self-Improving Search Agents Need Co-Evolving Feedback
url: http://arxiv.org/abs/2608.24794v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_16-39-00Z_CAFE_Self_ImprovingSearchAgentsNeedCo_EvolvingFeed.md
generated_at: 2026-08-25 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAFE, a framework that couples an agent and its critic in a co‑evolving loop to improve self‑improving search agents. By alternating between online feedback shaping and offline preference optimization on matched rollouts, CAFE reduces hallucinations and outperforms existing RL‑based search agents across seven benchmarks.

## Key Takeaways
- The agent must decide when to request feedback while the critic infers corrections from outcome‑confounded trajectories that shift as the policy improves.  
- Online updates use a prompt‑level call‑skip success gap to shape retrieval returns, and advantage shaping reweights token advantages around feedback events. Offline preference optimization learns from matched successful and unsuccessful rollouts.  
- Alternating updates between agent and critic continues to improve performance, whereas improving only one component eventually plateaus.

## Context
Self‑improving agents require mechanisms that can correct intermediate errors before they compound, a challenge for outcome‑supervised search where terminal rewards are too coarse. CAFE addresses this by treating feedback as an in‑trajectory intervention that is learned jointly with the policy, aligning with broader efforts to make AI systems more robust and reliable.

## Implications
For practitioners developing autonomous agents, CAFE offers a practical way to integrate corrective feedback without sacrificing learning speed. The framework’s co‑evolution approach could be adapted to other domains where iterative improvement is critical, such as recommendation systems or code generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24794v1)
