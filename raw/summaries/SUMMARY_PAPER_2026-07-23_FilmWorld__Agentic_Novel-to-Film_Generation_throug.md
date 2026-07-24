---
title: FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling
url: http://arxiv.org/abs/2607.19038v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_12-28-58Z_FilmWorld_AgenticNovel_to_FilmGenerationthroughDyn.md
generated_at: 2026-07-23 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FilmWorld, an agentic system that generates full films from novels by modeling a dynamic cinematic world in two phases: construction and evolution. Experiments show it outperforms state-of-the-art video generation agents on long-form narrative fidelity and cross-scene consistency.

## Key Takeaways
- Construction agents translate abstract literary prose into concrete, persistent world entities with visual anchors, enabling structured shot planning across scenes.
- Evolution agents propagate dynamic state updates between shots while verifying causal consistency to maintain film coherence.
- The evaluation framework FilmEval provides a difficulty‑graded benchmark and nine objective metrics covering cinematic presentation, consistency, and fidelity.

## Context
Long‑form video generation remains limited by models that produce only short clips within narrow contexts. This work addresses the gap by treating narrative generation as a persistent world modeling problem, aligning AI with storytelling complexity.

## Implications
FilmWorld offers a scalable approach for novel‑to‑film conversion, potentially reducing reliance on manual script breakdowns and enabling automated cinematic production pipelines. Practitioners can leverage its agentic workflow to integrate literary content into high‑quality video outputs efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19038v1)
