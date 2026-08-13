---
title: MuseCritic: Learning Multi-Aspect Song Rewards through Natural-Language Aesthetic Critiques
url: http://arxiv.org/abs/2608.11755v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_07-49-17Z_MuseCritic_LearningMulti_AspectSongRewardsthroughN.md
generated_at: 2026-08-12 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
MUSECRITIC is a semi‑scalar reward model that generates natural‑language critiques across five aesthetic dimensions and uses them to predict continuous song scores. The approach reduces macro‑averaged mean squared error on SongEval from 0.2875 to 0.2316 and improves several correlation metrics, while achieving the highest accuracy of 71.35% on the out‑of‑domain Music Arena benchmark. When combined with GRPO, it boosts Muse‑0.6B across all nine aesthetic metrics.

## Key Takeaways
- Macro‑averaged mean squared error drops from 0.2875 to 0.2316, indicating a substantial reduction in scoring error.
- Macro‑averaged LCC, SRCC, and Kendall’s tau increase to 0.9068, 0.8838, and 0.7178 respectively, showing stronger alignment with human preferences.
- The model reaches the highest accuracy of 71.35% on Music Arena preference pairs and improves Muse‑0.6B metrics from SongEval and Audiobox Aesthetics.

## Context
Long‑form song generation models have advanced in duration and complexity but still rely on limited, single‑pass reward models that lack human‑readable explanations. This paper addresses the need for reliable aesthetic rewards by introducing a critique‑conditioned model that bridges the gap between natural language feedback and continuous scoring.

## Implications
The results demonstrate that integrating natural‑language critiques as an intermediate representation can reduce scoring error and provide a more effective optimization signal for song generation. Practitioners can leverage this framework to improve alignment with human aesthetics, fostering higher quality outputs in music AI applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11755v1)
