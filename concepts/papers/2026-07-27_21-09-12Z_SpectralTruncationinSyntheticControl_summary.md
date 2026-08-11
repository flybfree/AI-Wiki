# Summary: 2026-07-27_21-09-12Z_SpectralTruncationinSyntheticControl.md
Saved: 2026-07-28 22:25
Source: 2026-07-27_21-09-12Z_SpectralTruncationinSyntheticControl.md
Model: None

---

## Summary  
The paper investigates Spectral Synthetic Control, a matching approach that uses the leading temporal singular vectors of donor units to define coordinates for the treated unit, and proposes a hybrid estimator that balances retained versus discarded spectral directions. It proves theoretical properties linking full‑rank synthetic control to raw‑path SC, underdetermination when donors exceed dimensions, and bias from spectral imbalance via best‑linear‑predictor decomposition. The authors evaluate this framework across eleven data‑generating regimes with Monte Carlo experiments, showing performance trade‑offs between truncation and raw‑path matching.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Spectral SC reduces to raw‑path SC at full rank; the hybrid estimator nests both extremes.  
- [Finding 2] When the number of donors \(N_0 > K+1\), exact balance on \(K\) retained dimensions is underdetermined, yielding an affine solution set of dimension \(N_0-K-1\).  
- [Finding 3] Spectral imbalance introduces treatment‑effect bias through a finite‑sample best‑linear‑predictor decomposition.

## Methodology  
The authors construct the spectral decomposition of donor trajectories and split it into retained and discarded directions. A hybrid estimator assigns tunable weights to each direction, nesting raw‑path SC (all retained) and truncated Spectral SC (some discarded). They generate eleven data‑generating regimes, run 400 replications per regime, tune regularization and mixing weight, and compute RMSE using donor‑only placebo validation.

## Results  
Truncated Spectral SC has higher RMSE than tuned raw‑path SC in every regime; paired differences are 4–11 Monte Carlo standard errors. The hybrid estimator often selects raw‑path matching and is statistically indistinguishable from tuned SC, except when unit and time fixed effects are removed before spectral decomposition—then the gap shrinks and placebo validation favors truncation.

## Significance  
The findings highlight that spectral matching can improve only after removing confounding biases; otherwise raw‑path SC remains preferable. The results clarify underdetermination, basis‑estimation noise, and the impact of preprocessing on performance, offering a diagnostic rather than prescriptive conclusion about replacing synthetic control with Spectral SC.

## Related Concepts  
Synthetic Control, spectral decomposition, singular vectors, best‑linear‑predictor decomposition, underdetermined linear systems, fixed‑effect removal, RMSE, placebo validation.
