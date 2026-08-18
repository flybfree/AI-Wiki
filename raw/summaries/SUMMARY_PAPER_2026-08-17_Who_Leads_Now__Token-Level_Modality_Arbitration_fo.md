---
title: Who Leads Now? Token-Level Modality Arbitration for Chart-to-Code Generation
url: http://arxiv.org/abs/2608.15510v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_03-33-01Z_WhoLeadsNow_Token_LevelModalityArbitrationforChart.md
generated_at: 2026-08-17 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MoCA, a chart-to-code model that separates visual understanding from code generation using a lightweight arbiter within Cross-modal Arbitration Block. It trains MoCA in two stages: supervised warm‑up on self‑distilled reasoning trajectories and reinforcement learning with rewards for both reasoning steps and final code. Experiments show MoCA achieves competitive performance across three benchmarks, outperforming general‑domain and chart‑specialized models.

## Key Takeaways
- The arbiter allocates contributions systematically to visual or code tokens at each layer, preventing arbitrary mixing.
- Joint initialization of the two branches enables complementary strengths without larger model size.
- Training stages decompose visual understanding into explicit steps before reinforcement learning refines code generation.

## Context
Chart‑to‑code systems often conflate visual parsing and programming tasks, leading to suboptimal performance. Separating these modalities aligns with recent efforts in modular neural architectures that treat distinct sub‑tasks independently.

## Implications
This approach can be applied to other multimodal translation tasks where two specialized branches must collaborate without interference. Practitioners may adopt CAB‑like blocks to improve efficiency and adaptability across diverse data domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15510v1)
