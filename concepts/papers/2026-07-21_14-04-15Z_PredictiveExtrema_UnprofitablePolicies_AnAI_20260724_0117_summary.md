# Summary: 2026-07-21_14-04-15Z_PredictiveExtrema_UnprofitablePolicies_AnAI_Assist.md
Saved: 2026-07-24 01:17
Source: 2026-07-21_14-04-15Z_PredictiveExtrema_UnprofitablePolicies_AnAI_Assist.md
Model: None

---

## Summary  
The paper audits whether machine‑learning models that predict cryptocurrency extrema or short‑horizon outcomes can be turned into profitable Binance Spot policies after accounting for transaction costs. By running a series of scripted, fixed‑seed simulations and having human‑supervised AI agents perform literature retrieval, critique, artifact reconciliation, and documentation, the authors demonstrate that most candle‑based timing models fail to generate positive returns. The audit also uncovers methodological flaws in earlier work, reinforcing the need for rigorous cost‑aware evaluation before deploying any trading strategy.

## Key Contributions  
- [Finding 1] Candle‑based ML models, when evaluated with realistic costs, produce negative net returns over multiple cycles, indicating that predictive extrema do not translate into profitable policies.  
- [Finding 2] The best‑performing local‑minimum policy lost 6.72 % after a ten‑pair daily selector was applied for 19 July cycles, while its gross mean advantage (≈11.11 bps) fell below the 21‑bp stress threshold used in the study.  
- [Finding 3] A forensic audit of an earlier “One4All 30‑day holdout” reveals that date selection, four‑hour horizon handling, same‑close entry, and missing raw result directories biased the results, undermining its credibility.

## Methodology  
The authors employed a deterministic simulator to execute model runs with fixed seeds, ensuring reproducibility. Human‑supervised AI agents were tasked with retrieving relevant literature, critiquing the methodology, reconciling artifacts, preparing documentation, and packaging sources—none of which involved actual trading decisions. This hybrid approach allowed systematic testing while preserving human oversight for audit integrity.

## Results  
Across seven cycles, the OHLCV‑only daily adaptation reached ROC AUCs of 0.874 (minimum) and 0.896 (maximum), but its average precision was only 0.134 and 0.116 respectively, resulting in a 44.30 % loss versus -41.20 % for buy‑and‑hold. The ten‑pair selector’s net loss of 6.72 % after costs is the most severe observed outcome. All experimental outcomes confirm that event‑ranking performance does not guarantee executable policy value.

## Significance  
These findings matter because they highlight a common pitfall: AI‑driven timing models often overestimate profitability when cost and data biases are ignored. By exposing methodological weaknesses, the paper encourages developers to adopt rigorous, cost‑aware audits before deploying any crypto trading strategy, thereby reducing speculative losses in volatile markets.

## Related Concepts  
Predictive extrema, machine learning, Binance Spot trading, ROC AUC, average precision, event ranking, AI‑assisted audit, deterministic simulation, cost‑aware evaluation.
