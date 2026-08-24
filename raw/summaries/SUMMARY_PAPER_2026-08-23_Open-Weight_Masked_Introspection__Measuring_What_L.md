---
title: Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation
url: http://arxiv.org/abs/2608.20569v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-20_21-09-50Z_Open_WeightMaskedIntrospection_MeasuringWhatLangua.md
generated_at: 2026-08-23 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether open‑weight language models can introspect about their own computation and report accurately about any changes. It finds that none of the eight tested models can distinguish real interventions from sham conditions beyond chance, with an AUROC around 0.5007. A linear probe also recovers intervention signals at high accuracy, indicating the information is present but not conveyed in the model’s verbal output.

## Key Takeaways
- No model's report discriminates a real intervention from a sham beyond chance (AUROC ~0.5007)  
- An equivalence test limits the effect to below 0.15 percentage points of AUROC  
- A linear probe recovers intervention presence at 75%‑95.8% accuracy, with no held‑out error at the last layer before the model speaks  

## Context
Frontier models have been claimed to be able to audit their internal states and report confidently about changes. This work challenges that optimism by demonstrating a gap between what the models actually compute and what they can convey in text, especially for open‑weight variants.

## Implications
The inability of current open‑weight models to introspect means any reliance on their self‑reported testimony must be cross‑checked against an internal reference. Future research may focus on improving the pathway from internal signals to verbal reports rather than expecting perfect self‑audit.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20569v1)
