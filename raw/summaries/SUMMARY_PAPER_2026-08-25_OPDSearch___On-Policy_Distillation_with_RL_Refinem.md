---
title: OPDSearch+: On-Policy Distillation with RL Refinement for Search-Augmented Reasoning
url: http://arxiv.org/abs/2608.24310v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_09-39-16Z_OPDSearch__On_PolicyDistillationwithRLRefinementfo.md
generated_at: 2026-08-25 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces OPDSearch+, a distillation method that enables small language models to perform search‑augmented reasoning without fine‑tuning a task‑specific teacher. The approach first transfers knowledge from an off‑the‑shelf instruct model through a per‑position forward KL objective and then refines the distilled student with reinforcement learning, achieving performance gains that pure RL cannot reach.

## Key Takeaways
- OPDSearch+ eliminates the need for expensive task‑specific teacher fine‑tuning by using a frozen off‑the‑shelf instructor as the teacher.  
- The per‑position forward KL objective transfers reasoning decomposition and evidence integration skills directly to the student’s policy distribution.  
- Subsequent RL refinement leverages this richer behavioral foundation, producing results that exceed those of any 3B‑parameter RL baseline.

## Context
Search‑augmented reasoning remains a bottleneck for small language models because it relies on dynamic retrieval systems whose responses vary across interactions. Traditional on‑policy distillation struggles with high data costs and task specificity, limiting its scalability. This work demonstrates that leveraging an existing teacher can reshape the student’s policy in ways that pure RL cannot achieve.

## Implications
For practitioners, OPDSearch+ offers a cost‑effective pathway to improve reasoning capabilities without large fine‑tuning budgets or extensive search data collection. In industry, it could enable rapid deployment of search‑enhanced assistants across diverse domains where upfront task tuning is impractical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24310v1)
