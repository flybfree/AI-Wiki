---
title: LM-GRASP: Instance-Specific Language Models for Combinatorial Construction via Online Imitation Learning
url: http://arxiv.org/abs/2607.28135v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_12-45-18Z_LM_GRASP_Instance_SpecificLanguageModelsforCombina.md
generated_at: 2026-07-30 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LM-GRASP, a metaheuristic that treats the randomized constructive phase of GRASP as an online imitation learning task. It replaces static heuristic rules with a decoder‑only Transformer trained from scratch on each instance using elite trajectories discovered during local search. Evaluated on Taillard PFSP block ta51‑ta60, LM-GRASP beats GPU‑GRASP by 28.4 makespan units on average.

## Key Takeaways
- LM‑GRASP trains a Transformer policy online via behavioral cloning without any offline pretraining or problem‑specific feature engineering.  
- The local search acts as an expert oracle, providing high‑quality solutions that the model learns to emulate in real time.  
- On the benchmark block with half unknown optima, LM‑GRASP outperforms GPU‑accelerated GRASP by 28.4 makespan units, comparable to the speedup from parallel execution.

## Context
Current combinatorial optimization often relies on large offline pretrained neural constructors that consume significant compute and generalize poorly across problem instances. This work proposes an instance‑specific alternative that learns directly from the search process, reducing reliance on external data and static heuristics.

## Implications
The approach offers a practical path for practitioners needing fast, adaptable construction methods in resource‑constrained settings. By training models per instance, it could become standard in automated planning and scheduling where offline pretraining is impractical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28135v1)
