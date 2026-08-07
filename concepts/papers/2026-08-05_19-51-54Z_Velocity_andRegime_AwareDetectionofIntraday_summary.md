# Summary: 2026-08-05_19-51-54Z_Velocity_andRegime_AwareDetectionofIntradayOptions.md
Saved: 2026-08-06 21:50
Source: 2026-08-05_19-51-54Z_Velocity_andRegime_AwareDetectionofIntradayOptions.md
Model: None

---

## Summary  
The paper proposes a detection method that identifies intraday options market manipulation by focusing on the velocity of market state rather than its level, providing explainable alerts via SHAP attribution and achieving high precision under a closed‑world assumption. It demonstrates that manipulation leaves a distinctive dynamic signature—a pump‑and‑crash pattern visible in the velocity of option Delta and equity price streams—enabling regulators to flag rare events with reliable explanations.

## Key Contributions  
- [Finding 1] The dynamic signature of pump‑and‑crash manipulation appears as a distinctive velocity pattern in both index options (Delta) and equities (price).  
- [Finding 2] Conditioning detection on hidden Markov‑inferred market regimes improves precision but reduces recall; the closed‑world assumption yields near 25 % precision.  
- [Finding 3] Exact SHAP attribution matches regulator‑identified days with cosine similarity 0.99, confirming alert reliability.

## Methodology  
The authors built a minute‑level pipeline that computes smoothed velocity of index options (Delta) and equities (price), filters alerts via thresholds set before evaluation, uses a hidden Markov model to infer regimes, and applies SHAP for explainability; the test period is strictly out‑of‑sample.

## Results  
On the Indian BANKNIFTY index‑options test, a plain autoencoder recovered 10 of 10 regulator‑identified manipulation days. Conditioning on regimes raises precision but lowers recall. Under the closed‑world assumption, precision hovers around 25 %. The same velocity signature appears in thinly traded U.S. equities (SEC v. Patel); pump‑reversal shape scores achieve AUC 0.91 (ARQQ) and 0.81 (ACY). SHAP attribution similarity between alerts and regulator days is 0.99.

## Significance  
The work shows that market manipulation leaves a velocity‑based dynamic fingerprint, allowing regulators to detect rare intraday events with explainable alerts while respecting precision limits; the signature transfers across markets and instrument types.

## Related Concepts  
Market manipulation detection, velocity analysis, hidden Markov models, regime switching, SHAP attribution, closed‑world assumption, pump‑and‑crash pattern, intraday options.
