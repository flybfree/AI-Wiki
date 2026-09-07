---
title: Iris: Climbing to the Search Frontier
url: http://arxiv.org/abs/2609.04304v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_17-51-01Z_Iris_ClimbingtotheSearchFrontier.md
generated_at: 2026-09-06 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces two search agents named Iris-mini and Iris-pro, trained at the 35B‑A3B and 397B‑A17B scales respectively. The authors reverse‑construct multi‑hop questions from a web corpus’s hyperlink graph, rewriting non‑answer entities into descriptive references to prevent simple string matching, and then train a ReAct agent using supervised fine‑tuning followed by reinforcement learning against live search. Their results show the strongest performance among open‑source agents in their parameter ranges.

## Key Takeaways
- The models are trained on extremely large foundation models (35B‑A3B and 397B‑A17B) which enables them to handle complex, multi‑step reasoning tasks.  
- A custom data pipeline constructs answer trails by turning non‑answer entities into descriptive references, ensuring that no clue can be resolved without the supporting evidence.  
- The training alternates supervised fine‑tuning and reinforcement learning in a “SFT‑RL climbing” procedure, selecting the hardest solved rollouts for each supervised pass.

## Context
The rapid growth of open‑source language models has created a need to evaluate how well they can perform real‑world search tasks at scale. This work demonstrates that even with billions of parameters, careful data construction and iterative RL training can yield state‑of‑the‑art results on benchmark suites such as BrowseComp and DeepSearchQA.

## Implications
The findings suggest that scaling up models alone is insufficient; the quality of generated question trails and the balance between supervised and reinforcement learning stages are crucial. Practitioners should adopt similar pipelines to improve search agent performance, and sharing the full recipe could accelerate progress across the community.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04304v1)
