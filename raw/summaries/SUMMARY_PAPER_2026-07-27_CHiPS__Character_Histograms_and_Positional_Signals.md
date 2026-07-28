---
title: CHiPS: Character Histograms and Positional Signals for Lightweight Authorship Attribution in Romanian Texts
url: http://arxiv.org/abs/2607.22884v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_19-48-32Z_CHiPS_CharacterHistogramsandPositionalSignalsforLi.md
generated_at: 2026-07-27 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CHiPS, a lightweight character-level authorship attribution method for Romanian texts that combines a one‑character histogram classifier with a positional signal classifier based on impulse trains and spectral descriptors. On a locked grouped ROST split the method achieves 93.10 accuracy and 93.41 macro‑F1 using a leakage‑safe decision‑level fusion variant.

## Key Takeaways
- CHiPS relies solely on one‑character marginal distributions in its histogram component, deliberately omitting n‑gram features to minimize leakage.
- The FFT12‑LR classifier encodes characters and punctuation as binary impulse trains over positions and extracts Fourier/Welch spectral descriptors to capture positional style cues.
- A decision‑level fusion variant CHiPS‑F reaches 93.10 accuracy and 93.41 macro‑F1, while a comparator SVM that uses unrestricted character n‑grams attains perfect scores, highlighting the method’s intentional restriction.

## Context
Authorship attribution often depends on tokenized embeddings or higher‑order n‑gram models that can introduce leakage and privacy concerns; this work shows that simple, transparent character signals can be effective when carefully constrained.

## Implications
For practitioners building low‑resource, privacy‑preserving text classifiers, CHiPS provides a simple, interpretable pipeline without tokenization or large language models. Its focus on strict leakage control sets a benchmark for ethical AI in authorship analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22884v1)
