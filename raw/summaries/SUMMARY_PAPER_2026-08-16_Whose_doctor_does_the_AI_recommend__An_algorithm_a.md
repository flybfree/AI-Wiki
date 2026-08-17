---
title: Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice
url: http://arxiv.org/abs/2608.14399v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_15-39-10Z_WhosedoctordoestheAIrecommend_Analgorithmauditofre.md
generated_at: 2026-08-16 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits seven large language model systems to see which factors causally influence their recommendations for a physician. It finds that reputation and fee significantly affect choice probability while gender and ethnicity signals have smaller but measurable impacts, though the models do not explain these effects.

## Key Takeaways
- Raising a doctor’s rating from 3.9 to 4.7 boosts selection chance by 31.4 percentage points, showing strong weight given reputation.
- Increasing the fee from $90 to $190 reduces selection probability by 20.0 percentage points, indicating price sensitivity is powerful.
- Female‑signaled names add about 2.5 pp and minority‑signaled names add 1.3–2.9 pp over white names, translating to $7–14 fee equivalents despite models mentioning these signals only 0.03% of the time.

## Context
Large language model assistants are becoming de facto decision makers in healthcare, yet most systems lack transparent reasoning about why they suggest a particular doctor. This study provides an external audit that can be repeated with any new model, offering a benchmark for accountability.

## Implications
Clinics and AI developers must monitor these hidden biases because algorithmic recommendations affect patient access and equity. The audit’s repeatable design enables ongoing compliance checks without relying on opaque self‑explanations from the models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14399v1)
