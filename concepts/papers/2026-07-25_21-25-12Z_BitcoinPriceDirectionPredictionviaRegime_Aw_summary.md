# Summary: 2026-07-25_21-25-12Z_BitcoinPriceDirectionPredictionviaRegime_AwareMult.md
Saved: 2026-07-27 23:51
Source: 2026-07-25_21-25-12Z_BitcoinPriceDirectionPredictionviaRegime_AwareMult.md
Model: None

---

## Summary  
The paper tackles the challenge of predicting Bitcoin price direction on sub‑daily time scales by integrating social sentiment from Reddit and Twitter with traditional OHLCV technical indicators. Conventional static concatenation fails because it treats sentiment equally regardless of market state, whereas behavioural finance suggests sentiment is most informative during volatile periods. The authors introduce Regime‑Aware Multi‑Modal Learning (RAML), a framework that detects a binary stable/volatile regime and applies an adaptive sigmoid gate to weight the sentiment embedding relative to price features. This conditional fusion improves calibration and recall compared with baseline models.

## Key Contributions  
- [Finding 1] RAML conditions the fusion of sentiment and technical data on a dynamically detected market regime, allowing the model to trust sentiment more during volatility.  
- [Finding 2] The adaptive weighting mechanism preserves recall at longer horizons (6 h) while static concatenation causes severe performance collapse (F1 ≈ 0.14).  
- [Finding 3] RAML attains macro‑F1 scores of 0.5474 (3‑hour horizon) and 0.5513 (6‑hour horizon), with the highest AUC at the 3‑hour window.

## Methodology  
The authors collect hourly Bitcoin OHLCV data together with FinBERT‑derived sentiment embeddings from r/Bitcoin posts over July 2024–September 2025. A rolling 24‑hour volatility partition creates a binary regime label; a learnable sigmoid gate adjusts the fusion weight between the price embedding (from a BiLSTM) and the sentiment embedding. Four models are trained: price‑only BiLSTM, sentiment‑only classifier, static concatenation BiLSTM, and RAML. Evaluation is performed across 3‑hour and 6‑hour prediction horizons with an ablation study isolating each component.

## Results  
RAML achieves macro‑F1 of 0.5474 at the 3‑hour horizon and 0.5513 at the 6‑hour horizon, outperforming all baselines. The AUC is maximized at 3 hours (0.5084). Ablation confirms that removing any component—regime detection, sentiment branch, or adaptive gating—significantly degrades performance; static concatenation yields a recall collapse to F1 ≈ 0.14 at 6 hours.

## Significance  
RAML demonstrates that regime‑aware fusion is essential for multi‑modal financial forecasting, aligning with behavioural finance insights about sentiment reliability. By dynamically weighting modalities based on market conditions, the approach improves calibration and recall, offering a principled design principle for future research in volatile asset prediction.

## Related Concepts  
Bitcoin price dynamics, fat‑tailed returns, non‑stationarity, social sentiment analysis (FinBERT), technical indicators (OHLCV), multi‑modal learning, binary market regimes, volatility partitions, rolling windows, adaptive gating, macro‑F1 score, AUC.
