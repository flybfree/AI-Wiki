---
title: Triplet2Track: A Hierarchical System with Object-Centric Representations for Reliable Long-Horizon Manipulation
url: http://arxiv.org/abs/2608.22800v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_04-46-25Z_Triplet2Track_AHierarchicalSystemwithObject_Centri.md
generated_at: 2026-08-24 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Triplet-to-Track System (TTS), a hierarchical closed-loop imitation learning framework that uses human-generated videos to ground high-level subgoals as object-centric triplets, translates them into continuous track priors for robot execution, and monitors progress online for replanning. Across real-world long-horizon tasks it achieves an average success rate of 74.8% while supporting object-level and compositional generalization.

## Key Takeaways
- TTS represents high‑level subgoals as instance‑grounded triplets that tie abstract goals to specific objects, reducing reliance on robot‑collected data.
- The system translates these triplets into continuous track priors for low‑level actions, enabling online replanning based on real observations.
- It achieves a 74.8% average success rate across diverse long‑horizon tasks and demonstrates object‑level and compositional generalization.

## Context
Long‑horizon robotic manipulation suffers from open‑loop failures because hierarchical plans lack grounding in low‑level actions and cannot incorporate online feedback, leading to hallucinations and data‑intensive end‑to‑end models. This work addresses those limitations by proposing a closed‑loop pipeline that leverages human demonstrations.

## Implications
The approach offers practitioners a more interpretable and reliable method for long‑horizon manipulation without massive training data, which could lower deployment costs in industrial settings. It also advances the field toward object‑centric representations that improve generalization across tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22800v1)
