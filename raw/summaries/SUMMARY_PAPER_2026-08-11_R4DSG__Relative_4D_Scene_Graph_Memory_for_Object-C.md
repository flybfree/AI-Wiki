---
title: R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video
url: http://arxiv.org/abs/2608.11017v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_15-00-15Z_R4DSG_Relative4DSceneGraphMemoryforObject_CentricQ.md
generated_at: 2026-08-11 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
R4DSG proposes a relative 4D scene graph memory to support object‑centric question answering in long egocentric video streams, achieving notable gains over prior approaches on the EgoLifeQA benchmark. The method’s retrieval‑ready memory yields a 6.7‑point overall improvement and a 12.5‑point boost specifically for “when” questions.

## Key Takeaways
- R4DSG converts video into compact, queryable memory entries indexed by time, place, persistent objects, anchor‑relative change, and local interaction context.
- The system separates stable anchors from dynamic objects while preserving object identity across frames, using anchor‑relative transitions instead of a globally aligned world model.
- This design enables long‑horizon question answering with structured spatial and temporal information.

## Context
Long‑horizon egocentric video is essential for wearable AI assistants, yet existing caption or transcript‑based memories fail to capture persistent object identity and structured spatial change. Prior 3D scene‑graph methods assume richer inputs such as point clouds or RGB‑D data, which are unavailable in free‑motion RGB streams.

## Implications
R4DSG demonstrates that relative 4D scene graphs can serve as a practical memory substrate for AR systems, embodied multimedia agents, and other long‑range video applications. The approach lowers the barrier to building object‑centric assistants by providing a lightweight, retrieval‑ready representation without heavy preprocessing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11017v1)
