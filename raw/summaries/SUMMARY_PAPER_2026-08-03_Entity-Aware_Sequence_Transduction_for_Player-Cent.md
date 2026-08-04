---
title: Entity-Aware Sequence Transduction for Player-Centric Ball Action Spotting
url: http://arxiv.org/abs/2608.01696v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_04-48-54Z_Entity_AwareSequenceTransductionforPlayer_CentricB.md
generated_at: 2026-08-03 23:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Multi-Entity Denoising Sequence Transduction which aims to improve player-centric ball action spotting by preserving the role-slot dimension in the model. It achieves a micro F1 of 0.778 on FOOTPASS, surpassing TAAD+DST by ten point three percent. The approach combines temporal and spatial attention with learnable embeddings.

## Key Takeaways
- ME-DST retains the role-slot axis throughout encoding which allows the model to capture each player’s unique temporal evolution separately from other players.
- Temporal attention models history of each role slot while spatial attention exchanges information across slots at every frame creating a factorized structure for within‑player versus inter‑player interactions.
- The inclusion of learnable role embeddings and tactical features derived from tracking yields higher accuracy than flattening the representation.

## Context
Current sports event detection systems often treat all players as a single entity, losing the inductive bias needed to model individual behaviors. This limits performance in crowded videos where player roles are crucial for accurate attribution. The proposed method addresses this by explicitly modeling entities within the sequence transduction pipeline.

## Implications
Explicit entity modeling can be applied to other sports and surveillance tasks requiring actor‑specific event recognition. Practitioners may integrate such architectures to improve real‑time analytics, reducing false positives in automated scouting tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01696v1)
