---
title: Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models
url: http://arxiv.org/abs/2609.04575v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_00-11-28Z_Training_FreeHalvingofActivatedExpertsinFine_Grain.md
generated_at: 2026-09-06 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the renormalization of router probabilities in fine‑grained MoE models implicitly calibrates expert output gain to the training top‑k. By separating activation and normalization, it demonstrates that halving the number of activated experts reduces compute while only modestly affecting performance when a suitable reference mass is preserved.

## Key Takeaways
- Reducing the router’s top‑k from 8 to 4 causes a 4.65‑point MMLU drop under standard renormalization but only 0.35 points with k₂=16, showing that expert strength can be tuned without retraining.
- Removing renormalization entirely leads to catastrophic performance loss, indicating that preserving the probability mass of a reference set is essential for stable inference.
- Perplexity and downstream accuracy favor different values of k₂, so compression settings should not rely solely on unlabeled text.

## Context
MoE architectures aim to compress large language models by routing tokens to a subset of expert networks. The implicit calibration introduced in this work highlights how small changes in routing parameters can have non‑trivial effects on model behavior and efficiency.

## Implications
Practitioners can now adjust MoE compression with minimal overhead, preserving accuracy while halving compute. This insight is valuable for deploying cost‑effective models at scale without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04575v1)
