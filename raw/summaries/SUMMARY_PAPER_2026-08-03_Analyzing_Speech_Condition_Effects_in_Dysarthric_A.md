---
title: Analyzing Speech Condition Effects in Dysarthric ASR: A Layer-wise Probing Study
url: http://arxiv.org/abs/2608.01865v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_08-14-26Z_AnalyzingSpeechConditionEffectsinDysarthricASR_ALa.md
generated_at: 2026-08-03 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how disordered articulation in dysarthric Mandarin speech reshapes the internal representations of a transformer ASR encoder. It conducts layer‑wise probing under three transcript‑matched conditions and discovers that phoneme boundary information stays weak, phoneme identity becomes recoverable at upper layers, and recognition difficulty is encoded deep down. The study also shows that tone‑sensitive errors persist across conditions.

## Key Takeaways
- Phoneme boundary information stays weak for dysarthric speech across all layers indicating low‑level encoding is not preserved.
- Phoneme identity becomes recoverable toward the upper layers showing that higher‑level representations capture more semantic detail.
- Recognition difficulty is encoded in the deepest layers revealing that model struggles with low‑level acoustic cues.

## Context
Automatic speech recognition systems often assume clean input, yet real‑world speech includes variability such as dysarthria. Understanding how these impairments affect model internals helps improve robustness without full retraining. This study bridges representation analysis and adaptation techniques for low‑resource Mandarin ASR.

## Implications
Layer‑aware fine‑tuning can reduce adaptation cost and maintain performance on dysarthric inputs. Practitioners can focus effort on upper layers where phoneme identity is more recoverable, offering a practical path to efficient model improvement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01865v1)
