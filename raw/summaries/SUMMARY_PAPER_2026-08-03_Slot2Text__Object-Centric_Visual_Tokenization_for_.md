---
title: Slot2Text: Object-Centric Visual Tokenization for Efficient and Spatially Traceable Surgical MLLMs
url: http://arxiv.org/abs/2608.01473v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_20-09-45Z_Slot2Text_Object_CentricVisualTokenizationforEffic.md
generated_at: 2026-08-03 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
Slot2Text introduces a dual‑mode surgical multimodal language model that replaces the dense visual token stream with a compact set of region‑encoded slot latents, drastically lowering inference cost while preserving spatial traceability. Experiments demonstrate that Slot2Text‑Fast achieves state‑of‑the‑art performance on visual question answering and grounding tasks with a 91.8 % reduction in total token consumption and a 96.4 % drop in the visual prefix length from 1,295 to 47 tokens.

## Key Takeaways
- Slot2Text substitutes dense visual representations with a few area‑labeled slots, enabling efficient inference.
- The method reduces average token usage by 91.8 %, cutting the visual prefix size dramatically.
- Two modes are provided: Fast for low‑cost answering and Reason for explicit spatial grounding.

## Context
Current surgical MLLMs rely on dense image embeddings that inflate model size and latency, limiting real‑time applicability in operating rooms. Efficient tokenization is crucial for integrating these models into clinical workflows where speed and resource constraints are paramount.

## Implications
This approach offers a scalable template for other medical imaging tasks requiring spatial awareness without heavy visual tokens. Practitioners can adopt slot latents to build faster, more interpretable surgical assistants that balance performance with computational efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01473v1)
