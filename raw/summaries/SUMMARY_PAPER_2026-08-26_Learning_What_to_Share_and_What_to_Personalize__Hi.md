---
title: Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory
url: http://arxiv.org/abs/2608.25329v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_03-24-52Z_LearningWhattoShareandWhattoPersonalize_Hierarchic.md
generated_at: 2026-08-26 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HiPS, a hierarchical strategy co-evolution framework that separates memory management into a universal foundation and a user‑specific adaptive tier. By integrating cross‑persona learning with personalized rule distillation, HiPS enables agents to retain only the most relevant information while discarding irrelevant data. The approach is validated through extensive experiments showing consistent improvements over existing memory‑augmented baselines.

## Key Takeaways
- Universal Strategy extracts shared principles from trajectories across multiple personas, providing a common set of rules that apply broadly.
- Persona Delta Distillation creates tailored rule sets for users whose behavior deviates from the general patterns learned by the universal strategy.
- Cross‑Level Rule Flow dynamically adjusts the boundary between global and personalized rules, promoting validated personal rules while demoting contradicted global ones.

## Context
Memory‑augmented agents aim to keep user profiles compact throughout long conversations, but most existing methods rely on static, one‑size‑fits‑all strategies that do not adapt to individual users. This limitation hampers the ability of agents to deliver truly personalized responses efficiently.

## Implications
The HiPS framework offers a scalable solution for conversational AI by reducing data overload and improving response relevance without sacrificing performance. Practitioners can leverage this approach to build more efficient, user‑centric systems that adapt in real time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25329v1)
