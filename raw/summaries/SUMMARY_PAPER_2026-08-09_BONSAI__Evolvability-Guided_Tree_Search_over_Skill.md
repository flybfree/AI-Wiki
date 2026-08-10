---
title: BONSAI: Evolvability-Guided Tree Search over Skills
url: http://arxiv.org/abs/2608.07056v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_10-04-52Z_BONSAI_Evolvability_GuidedTreeSearchoverSkills.md
generated_at: 2026-08-09 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
BONSAI is a novel skill‑optimization framework that steers the search for high‑scoring natural‑language documents using evolvability rather than blind score improvement. The method grows skills as a Monte Carlo tree where each child is a mutation of its parent, and it replaces the single best scoring document found with an accept‑better loop. This approach lifts heldout accuracy by 2313 points over a skillfree agent on three benchmarks.

## Key Takeaways
- BONSAI uses evolvability to guide a search tree that focuses on regions of documentspace capable of producing viable variation under further mutation.  
- The mean score recorded beneath a node estimates the neighbourhood’s evolvability at no extra cost, allowing the selection rule to concentrate budget on improving areas.  
- BONSAI replaces the traditional accept‑better loop with an evolvability‑aware rule and achieves a 2313‑point gain in heldout accuracy.

## Context
BONSAI addresses the challenge of optimizing frozen agents that rely solely on prose skills, where standard score‑based optimization is blind to overfitting. The framework aligns with biological principles of adaptability, offering a principled way to balance exploitation and exploration in text generation tasks.

## Implications
For industry practitioners, BONSAI demonstrates that evolvability‑guided search can significantly boost model performance without additional compute beyond the accept‑better loop. This opens avenues for more robust skill design and efficient training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07056v1)
