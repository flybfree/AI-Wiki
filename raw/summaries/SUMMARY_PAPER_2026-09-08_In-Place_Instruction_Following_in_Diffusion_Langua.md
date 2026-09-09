---
title: In-Place Instruction Following in Diffusion Language Models
url: http://arxiv.org/abs/2609.07160v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_07-55-40Z_In_PlaceInstructionFollowinginDiffusionLanguageMod.md
generated_at: 2026-09-08 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces In-place Instruction Following (IIF) for diffusion language models and evaluates it on IIF‑Bench. It shows that vanilla dLLMs under‑prioritize constraint spans, but a GRAFT framework boosts scores from 57.75 to 73.10.

## Key Takeaways
- The study formalizes IPP as the IIF task and creates a hierarchical benchmark with literal, style, and discourse-function constraints evaluated via rubric‑based local‑global metrics.
- Inference‑time attention‑bias probes reveal that constraint spans are often ignored during denoising in vanilla dLLMs.
- GRAFT’s combination of constraint‑aware SFT and preference optimization raises average IIF score by 15.35 points, especially for literal (15.91) and discourse-function constraints.

## Context
Diffusion language models have become a dominant approach for generating coherent text, but their ability to follow precise user instructions at arbitrary positions remains under‑explored. This work addresses that gap by defining a concrete evaluation protocol and demonstrating practical improvements through post‑training fine‑tuning.

## Implications
For practitioners, the results suggest that targeted instruction following can be achieved without sacrificing general generation quality, offering a route for more reliable chatbots and content creators. The methodology could inform future research on constraint‑aware model training across diffusion frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07160v1)
