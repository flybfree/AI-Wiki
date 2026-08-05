# Summary: 2026-08-03_04-42-28Z_ARM_Detector_AgnosticChangepointAttributionwithFin.md
Saved: 2026-08-04 00:29
Source: 2026-08-03_04-42-28Z_ARM_Detector_AgnosticChangepointAttributionwithFin.md
Model: None

---

## Summary  
The paper introduces ARM (Attribution by Rank Maxima), a detector‑agnostic method that, given any changepoint location estimated by an arbitrary detector, returns the set of coordinates certified to have changed and assigns each a type label. It does so without requiring predefined coordinate groups or exact split locations, thereby addressing the incompleteness of existing block‑level procedures. ARM’s core innovation is using a max‑over‑splits rank statistic that dominates the estimator’s rank at the estimated changepoint, guaranteeing that the resulting certificate is invariant to both the detection method and its accuracy. The approach also provides rigorous finite‑sample error control across coordinates.

## Semantic links
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- Finite‑sample family‑wise error control via a Westfall–Young joint permutation test with a fully distribution‑free Holm fallback.  
- Detector‑agnostic attribution: the max‑over‑splits rank statistic yields a certificate that is valid regardless of how accurately the changepoint estimate is obtained.  
- High‑dimensional false discovery rate control through Benjamini–Yekutieli and e‑BH methods, preserving validity under arbitrary coordinate dependence.

## Methodology  
ARM works by accepting an estimated changepoint from any detector and then computing a per‑coordinate “max‑over‑splits rank” statistic. Because this statistic is always at least as large as the rank of the estimator’s score at the split, it serves as a certificate that the coordinate changed. Validity is ensured by analyzing within‑coordinate ranks alone; error control follows from permutation theory: a Westfall–Young joint test controls the family‑wise error rate, while Holm provides an exact sequential correction. For high dimensions, Benjamini–Yekutieli and e‑BH bound the false discovery rate under any dependence structure.

## Results  
Simulations demonstrate that naïve per‑coordinate testing at the estimated changepoint inflates the family‑wise error to about 0.66 as dimensionality grows, whereas ARM maintains the nominal level while retaining power in high dimensions and handling heavy tails. On five financial series surrounding the 2008 market collapse, ARM correctly attributes a scale change to every asset class and excludes injected control coordinates, confirming its robustness.

## Significance  
ARM supplies rigorous error guarantees for changepoint attribution, enabling reliable identification of changed variables across many dimensions without relying on detector accuracy or coordinate‑selection methods that lack finite‑sample assurances. This is crucial for applications where false attributions are costly, such as finance and health monitoring.

## Related Concepts  
changepoint detection, finite‑sample error control, Westfall–Young permutation test, Holm sequential testing, Benjamini–Yekutieli FDR correction, e‑BH, max‑over‑splits rank statistic, attribute attribution.
