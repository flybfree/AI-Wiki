---
title: Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music Generation
url: http://arxiv.org/abs/2608.03999v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_17-56-49Z_Agogic_Performance_TimedMusicTokensforLLM_NativeTe.md
generated_at: 2026-08-05 01:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how music tokenization influences the performance of LLM‑native text‑to‑music generation, measuring distributional fidelity with Frechet Music Distance across seven different tokenizations while keeping model size, data, budget and decoding fixed. It finds that representation (tokenization) is far more important than model scale, with a 0.8B model using the PMT stream achieving lower FMD than larger models that rely on beat grids.

## Key Takeaways
- Representation matters more than model size; switching tokenization halves Frechet Music Distance while scaling the backbone barely changes it.
- The performance‑resolution stream PMT (10 ms timing, per‑note velocity, multi‑track texture) reaches FMD 159 at 0.8B versus 272–286 for beat grids, beating them across metrics and with non‑overlapping bootstrap CIs.
- The improvement is distributional, not merely a finer lattice artifact; snapping PMT’s onsets to the beat grid resolution still leaves it ahead by 67–129 FMD.

## Context
In AI text‑to‑music generation tokenization choices are often treated as secondary to model size and data, yet they can dramatically affect output quality. This work isolates tokenization as a variable and provides empirical evidence that representation‑level improvements can outperform larger models without extra compute.

## Implications
Optimizing tokenization offers a viable path to better music generation without scaling up compute, encouraging developers to experiment with resolution‑aware tokenizers. The findings also open avenues for human evaluation beyond FMD and support reproducible research through released datasets and diagnostic tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03999v1)
