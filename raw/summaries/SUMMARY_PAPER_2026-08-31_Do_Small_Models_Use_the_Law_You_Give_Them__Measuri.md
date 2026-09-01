---
title: Do Small Models Use the Law You Give Them? Measuring Context Use on a Bilingual Bangladesh Legal Benchmark
url: http://arxiv.org/abs/2608.30327v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_06-45-16Z_DoSmallModelsUsetheLawYouGiveThem_MeasuringContext.md
generated_at: 2026-08-31 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether fine‑tuned legal language models actually rely on the law provided in a bilingual Bangladesh dataset or merely improve scoring of answers. Using a curated hierarchy‑preserving corpus and controlled experiments, it finds that model performance gains are largely driven by answer scoring rather than genuine use of governing provisions.

## Key Takeaways
- The Qwen3.5‑2B seed‑42 adapter shows an exact‑line parser accuracy boost of 50 % while option‑letter scoring adds only 3 %, indicating that most improvement comes from the scorer, not direct law usage.
- Removing the governing provision reduces model and adapter accuracy by 8–15 % points, yet difference‑in‑differences analyses reveal no increase in reliance on the provision after fine‑tuning, suggesting scorers mask true legal dependence.
- Fine‑tuned models improve by 14.7–19.3 % under a four‑order criterion only when the governing law is guaranteed present, highlighting the need to separate scorer, retriever, and model effects.

## Context
Legal question‑answering systems often claim that fine‑tuning makes them “use” supplied statutes, but empirical evidence shows this may be an artifact of answer scoring rather than genuine comprehension. This study contributes a granular measurement framework for bilingual legal data, helping researchers distinguish between algorithmic artifacts and true legal reasoning.

## Implications
For developers, the findings warn against attributing performance gains to fine‑tuning alone; they recommend rigorous evaluation that isolates scorer behavior. Practitioners should focus on improving retrieval and model alignment with statutes rather than merely adjusting scoring mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30327v1)
