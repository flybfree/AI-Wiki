---
title: 'Ghaib in Translation' aka Unseen Harm: Measuring Cross-Script Safety Inconsistency with 'Missed-in-Urdu' Scores in LLM Hate Speech Detection
url: http://arxiv.org/abs/2608.24191v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_07-58-40Z_GhaibinTranslation_akaUnseenHarm_MeasuringCross_Sc.md
generated_at: 2026-08-25 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models handle hate speech detection in Urdu scripts versus their English translations, revealing significant inconsistency across model families. It finds that while closed frontier models perform better than smaller open‑weight ones, label instability ranges from 15.9% to 31.6%, and a missed‑in‑Urdu rate of up to 9.9% occurs.

## Key Takeaways
- Label instability between original Urdu script and English translation varies widely across models, from 15.9% (Gemini) to 31.6% (Qwen), indicating unreliable cross‑script safety.
- The missed‑in‑Urdu rate, where harmful content is flagged in English but not in the original script, peaks at 9.9%, highlighting gaps in detection for native Urdu text.
- Smaller open‑weight models exhibit substantially higher instability and missed‑harm rates compared to larger closed frontier models.

## Context
Mainstream AI safety evaluations have largely ignored Urdu, a language with over 246 million speakers, leaving its script varieties underrepresented. This gap means that current LLM moderation systems may perform poorly for non‑English users, especially those using Urdu scripts.

## Implications
For practitioners, the findings suggest that deploying models without testing on Urdu can lead to unsafe content slipping through, particularly in mixed Urdu‑English contexts. Industry must prioritize multilingual safety audits and develop models with balanced script support to ensure equitable protection across languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24191v1)
