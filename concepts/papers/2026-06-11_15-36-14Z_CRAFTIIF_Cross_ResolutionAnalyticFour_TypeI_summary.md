# Summary: 2026-06-11_15-36-14Z_CRAFTIIF_Cross_ResolutionAnalyticFour_TypeInterpre.md
Saved: 2026-06-11 21:01
Source: 2026-06-11_15-36-14Z_CRAFTIIF_Cross_ResolutionAnalyticFour_TypeInterpre.md
Model: None

---


## Summary  
The paper introduces CRAFTIIF, a fully unsupervised framework that simultaneously detects four distinct types of anomalies in multivariate time series—point spikes, distributional level shifts, temporal rhythm changes, and collective inter‑sensor correlation breakdowns. It accomplishes this by generating five structured Isolation Forests, each trained on wavelet features tailored to one anomaly type plus a meta‑IF for compound cases, while employing an adaptive Otsu/MAD threshold that automatically calibrates across anomaly rates from 0.1 % to 69.2 %. The approach provides per‑type attribution by construction and achieves state‑of‑the‑art performance on the mTSBench benchmark.  

## Key Contributions  
- CRAFTIIF detects all four anomaly types simultaneously with direct type attribution via branch firing.  
- Adaptive Otsu/MAD threshold calibration works across a wide range of anomaly rates without dataset‑specific tuning.  
- The meta‑IF improves detection of compound anomalies, raising VUS‑PR F1 from 0.329 to 0.463 (+40.7 %).  

## Methodology  
The authors construct five Isolation Forests: four use feature families (Morlet, DOG, Haar, Coiflet) each tuned to a specific anomaly type; the fifth meta‑IF combines them. Random analytic wavelet features are drawn across resolutions and types, feeding structured thresholds that are calibrated by an adaptive Otsu/MAD rule.  

## Results  
On all 19 datasets of the mTSBench benchmark CRAFTIIF attains a mean F1 of 0.228 (overall) and 0.322 on the 13 detectable datasets, ranking first among 25 evaluated methods. In VUS‑PR it scores 0.463 versus the previous best 0.329, an improvement of +40.7 %. A diagnostic framework (oracle F1, detectability limits, branch separation ratios) identifies six datasets as fundamentally undetectable by any unsupervised method. Ablation studies confirm that adaptive thresholding (+38 % F1), the four‑branch structure (+20 %), and the meta‑IF (+23 %) are each essential.  

## Significance  
CRAFTIIF advances interpretable anomaly detection for multivariate time series by handling diverse temporal patterns in a single model, eliminating manual tuning of thresholds or feature sets, and delivering built‑in type attribution that is crucial for real‑world monitoring where explainability matters.  

## Related Concepts  
- Isolation Forest (unsupervised outlier detection)  
- Wavelet feature extraction (Morlet, DOG, Haar, Coiflet)  
- Adaptive thresholding via Otsu/MAD  
- Multi‑type anomaly classification  
- Meta‑learning / ensemble of IFs
