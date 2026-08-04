---
title: Floor, Ceiling, and the Fusion Gap: How Much of Crowd Reading Attention Can Machines Predict?
url: http://arxiv.org/abs/2608.01704v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_05-09-49Z_Floor_Ceiling_andtheFusionGap_HowMuchofCrowdReadin.md
generated_at: 2026-08-03 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper defines a benchmark for predicting which sentences readers highlight in web documents and evaluates how well machine models can capture the crowd’s signal. It establishes a floor of naive truncation and a ceiling given by a split‑half oracle, showing a gap of +0.2028 AP. The study shows that frontier language models recover 35–53% of this gap zero‑shot, while an unweighted fusion of five models improves performance by +0.0159 and this gain is confirmed in a pre‑registered replication.

## Key Takeaways
- Semantic features such as position and length explain only about 5 % of the crowd’s advantage, indicating that most signal is beyond simple cues.
- Zero‑shot frontier language models capture a substantial portion (35–53%) of the gap, yet their performance remains far below the true crowd baseline.
- An unweighted cross‑vendor fusion of five state‑of‑the‑art rankings yields 60 % AP, beating any single model by +0.0159 and this gain is confirmed in a pre‑registered replication.

## Context
The work addresses a rare ground truth where crowd attention is measured without instruction, highlighting the difficulty of extracting unstructured human behavior from text. It contributes to AI research on fusion methods that combine heterogeneous models to approximate collective intelligence.

## Implications
For practitioners, the findings suggest that averaging multiple frontier models can yield modest but reliable gains with minimal cost, and that document‑level structure holds richer information than local context alone. This cheap improvement strategy could be applied to other crowd‑based tasks where human signals are sparse and unstructured.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01704v1)
