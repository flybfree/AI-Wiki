---
title: SynWeaver: Website-Prior Task and Trajectory Co-Synthesis for Web Agents
url: http://arxiv.org/abs/2608.12429v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_12-03-20Z_SynWeaver_Website_PriorTaskandTrajectoryCo_Synthes.md
generated_at: 2026-08-13 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
SynWeaver addresses the limitation of website-prior task and trajectory co-synthesis by constructing a structured website map that captures functional page states and interactions. The framework trains a UI‑aware model with website‑specific priors to generate grounded tasks, then collaboratively updates task and execution trajectories while repairing inconsistencies. Experiments on WebArena and WebVoyager show SynWeaver outperforms baselines and provides more effective supervision for both in‑domain and out‑of-domain generalization.

## Key Takeaways
- The website map covers a broad set of functionally distinct page states and executable interactions, providing structured supervision that reduces hallucinated tasks. 
- Deriving page‑level and transition‑level supervision from the map enables a UI‑aware model to propose grounded tasks aligned with actual functionality. 
- Joint updating of task and trajectory while repairing inconsistencies ensures collected results are executable and semantically aligned.

## Context
Automation agents often rely on generic or manually annotated data, leading to poor generalization when encountering new websites. This paper contributes a method that leverages website‑specific exploration to create high‑quality supervision without manual labeling, advancing the field of web‑agent autonomy.

## Implications
For practitioners developing autonomous browsing tools, SynWeaver offers a scalable way to generate reliable task‑trajectory pairs, reducing reliance on costly human annotation. In industry, this can lead to more robust and adaptable web agents that perform well across diverse sites without extensive retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12429v1)
