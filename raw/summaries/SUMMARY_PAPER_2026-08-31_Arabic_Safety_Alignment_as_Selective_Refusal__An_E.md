---
title: Arabic Safety Alignment as Selective Refusal: An Empirical Study of SFT, DPO, and Guard Calibration
url: http://arxiv.org/abs/2608.29378v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_17-25-01Z_ArabicSafetyAlignmentasSelectiveRefusal_AnEmpirica.md
generated_at: 2026-08-31 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how Arabic large language models balance refusing harmful prompts while preserving acceptance of benign or sensitive ones, measuring refusal via two rates: H for harmful‑prompt refusals and B for benign refusals. Across five Arabic models on the AraSafe dataset, mixed supervised fine‑tuning (SFT) can achieve high H values with moderate B, whereas pure SFT leads to blanket refusals. A blind audit shows strong annotator agreement, and model‑specific interventions vary in their impact.

## Key Takeaways
- Mixed‑SFT configurations reach H = 90% to 93% while keeping B between 14% and 23%, exceeding the target H = 90% in several runs.  
- Direct Preference Optimization (DPO) and inference guards alter refusal rates differently across models, acting as non‑uniform upgrades rather than a single improvement.  
- Selected SFT raises H on Arabizi for all five models but none reaches 90%, indicating only partial transfer from Modern Standard Arabic.

## Context
Safety alignment in language models is essential to prevent harmful outputs while avoiding over‑restriction that harms legitimate use cases. This study highlights the nuanced trade‑off between refusal rates and demonstrates that uniform solutions rarely suffice for diverse linguistic contexts. The findings contribute to ongoing research on controllable model behavior across languages.

## Implications
For practitioners, selecting a deployment target and retaining only interventions that improve it is crucial; generic fixes may degrade performance. Industry adoption should focus on model‑specific tuning rather than one‑size‑fits‑all safeguards, ensuring Arabic models maintain high safety without sacrificing usability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29378v1)
