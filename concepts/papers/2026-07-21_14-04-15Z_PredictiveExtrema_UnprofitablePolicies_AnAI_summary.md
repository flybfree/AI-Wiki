# Summary: 2026-07-21_14-04-15Z_PredictiveExtrema_UnprofitablePolicies_AnAI_Assist.md
Saved: 2026-07-24 00:57
Source: 2026-07-21_14-04-15Z_PredictiveExtrema_UnprofitablePolicies_AnAI_Assist.md
Model: None

---

## Summary  
The paper audits whether candle‑based machine‑learning models can convert predictions of cryptocurrency extrema or short‑horizon outcomes into profitable Binance Spot trading policies after accounting for transaction costs. It evaluates a suite of fixed‑seed, deterministic simulations and human‑supervised AI agents that performed literature retrieval, critique, artifact reconciliation, and documentation without ever executing trades. The audit reveals that most candidate strategies, despite seemingly high predictive metrics, generate negative returns or modest gains that are outweighed by costs. A forensic review also uncovers methodological flaws in an earlier “30‑day holdout” experiment. Overall, the study demonstrates that event‑ranking models do not reliably produce executable, profitable policies on Binance Spot.

## Key Contributions  
- [Finding 1] The unchanged ten‑pair mandatory‑daily selector lost 6.72 % over 19 July cycles at an assumed 31‑bps cost, yielding three wins and sixteen losses.  
- [Finding 2] In short‑term model evaluations the validation‑selected local‑minimum policy returned –1.79 %, while a sell‑to‑cash/re‑entry policy underperformed continuous holding by 2.80 %; their gross mean advantages of 11.11 and 12.21 bps fell short of even the 21‑bps stress threshold.  
- [Finding 3] The earlier One4All “30‑day holdout” was downgraded because its dates influenced prior architecture work, a four‑hour outcome horizon was not purged at split boundaries, it used same‑close entry, and raw result directories were missing.

## Methodology  
The authors employed scripted fixed‑seed model runs within deterministic simulators to generate trading signals from candle data. Human‑supervised AI agents assisted by retrieving relevant literature, performing independent critique, reconciling artifacts, and packaging documentation—none of which involved actual trades. The evaluation covered a mandatory daily selector across ten pairs, short‑term policy tests, and a forensic audit of prior work, all using the same July 20 evidence set.

## Results  
Performance metrics include a ROC AUC of 0.874 for the local‑minimum model and 0.896 for the maximum model, but average precision was low at 0.134 and 0.116 respectively. The selector’s net loss over seven cycles was –44.30 % versus a buy‑and‑hold loss of –41.20 %. Model‑specific July results showed the local‑minimum policy’s –1.79 % return and the sell‑to‑cash/re‑entry’s –2.80 % underperformance relative to continuous holding, with gross mean advantages of 11.11 bps and 12.21 bps respectively—both below the 21‑bps stress benchmark.

## Significance  
The study underscores that high predictive accuracy does not guarantee profitable trading when transaction costs are factored in; many AI‑assisted event‑ranking models produce negative or negligible returns. It also highlights the importance of rigorous methodological audits to avoid hidden biases and flawed experiment design, which can mislead practitioners into believing otherwise.

## Related Concepts  
candle‑based modeling, extrema prediction, Binance Spot trading, ROC AUC, average precision, forced‑selection policies, event‑ranking, deterministic simulation, forensic audit, human‑supervised AI assistance.
