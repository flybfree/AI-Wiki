---
title: Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation
url: http://arxiv.org/abs/2608.19778v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_08-23-24Z_DistillingAggregateMobilityStatisticsintoaLanguage.md
generated_at: 2026-08-20 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a method for creating crowd simulation policies that match real pedestrian destination distributions using only aggregated zone counts and origin-to-destination flows. By fine‑tuning a language model to reproduce the observed fraction of people heading to each point of interest, the authors achieve a 25 % reduction in error compared with standard approaches while keeping grid correlation stable.

## Key Takeaways
- The fine‑tuned agent directly uses OD flow data to set its destination distribution, eliminating the need for inference‑time correction after training.  
- To avoid over‑representing dominant destinations during fine‑tuning, the authors resample trajectories with a low‑rank adapter that matches the corrected composition.  
- On mobile network counts from two baseball games the method cuts destination‑share error by 25 % without degrading spatial correlation across policies.

## Context
This work addresses a longstanding challenge in agent‑based simulation where privacy constraints prevent use of individual trajectories, forcing reliance on coarse aggregates that underestimate behavioural diversity. By leveraging language model fine‑tuning, the approach demonstrates how data‑driven adaptation can improve realism without violating privacy.

## Implications
Practitioners can adopt this technique to generate more accurate crowd models for urban planning, event management, and safety analysis using only publicly available aggregate counts. The method offers a scalable way to align simulation outputs with real‑world flows while respecting individual privacy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19778v1)
