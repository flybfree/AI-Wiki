---
title: When Models Edit Too Much: On the Fidelity of Minimal Code Edits
url: http://arxiv.org/abs/2609.04061v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_16-36-05Z_WhenModelsEditTooMuch_OntheFidelityofMinimalCodeEd.md
generated_at: 2026-09-03 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates over‑editing in large language model code repairs, showing that models often make unnecessary changes even when they achieve high pass rates. The study demonstrates that a preservation instruction can reduce excess edits and cognitive complexity while improving pass@1 scores. Supervised fine‑tuning overfits to known corruption patterns, whereas reinforcement learning yields better out‑of‑domain fidelity without sacrificing performance.

## Key Takeaways
- High Pass@1 can coexist with unnecessarily large edits that increase cognitive complexity, as shown by a 0.195 average excess Levenshtein distance across frontier models.
- A preservation instruction reduces the excess edit distance to 0.131 and cuts added cognitive complexity by 26.6%, while raising Pass@1 by two points.
- Reinforcement learning outperforms supervised fine‑tuning for out‑of‑domain edit fidelity, indicating that direct learning of minimal edits is more effective than pattern memorization.

## Context
Code repair remains a critical task in AI‑assisted software development, where correctness and maintainability are essential. This research highlights a gap: models prioritize pass rates over preserving original design intent, which can lead to brittle or hard‑to‑review code. Understanding edit fidelity is therefore vital for reliable deployment of automated repair systems.

## Implications
Practitioners must evaluate not only whether a model fixes bugs but also how much it rewrites the code, as large edits increase risk and review burden. The findings suggest that incorporating preservation instructions or using reinforcement learning can improve both quality and usability in real‑world code‑repair pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04061v1)
