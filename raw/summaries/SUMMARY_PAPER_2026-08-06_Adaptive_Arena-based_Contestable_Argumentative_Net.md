---
title: Adaptive Arena-based Contestable Argumentative Network-of-Experts for Open-Ended Care Plan Coordination
url: http://arxiv.org/abs/2608.05391v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_20-18-45Z_AdaptiveArena_basedContestableArgumentativeNetwork.md
generated_at: 2026-08-06 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces CANOE, a contestable argumentative network‑of‑experts that synthesizes heterogeneous clinical, functional and psychosocial information for care plan coordination without relying on monolithic LLM pipelines. Evaluation shows medically fine‑tuned models achieve the highest clinical correctness while CANOE’s structured argumentation provides faithful explanations and human contestability.

## Key Takeaways  
- The complexity assessment module determines which expert agents are recruited based on the intricacy of the care plan, ensuring appropriate expertise is deployed.  
- Arena‑based clash resolution resolves conflicting arguments between supporting and attacking agents before acceptability scores propagate across the argumentation graph, preserving safety.  
- Human contestability allows care planners to accept, reject, edit or add arguments, leading to a deterministic recomputation of the final plan.

## Context  
Current AI approaches for healthcare often use single‑model pipelines that lack transparency and safety guarantees, making them unsuitable for complex interdisciplinary tasks such as care planning where multiple professional perspectives must be integrated.

## Implications  
This framework offers a transparent, contestable method for integrating diverse expert knowledge, thereby improving clinical decision‑making and trustworthiness in patient care coordination.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05391v1)
