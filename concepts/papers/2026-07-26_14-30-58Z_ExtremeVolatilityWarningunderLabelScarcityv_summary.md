# Summary: 2026-07-26_14-30-58Z_ExtremeVolatilityWarningunderLabelScarcityviaMulti.md
Saved: 2026-07-27 21:29
Source: 2026-07-26_14-30-58Z_ExtremeVolatilityWarningunderLabelScarcityviaMulti.md
Model: None

---

## Summary  
Early warning of extreme market volatility is essential for financial risk management, yet actionable events are rare and non‑stationary in the CSI ~300 index. The authors address this label‑scarcity problem by proposing AAMSF (Anomaly‑Augmented Multi‑Signal Fusion) and its temporal extension T‑AAMSF, which fuse anomaly scores from market indicators, GDELT events, Chinese financial news, and English media using a lightweight Ridge fusion scheme. Their framework avoids the instability of large hierarchical text‑signal models when only ~80 positive samples are available.

## Key Contributions  
- [Finding 1] A 100 K‑parameter hierarchical model deteriorates under low‑label regimes, highlighting the need for a semisupervised design that leverages unsupervised anomaly detection.  
- [Finding 2] AAMSF reaches an AUC‑ROC of 0.680 on CSI ~300 (2018–2023), surpassing both the strongest unsupervised baseline (0.630) and a neural baseline (0.588).  
- [Finding 3] Ablation studies reveal source asymmetry: GDELT events and domestic financial news improve performance, while English media degrades it; learned weighting is unreliable under validation noise.

## Methodology  
The authors first analyze the failure of a hierarchical text‑signal fusion (HTSF) model with 100 K parameters in the low‑label environment. To remedy this, they introduce AAMSF, which combines Isolation Forest anomaly scores from four data sources—market indicators, GDELT events, Chinese financial news, and English media—via a simple Ridge regression that aggregates these scores into a single risk signal. T‑AAMSF extends this approach by accumulating anomalies over multiple days to capture longer‑horizon volatility triggers.

## Results  
On the CSI ~300 dataset (2018–2023), AAMSF achieves an AUC‑ROC of 0.680, outperforming all baselines. Its temporal extension T‑AAMSF improves PR‑AUC to 0.291, indicating better detection of rare extreme events. Ablation experiments confirm that the fusion of GDELT and domestic news provides complementary risk information, whereas English media introduces noise that degrades performance.

## Significance  
The work supplies an empirical design principle for label‑scarce financial risk warning: robust anomaly geometry and reliable source data matter more than the capacity of supervised representations. By integrating unsupervised anomaly scores with a lightweight fusion layer, AAMSF demonstrates that semisupervised strategies can outperform large hierarchical models when labels are scarce.

## Related Concepts  
- Extreme volatility early warning  
- Semisupervised learning  
- Multi‑source signal fusion  
- Isolation Forest anomaly detection  
- Ridge regression for score aggregation  
- Label scarcity in financial data  
- Temporal anomaly accumulation
