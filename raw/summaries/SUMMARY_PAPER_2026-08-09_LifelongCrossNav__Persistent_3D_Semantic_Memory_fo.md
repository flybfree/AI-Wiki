---
title: LifelongCrossNav: Persistent 3D Semantic Memory for Cross-Floor Multi-Object Navigation
url: http://arxiv.org/abs/2608.07079v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_10-31-20Z_LifelongCrossNav_Persistent3DSemanticMemoryforCros.md
generated_at: 2026-08-09 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
LifelongCrossNav introduces a persistent 3D semantic memory that stores scene information across floor transitions for multi‑object navigation. The framework outperforms planar baselines on the HM3D-MFMON benchmark, showing improved recall and traversal.

## Key Takeaways
- The model maintains a shared sparse 3D semantic voxel memory that accumulates geometry, traversability, and vision‑language features throughout an episode, enabling later queries to retrieve scene information without rebuilding the map.
- It integrates support‑aware 3D mapping with stair perception to enable reliable cross‑floor movement without rebuilding the map.
- A unified navigation policy coordinates same‑floor exploration, historical point‑of‑interest retrieval, stair navigation, and target object approach.

## Context
In autonomous navigation research, persistent memory is essential for tasks that span multiple floors where maps are unknown. This work bridges the gap between planar map building and multi‑object search in complex indoor settings.

## Implications
The findings suggest that 3D semantic persistence can be a general solution for any sequential navigation task requiring long‑term memory across dynamic environments. Industries developing smart buildings may adopt such models to improve robot coordination across floors without costly re‑mapping.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07079v1)
