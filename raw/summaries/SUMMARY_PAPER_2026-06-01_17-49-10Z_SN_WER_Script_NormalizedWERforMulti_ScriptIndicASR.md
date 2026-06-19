---

title: "Summary: SN-WER: Script-Normalized WER for Multi-Script Indic ASR Evaluation"
url: http://arxiv.org/abs/2606.02548v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-01_17-49-10Z_SN_WER_Script_NormalizedWERforMulti_ScriptIndicASR.md
generated_at: "2026-06-11 10:50"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces Script-Normalized WER (SN-WER), a training‑free evaluation metric that transliterates both reference and hypothesis into a language‑specific canonical script before computing the usual word error rate. On Indic languages, SN-WER reduces inflated model gaps by up to 12% on the curated FLEURS data.

## Key Takeaways
- SN-WER reduces inflated WER inflation by up to 12% on curated FLEURS data for Indic languages.
- It attenuates artificial romanization‑induced errors by 67%, indicating genuine recognition weaknesses are not just script mismatch.
- Lexical‑substitution controls show Delta SN‑WER / Delta WER ≈ 1.09, showing the metric is sensitive to semantic errors similarly to WER.

## Context
This work addresses a known limitation of standard WER in multilingual ASR where romanized outputs cause false error counts, affecting model evaluation and downstream tasks like search indexing.

## Implications
For practitioners, reporting SN‑WER alongside WER provides a script‑insensitive view useful for LLM pipelines. It encourages better handling of non‑Latin scripts without sacrificing metric reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.02548v1)
