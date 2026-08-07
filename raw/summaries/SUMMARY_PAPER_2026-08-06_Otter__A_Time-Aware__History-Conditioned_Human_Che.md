---
title: Otter: A Time-Aware, History-Conditioned Human Chess AI
url: http://arxiv.org/abs/2608.05206v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_07-47-30Z_Otter_ATime_Aware_History_ConditionedHumanChessAI.md
generated_at: 2026-08-06 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
Otter is a human chess AI that predicts move selection by modeling play as a time‑aware sequential process rather than evaluating positions in isolation. It achieves top‑1 accuracy of 55.23% and top‑5 accuracy of 90.95%, beating the previous model Maia 2 with fewer parameters and less data.

## Key Takeaways
- The model uses a move history encoder that conditions predictions on the last 20 moves, capturing opening preferences and intra‑game behavioral trends.
- A time control module adjusts predictions based on clock pressure, integrating temporal dynamics into move selection.
- Training was performed on 6.1 billion positions from 117 million rapid games in 30 days on a single T4 GPU.

## Context
The paper contributes to the growing effort of human‑centric AI by showing that sequential modeling can outperform position‑only models despite smaller scale. It also demonstrates efficient training on limited hardware, reducing cost and environmental impact. The results also highlight the importance of capturing both historical patterns and real‑time constraints.

## Implications
For practitioners, Otter suggests that incorporating temporal context can improve performance in games where time pressure matters. The approach may inspire other domains where sequential behavior influences outcomes, offering a scalable template for human‑aware AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05206v1)
