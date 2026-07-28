---
title: Extreme Volatility Warning under Label Scarcity via Multi-Source Anomaly Fusion
url: http://arxiv.org/abs/2607.23682v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_14-30-58Z_ExtremeVolatilityWarningunderLabelScarcityviaMulti.md
generated_at: 2026-07-27 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses the challenge of detecting extreme market volatility when labeled data are scarce, using a multi-source anomaly fusion approach on the CSI~300 index. It shows that a simple hybrid model outperforms both unsupervised baselines and neural networks in this low‑label regime.

## Key Takeaways
- The 100K‑parameter hierarchical text‑signal fusion model (HTSF) degrades when added parameters are introduced, indicating instability under few positive labels.
- AAMSF combines Isolation Forest anomaly scores with GDELT events and Chinese financial news, achieving an AUC‑ROC of 0.680 on test data.
- Temporal extension T‑AAMSF captures multi‑day risk accumulation, raising PR‑AUC to 0.291.

## Context
In finance AI, early warning systems rely heavily on supervised learning which fails when anomalies are rare and nonstationary. This work demonstrates that unsupervised anomaly geometry can be more reliable than deep representation capacity in such regimes.

## Implications
The findings suggest a design principle where source reliability outweighs model complexity for label‑scarce risk prediction. Practitioners should prioritize data provenance and temporal accumulation to build robust volatility alerts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23682v1)
