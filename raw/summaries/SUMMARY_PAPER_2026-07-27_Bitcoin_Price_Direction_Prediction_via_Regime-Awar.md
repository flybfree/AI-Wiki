---
title: Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of Social Sentiment and Technical Features
url: http://arxiv.org/abs/2607.23370v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_21-25-12Z_BitcoinPriceDirectionPredictionviaRegime_AwareMult.md
generated_at: 2026-07-27 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Regime-Aware Multi-Modal Learning (RAML), a framework that predicts Bitcoin price movements on sub‑daily horizons by fusing technical OHLCV data with social sentiment from Reddit and Twitter. By detecting volatile versus stable market regimes and applying adaptive fusion weights, RAML outperforms static concatenation methods, achieving macro‑F1 scores of 0.5474 at three hours and 0.5513 at six hours.

## Key Takeaways
- The paper demonstrates that sentiment is most informative during volatile periods, while price dynamics dominate in stable phases, highlighting the need for regime‑aware fusion.  
- RAML’s adaptive weighting improves calibration, with the highest AUC of 0.5084 observed at three‑hour horizons compared to other models.  
- Ablation results show that removing any component—sentiment branch, regime detection, or adaptive gating—causes a sharp drop in performance, especially recall at six hours.

## Context
The study addresses the challenge of Bitcoin price forecasting by integrating heterogeneous data streams within a single model, reflecting broader trends in AI research toward multi‑modal and context‑aware learning. By conditioning fusion on market regime, RAML exemplifies how dynamic weighting can enhance predictive accuracy beyond rigid concatenation approaches.

## Implications
For practitioners, RAML offers a practical blueprint for building robust financial forecasting systems that adapt to changing market conditions. The methodology could be extended to other assets or sentiment sources, providing a scalable template for AI‑driven investment tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23370v1)
