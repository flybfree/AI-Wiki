---
title: MAGE: Human-Like Macro Placement via Agentic Multimodal Reasoning
url: http://arxiv.org/abs/2607.18536v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_22-02-22Z_MAGE_Human_LikeMacroPlacementviaAgenticMultimodalR.md
generated_at: 2026-07-23 23:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
MAGE (Macro Placement Agentic Engine) is a multimodal multi‑agent framework that refines macro placement in industrial physical design flows by combining structured floorplanning rules, visual checks, and iterative refinement guided by natural‑language directives. The system achieves geometric‑mean improvements of 11.1%–19.3% in wirelength (WNS) and 70.0%–74.0% in total net size (TNS) over commercial macro placers on real design sets.

## Key Takeaways
- MAGE encodes expert floorplanning knowledge through natural‑language directives rather than training on labeled placement data, enabling interpretable rule‑based guidance.
- The tournament‑style refinement mode evaluates multiple candidate placements and propagates feedback from higher‑quality solutions, allowing systematic improvement without manual iteration.
- On NanGate45 designs, MAGE outperforms human experts by 18.3% in WNS and 72.5% in TNS, and exceeds Hier‑RTLMP by 47.0% and 80.4%, while maintaining comparable wirelength and power.

## Context
This work advances AI research on multimodal reasoning by integrating visual inspection with structured rule execution within an agentic workflow. It demonstrates that agents can perform complex design tasks without requiring extensive labeled datasets, highlighting a shift toward explainable, transfer‑friendly AI systems in engineering.

## Implications
MAGE reduces reliance on manual refinement steps, lowering cost and error rates for manufacturers adopting automated placement tools. Its human‑likeness metrics provide clear benchmarks for evaluating aesthetic quality, encouraging the industry to prioritize both performance and design aesthetics in AI‑driven layout solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18536v1)
