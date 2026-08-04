---
title: Breaking Diversity Collapse in Spiking Pseudo-Ensembles for Efficient OOD Detection in Remote Sensing
url: http://arxiv.org/abs/2608.01090v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_08-44-25Z_BreakingDiversityCollapseinSpikingPseudo_Ensembles.md
generated_at: 2026-08-03 23:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an efficient spiking pseudo‑ensemble for out‑of‑distribution detection in remote‑sensing systems. By attaching lightweight classification heads to a frozen SNN backbone and training them with an agree‑disagree objective, the method recovers useful ensemble‑style uncertainty while drastically reducing parameter count and inference cost.

## Key Takeaways
- Naively trained multi‑head models suffer from diversity collapse because their predictions become correlated.  
- The agree‑disagree loss keeps correct in‑distribution predictions intact while promoting diverse outputs on structured input transformations without needing external OOD data.  
- Using three backbones with five heads each matches or improves a conventional five‑model deep ensemble, yet requires about 38 % fewer parameters and 40 % fewer backbone evaluations.

## Context
Remote sensing often relies on spiking neural networks because they are lightweight and energy‑efficient, but reliable out‑of‑distribution detection is essential for robust decision making. Deep ensembles provide high uncertainty estimates, yet their multiple full model evaluations make them impractical for edge deployment. This work demonstrates that explicit diversity mechanisms can substitute costly ensemble training.

## Implications
The approach enables edge devices to achieve ensemble‑level confidence with minimal compute and memory overhead, improving reliability in sensor data classification. Practitioners can adopt this method to enhance OOD robustness while keeping the system lightweight and cost‑effective.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01090v1)
