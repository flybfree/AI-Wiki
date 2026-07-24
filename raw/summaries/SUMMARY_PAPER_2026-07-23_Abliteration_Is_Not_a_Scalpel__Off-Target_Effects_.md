---
title: Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families
url: http://arxiv.org/abs/2607.17427v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_22-27-00Z_AbliterationIsNotaScalpel_Off_TargetEffectsofRefus.md
generated_at: 2026-07-23 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates what happens when refusal directions are removed from open-weight models using abliteration, a technique that deletes model outputs containing refusals. Experiments compare two Mixture-of-Experts families—Gemma‑4‑26B‑A4B‑it and Qwen3‑30B‑A3B‑Instruct‑2507—using 21,600 equity decisions as a side‑effect probe. The results show systematic shifts in optimism, length of justification, use of uncertainty words, and confidence that differ by model family.

## Key Takeaways
- Abliteration makes both models more optimistic: Gemma gains +12.2 percentage points while Qwen gains +7.4 pp on the weekly up/down call endpoint.
- The abliterated arms produce longer justifications and fewer explicit uncertainty words in forced self‑critiques, indicating altered reasoning style.
- A fourth effect reverses sign across families: Gemma‑abliterated becomes less confident whereas Qwen‑abliterated becomes more confident, with non‑overlapping confidence intervals.

## Context
Open‑weight models are increasingly marketed as “uncensored,” yet their decision‑making behavior may be altered by simple weight edits. This study reveals that such modifications produce measurable changes in output style and confidence, challenging the assumption that removing refusals leaves model capability intact.

## Implications
For practitioners deploying open‑weight agents, the paper warns that an “uncensored” model is not merely the base model minus refusals; it may behave differently in real‑world settings. This insight should guide rigorous evaluation pipelines and provenance checks to avoid hidden side effects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17427v1)
