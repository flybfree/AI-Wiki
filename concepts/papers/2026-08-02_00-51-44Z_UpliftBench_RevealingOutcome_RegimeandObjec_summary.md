# Summary: 2026-08-02_00-51-44Z_UpliftBench_RevealingOutcome_RegimeandObjectiveMis.md
Saved: 2026-08-03 23:57
Source: 2026-08-02_00-51-44Z_UpliftBench_RevealingOutcome_RegimeandObjectiveMis.md
Model: None

---

## Summary  
Uplift modeling aims to estimate the conditional average treatment effect for personalized interventions, but existing benchmarks often compare different metrics rather than models. The paper introduces UpliftBench, a systematic evaluation protocol that isolates the outer test and uses multi‑objective criteria across seven dataset families. It demonstrates that the apparent ranking disputes stem from objective mismatch: F1 is ineffective on continuous outcomes while AUUC aligns better with true effect accuracy; conversely, rank‑only metrics fail to capture sign‑threshold policy risk in a within‑sample case study. The findings are bounded by dataset and objective constraints, not universal truths. UpliftBench also provides versioned loaders, fixed protocols, artifacts, and a living leaderboard for reproducibility.

## Key Contributions  
- [Finding 1] F1 on the standard continuous benchmark (IHDP) shows negligible rank correlation with effect accuracy across all realizations, indicating it is not a reliable proxy.  
- [Finding 2] AUUC consistently outperforms Qini in aligning with true effect magnitude and even surpasses shipped cumulative‑gain AUUC; threshold calibration reduces Qini’s regret by 81 %.  
- [Finding 3] In the Jobs split‑rotation case study, direct policy‑risk selection yields lower benchmark regret than random model selection, while Qini, AUUC, and uplift‑at‑$k$ incur 14–15 % regret.

## Methodology  
UpliftBench evaluates twelve uplift estimators under an outer‑test‑isolated protocol across seven distinct dataset families (IHDP, ACIC, Revenue‑Synthetic, Jobs, etc.). For each family the authors compute multiple objectives: effect accuracy (F1/F2), rank correlation, and policy‑risk regret. The inner test is held fixed while the outer test varies to isolate estimator performance. Results are aggregated using versioned loaders and a reproducible leaderboard.

## Results  
On IHDP, mean rank correlation between Qini and effect accuracy is +0.07 (95 % CI [‑0.03, +0.16]), whereas AUUC’s paired prefix‑mean gap over Qini is +0.49 (+0.40 to +0.59). The shipped cumulative‑gain AUUC improves this to +0.73. In Jobs, direct policy‑risk selection reduces benchmark regret by 14–15 % compared with random model selection; threshold calibration eliminates most of Qini’s regret. F1 and F2 are not detected on ACIC or Revenue‑Synthetic splits.

## Significance  
These results clarify that uplift evaluation is driven more by objective choice than by estimator quality, guiding practitioners to select metrics aligned with their treatment‑effect goals. The bounded findings prevent overgeneralization and highlight the need for context‑aware benchmarking. UpliftBench’s open protocols enable transparent, reproducible research.

## Related Concepts  
- Conditional average treatment effect (CATE) estimation  
- F1/F2 as rank correlation metrics  
- Qini coefficient and AUUC ranking measures  
- Policy‑risk regret in uplift selection  
- Split‑rotation evaluation protocol
