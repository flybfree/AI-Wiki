---
title: Seeds Before Objectives: Rethinking Evaluation for Low-Resource Garhwali ASR
url: http://arxiv.org/abs/2608.10670v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_08-51-57Z_SeedsBeforeObjectives_RethinkingEvaluationforLow_R.md
generated_at: 2026-08-11 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a reproducible multi‑seed ASR benchmark for Garhwali, an under‑resourced Indo‑Aryan language, by generating per‑seed outputs and performing significance testing on the official VAANI splits. It re‑examines earlier reported gains and finds them fragile: neither Focal CTC nor a matra‑weighted objective beats standard CTC at seed level, while Hindi‑to‑Garhwali transfer offers no advantage over direct fine‑tuning. The only consistent result is that w2v‑BERT 2.0 with standard CTC achieves 47.0 % WER across five seeds, surpassing larger models like MMS‑1B.

## Key Takeaways
- Per‑seed evaluation and significance testing reveal that many reported gains are not robust, indicating they may be artifacts of a single random seed rather than genuine improvements.
- The matra‑weighted objective fails to reduce errors even on its intended targets, showing that weighting strategies do not always translate into better performance in low‑resource settings.
- w2v‑BERT 2.0 with standard CTC consistently reaches 47 % WER over five seeds, demonstrating that pretraining design and evaluation methodology matter more than sheer model size.

## Context
Low‑resource language ASR remains a challenge because benchmarking often relies on single runs that can mask variability between seeds. This work highlights the need for rigorous multi‑seed testing to separate real performance gains from statistical noise.

## Implications
For practitioners, adopting multi‑seed evaluation will prevent overstated confidence in model improvements. Researchers should prioritize pretraining design and reproducible benchmarks over chasing higher parameter counts, ensuring that results are trustworthy across different random seeds.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10670v1)
