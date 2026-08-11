---
title: Reading is not Reasoning: Bridging the Agentic Policy Gap in Vision-Text Compression
url: http://arxiv.org/abs/2608.08960v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_23-38-12Z_ReadingisnotReasoning_BridgingtheAgenticPolicyGapi.md
generated_at: 2026-08-10 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the performance gap that emerges when language‑model agents are compressed from pure text to a vision–text hybrid, where interaction histories are encoded as images. The authors demonstrate that visual‑history agents suffer systematic drift in decision making, query formulation, stopping criteria and evidence use, which cannot be resolved by improving OCR quality alone. They propose CAPS, a two‑stage cross‑modal policy self‑distillation framework, to transfer the stronger text‑policy behavior onto the compressed visual‑history model.

## Key Takeaways
- Visual‑history agents exhibit systematic drift in action selection, query formulation, stopping and evidence use, indicating an agentic policy gap beyond OCR quality.  
- CAPS uses offline trajectory self‑distillation to transfer successful text‑policy behavior to visual‑history inputs and online policy self‑distillation for dense supervision on visited states.  
- The framework improves performance by up to 15.6 % on full‑history ALFWorld with a 3B backbone, while reducing average memory‑context cost by up to 63.3 %.

## Context
Vision–text compression is increasingly adopted to lower compute and latency for multimodal agents, yet the shift from textual to visual histories introduces hidden performance penalties that are not fully understood. This work addresses that gap by showing that policy alignment mechanisms can mitigate these penalties.

## Implications
For practitioners, CAPS offers a practical method to preserve agent capability when compressing interaction data, directly impacting efficiency and reliability in real‑world deployment. The findings suggest that cross‑modal self‑distillation is a viable strategy for maintaining high‑quality reasoning under resource constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08960v1)
