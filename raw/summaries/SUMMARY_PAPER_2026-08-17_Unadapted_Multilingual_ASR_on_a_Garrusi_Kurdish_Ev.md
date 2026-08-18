---
title: Unadapted Multilingual ASR on a Garrusi Kurdish Evaluation Set: A Common-Reference Staged Normalization Analysis
url: http://arxiv.org/abs/2608.16379v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_10-31-30Z_UnadaptedMultilingualASRonaGarrusiKurdishEvaluatio.md
generated_at: 2026-08-17 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates an unadapted multilingual speech recognition system for Central Kurdish written in Latin orthography but producing Arabic script on the Garrusi questionnaire dataset. Using a common‑reference design, it shows that raw scores are inflated by writing‑system mismatches and that folding the reference into a reduced orthography dramatically lowers both WER and CER.

## Key Takeaways
- Raw Arabic‑script hypotheses score 111.70 % WER and 100.92 % CER with zero exact word matches, indicating severe recognition errors.
- Folding the reference into a Latin‑based orthography yields 97.85 % WER and 51.20 % CER, reducing measured errors by 13.85 points in WER and 49.72 points in CER; folding alone accounts for only 4.51 and 6.69 points.
- A Southern Kurdish fine‑tuned model scores worse (109.56 % WER, 55.85 % CER) and leaves many output characters unmapped, showing residual pipeline limitations.

## Context
Speech recognition evaluation often neglects orthographic mismatches between reference and hypothesis scripts, leading to misleading performance numbers. Common‑reference designs aim to standardize tokenization but can alter the scoring denominator, highlighting the need for careful normalization across writing systems in multilingual ASR research.

## Implications
Practitioners must treat raw scores as imperfect indicators when dealing with non‑Latin orthographies and ensure reference folding is applied consistently. The findings stress that improving recognition alone does not solve evaluation problems; pipeline alignment and tokenization choices are equally critical for reliable assessment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16379v1)
