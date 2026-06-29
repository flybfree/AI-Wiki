---
title: Vision-Default, Prior-Override: Causal Mechanisms of Perception-Knowledge Conflict in Vision-Language Models
url: http://arxiv.org/abs/2606.28273v1
type: paper-summary
date: 2026-06-28
source_paper: 2026-06-26_17-16-04Z_Vision_Default_Prior_Override_CausalMechanismsofPe.md
generated_at: 2026-06-28 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how vision-language models resolve conflicts between visual input and stored world knowledge, identifying a causal mechanism. It finds that visual grounding occurs automatically while prior grounding depends on a small set of attention heads in the second half of the network. Ablating those heads flips predictions from knowledge‑based to visual answers in most cases.

## Key Takeaways
- Visual grounding emerges by default across VLM families, whereas prior grounding relies on 2.5–4.8% of attention heads concentrated later in the model.
- Removing those heads changes predictions from stored knowledge to visual evidence in 68–96% of prior‑knowledge prompts but only minimally affects visually grounded answers (0.8–7.5%).
- The functional heads decompose into routing heads that control information flow and writing heads that directly inject answer tokens into the residual stream.

## Context
Vision-language models often struggle with perceptual‑knowledge conflicts, affecting reliability in applications like medical imaging or autonomous driving. Prior work treated these conflicts as black‑box behaviors without uncovering component‑level causal pathways. This study bridges that gap by linking model architecture to functional outcomes.

## Implications
Understanding the sparse causal circuit enables targeted interventions such as head pruning or routing adjustments to preserve knowledge grounding while maintaining visual fidelity. Practitioners can use this insight to design more robust multimodal systems with predictable behavior under conflicting evidence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.28273v1)
