---
title: Kathleen Remembers: Length-Invariant One-Shot Recall Without Attention
url: http://arxiv.org/abs/2608.30376v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_07-35-03Z_KathleenRemembers_Length_InvariantOne_ShotRecallWi.md
generated_at: 2026-08-31 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Kathleen Remembers, a length‑invariant one‑shot recall model that operates without attention by adding a fixed‑key holographic associative store called the notebook to a recurrent trunk. The notebook enables exact recall of items seen once at positions far beyond the training length, achieving 80–82 % accuracy while the bare trunk scores only ~4 %.

## Key Takeaways
- The notebook reaches 80‑82 % one‑shot recall at 4× the training length while the bare trunk scores ~4%; a parameter‑matched attention head scores 100 % inside its training length and drops to 0 % beyond it.  
- Length‑invariant by construction; the untrained memory alone recalls at 90 % accuracy identically at 512, 2048 and 4096 bytes.  
- Two capabilities follow from arithmetic alone: selective unlearning (one subtraction erases one fact to chance, retained facts unharmed) and per‑token attribution (counterfactual erasure names the source fact of every correct byte, 100 % provenance).  

## Context
This work challenges the assumption that attention is necessary for long‑range dependencies, suggesting alternative architectures can maintain performance without quadratic cost. It offers a memory mechanism that scales linearly with input size, preserving recall across variable‑length inputs.

## Implications
Practitioners can deploy models with exact recall across variable‑length inputs, reducing the need for costly attention mechanisms and enabling robust deployment on limited hardware. This approach may become standard in applications requiring reliable retrieval without attention overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30376v1)
