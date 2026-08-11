---
title: VectraYX-Vision-1B: A Sub-2B Spanish/LATAM Cybersecurity Vision-Language Model with Structured Visual Reasoning and Native Tool Use
url: http://arxiv.org/abs/2608.08477v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_04-46-58Z_VectraYX_Vision_1B_ASub_2BSpanish_LATAMCybersecuri.md
generated_at: 2026-08-10 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces VectraYX‑Vision‑1B, a sub‑2B vision‑language model for Spanish/LATAM cybersecurity imagery that couples a frozen SigLIP encoder with a 1.04B decoder and supports native tool use via <|tool_call|> tokens. Preliminary results show B6 scores of only 0.08 for tool identification, indicating the current SFT pipeline is ineffective despite functional pipelines.

## Key Takeaways  
- The model’s vision SFT pipeline (400–1900 steps, ~16M tokens) yields B6 scores of only 0.08 for tool identification, ignoring image content.  
- A checkpoint‑loader bug with an unstripped llm. prefix masquerades as training collapse, causing the low performance.  
- The authors release a three‑variant ablation matrix (V0: NoPE‑every‑4, V1: all‑RoPE, V2: NoPE+learned 2D) to study whether periodic no‑positional‑encoding layers help or hurt attention over the 729-token visual block.

## Context  
This work addresses the growing need for lightweight multilingual vision models that can operate offline in resource‑constrained environments such as air‑gapped security labs. By coupling a frozen encoder with a decoder and exposing tool calls via Model Context Protocol, it demonstrates how small models can still perform structured reasoning in low‑resource settings.

## Implications  
The findings highlight that even sub‑2B models require careful fine‑tuning schedules and architectural tweaks to achieve useful performance. The open release of checkpoints and configurations encourages reproducible research on efficient visual grounding for cybersecurity tasks, potentially lowering deployment barriers for field teams.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08477v1)
